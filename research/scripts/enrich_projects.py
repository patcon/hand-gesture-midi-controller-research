#!/usr/bin/env python3
# /// script
# dependencies = ["requests", "tqdm"]
# ///
"""
Enrich projects.csv with commit_count and commit_duration_days columns.

commit_count        = total number of commits in the default branch
commit_duration_days = days between first and last commit (0 if only 1 commit)

Uses the Link header trick for GitHub (per_page=1 → last page number = total count)
and X-Total header for GitLab. One extra request per repo to fetch the oldest commit.

Usage:
    uv run research/scripts/enrich_projects.py
    uv run research/scripts/enrich_projects.py --ids 1 2 gl-1   # specific projects only
    uv run research/scripts/enrich_projects.py --dry-run
"""

import csv
import re
import subprocess
import sys
import time
import argparse
from datetime import datetime, timezone
from pathlib import Path

import requests
from tqdm import tqdm

REPO_ROOT = Path(__file__).parent.parent.parent
PROJECTS_CSV = REPO_ROOT / "projects.csv"


def gh_token() -> str:
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    token = result.stdout.strip()
    if not token:
        sys.exit("Could not get GitHub token via `gh auth token`.")
    return token


def parse_last_page(link_header: str) -> int | None:
    """Extract the last page number from a GitHub Link header."""
    match = re.search(r'page=(\d+)>; rel="last"', link_header or "")
    return int(match.group(1)) if match else None


def parse_date(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def github_commit_stats(owner: str, repo: str, token: str) -> dict | None:
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

    # Most recent commit (page 1, per_page 1, default desc order)
    resp = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits",
        headers=headers,
        params={"per_page": 1},
    )
    if resp.status_code in (404, 409):  # 409 = empty repo
        return None
    resp.raise_for_status()

    commits = resp.json()
    if not commits:
        return {"commit_count": 0, "commit_duration_days": ""}

    last_commit_date = parse_date(commits[0]["commit"]["committer"]["date"])

    # Total count from Link header; if no "last" rel, there's exactly 1 page = 1 commit
    total = parse_last_page(resp.headers.get("Link", "")) or 1

    if total == 1:
        return {"commit_count": 1, "commit_duration_days": 0}

    # Oldest commit = last page in descending order
    time.sleep(0.1)
    resp2 = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits",
        headers=headers,
        params={"per_page": 1, "page": total},
    )
    resp2.raise_for_status()
    oldest = resp2.json()
    if not oldest:
        return {"commit_count": total, "commit_duration_days": ""}

    first_commit_date = parse_date(oldest[0]["commit"]["committer"]["date"])
    duration = (last_commit_date - first_commit_date).days

    return {"commit_count": total, "commit_duration_days": duration}


def gitlab_commit_stats(namespace: str, repo: str) -> dict | None:
    encoded = f"{namespace}%2F{repo}"

    # Most recent commit
    resp = requests.get(
        f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits",
        params={"per_page": 1},
    )
    if resp.status_code == 404:
        return None
    resp.raise_for_status()

    total = int(resp.headers.get("X-Total", 0))
    commits = resp.json()

    if not commits or total == 0:
        return {"commit_count": 0, "commit_duration_days": ""}

    last_commit_date = parse_date(commits[0]["committed_date"])

    if total == 1:
        return {"commit_count": 1, "commit_duration_days": 0}

    # Oldest commit (ascending order)
    time.sleep(0.1)
    resp2 = requests.get(
        f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits",
        params={"per_page": 1, "order": "asc"},
    )
    resp2.raise_for_status()
    oldest = resp2.json()
    if not oldest:
        return {"commit_count": total, "commit_duration_days": ""}

    first_commit_date = parse_date(oldest[0]["committed_date"])
    duration = (last_commit_date - first_commit_date).days

    return {"commit_count": total, "commit_duration_days": duration}


def main():
    parser = argparse.ArgumentParser(description="Enrich projects.csv with commit stats")
    parser.add_argument("--ids", nargs="+", help="Only process these project IDs (e.g. 1 2 gl-1)")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    token = gh_token()
    filter_ids = set(args.ids) if args.ids else None

    rows = []
    with open(PROJECTS_CSV, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    new_fields = ["commit_count", "commit_duration_days"]
    for field in new_fields:
        if field not in fieldnames:
            fieldnames.append(field)

    for row in tqdm(rows, desc="Fetching commit stats"):
        pid = row["id"]
        url = row["url"]

        if filter_ids and pid not in filter_ids:
            continue

        # Skip if already populated and not explicitly requested
        if not filter_ids and row.get("commit_count") not in (None, ""):
            continue

        gh_match = re.match(r"https://github\.com/([^/]+)/([^/]+)", url)
        gl_match = re.match(r"https://gitlab\.com/([^/]+)/([^/]+)", url)

        if gh_match:
            owner, repo = gh_match.groups()
            stats = github_commit_stats(owner, repo, token)
        elif gl_match:
            namespace, repo = gl_match.groups()
            stats = gitlab_commit_stats(namespace, repo)
        else:
            tqdm.write(f"  {pid} ({row['name']}): unrecognised URL, skipping")
            continue

        if stats is None:
            tqdm.write(f"  {pid} ({row['name']}): not found")
            row["commit_count"] = ""
            row["commit_duration_days"] = ""
        else:
            tqdm.write(f"  {pid} ({row['name']}): {stats['commit_count']} commits, {stats['commit_duration_days']} days")
            row.update(stats)

        time.sleep(0.1)

    if args.dry_run:
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    else:
        with open(PROJECTS_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Written to {PROJECTS_CSV}")


if __name__ == "__main__":
    main()
