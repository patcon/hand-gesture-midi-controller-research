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


def fetch_source_repo_stats(username: str, token: str) -> tuple[int, int]:
    """Return (source_repo_count, total_stars) for a GitHub user/org."""
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    source_count = 0
    total_stars = 0
    page = 1

    while True:
        # Try user endpoint first, fall back to org endpoint
        url = f"https://api.github.com/users/{username}/repos"
        resp = requests.get(url, headers=headers, params={"per_page": 100, "page": page, "type": "owner"})

        if resp.status_code == 404:
            return None, None

        resp.raise_for_status()
        repos = resp.json()

        if not repos:
            break

        for repo in repos:
            if not repo["fork"]:
                source_count += 1
                total_stars += repo["stargazers_count"]

        if len(repos) < 100:
            break
        page += 1
        time.sleep(0.1)  # stay well under rate limits

    return source_count, total_stars


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
    new_fields = ["source_repo_count", "source_repo_stars"]
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
            row.setdefault("source_repo_count", "")
            row.setdefault("source_repo_stars", "")
            continue

        # Skip if already populated and not in explicit user filter
        if not filter_users and row.get("source_repo_count") and row.get("source_repo_stars"):
            continue

        count, stars = fetch_source_repo_stats(username, token)

        if count is None:
            tqdm.write(f"  {username}: not found")
            row["source_repo_count"] = ""
            row["source_repo_stars"] = ""
        else:
            tqdm.write(f"  {username}: {count} source repos, {stars} total stars")
            row["source_repo_count"] = count
            row["source_repo_stars"] = stars

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
