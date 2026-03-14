#!/usr/bin/env python3
# /// script
# dependencies = ["requests", "tqdm"]
# ///
"""
Enrich people.csv with source_repo_count and source_repo_stars columns.

Source repos = repos the user created (not forks).

Usage:
    uv run research/scripts/enrich_people.py
    uv run research/scripts/enrich_people.py --users akx johnowhitaker   # specific users only
    uv run research/scripts/enrich_people.py --dry-run                   # print without writing
"""

import csv
import subprocess
import sys
import time
import argparse
from datetime import datetime, timezone
from pathlib import Path

import requests
from tqdm import tqdm

REPO_ROOT = Path(__file__).parent.parent.parent
PEOPLE_CSV = REPO_ROOT / "people.csv"


def gh_token() -> str:
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    token = result.stdout.strip()
    if not token:
        sys.exit("Could not get GitHub token via `gh auth token`. Is gh installed and authenticated?")
    return token


def fetch_source_repo_stats(username: str, token: str) -> dict | None:
    """Return stats dict for a GitHub user/org, or None if not found."""
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    source_count = 0
    total_stars = 0
    most_recent_push = None
    one_year_ago = datetime.now(timezone.utc).replace(year=datetime.now().year - 1)
    repos_active_last_year = 0
    page = 1

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        resp = requests.get(url, headers=headers, params={"per_page": 100, "page": page, "type": "owner"})

        if resp.status_code == 404:
            return None

        resp.raise_for_status()
        repos = resp.json()

        if not repos:
            break

        for repo in repos:
            if not repo["fork"]:
                source_count += 1
                total_stars += repo["stargazers_count"]

                pushed_at = repo.get("pushed_at")
                if pushed_at:
                    pushed_dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
                    if most_recent_push is None or pushed_dt > most_recent_push:
                        most_recent_push = pushed_dt
                    if pushed_dt >= one_year_ago:
                        repos_active_last_year += 1

        if len(repos) < 100:
            break
        page += 1
        time.sleep(0.1)  # stay well under rate limits

    return {
        "source_repo_count": source_count,
        "source_repo_stars": total_stars,
        "most_recent_push": most_recent_push.date().isoformat() if most_recent_push else "",
        "repos_active_last_year": repos_active_last_year,
    }


def main():
    parser = argparse.ArgumentParser(description="Enrich people.csv with source repo stats")
    parser.add_argument("--users", nargs="+", help="Only process these usernames")
    parser.add_argument("--dry-run", action="store_true", help="Print results without writing CSV")
    args = parser.parse_args()

    token = gh_token()

    rows = []
    with open(PEOPLE_CSV, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Add new columns if not present
    new_fields = ["source_repo_count", "source_repo_stars", "most_recent_push", "repos_active_last_year"]
    for field in new_fields:
        if field not in fieldnames:
            fieldnames = fieldnames + [field]

    filter_users = set(args.users) if args.users else None

    for row in tqdm(rows, desc="Fetching repo stats"):
        username = row["username"]
        platform = row["platform"]

        if filter_users and username not in filter_users:
            continue

        if platform != "github":
            for field in new_fields:
                row.setdefault(field, "")
            continue

        # Skip if already populated and not in explicit user filter
        if not filter_users and row.get("most_recent_push") and row.get("repos_active_last_year"):
            continue

        stats = fetch_source_repo_stats(username, token)

        if stats is None:
            tqdm.write(f"  {username}: not found")
            for field in new_fields:
                row[field] = ""
        else:
            tqdm.write(f"  {username}: {stats['source_repo_count']} source repos, {stats['source_repo_stars']} stars, last push {stats['most_recent_push']}, {stats['repos_active_last_year']} active last year")
            row.update(stats)

    if args.dry_run:
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    else:
        with open(PEOPLE_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Written to {PEOPLE_CSV}")


if __name__ == "__main__":
    main()
