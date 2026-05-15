#!/usr/bin/env python3
"""
Local scheduled runner for daily_arxiv.py.
Replaces GitHub Actions: fetches papers, commits, and pushes automatically.

Environment variables:
    GITHUB_TOKEN    - GitHub personal access token (for authenticated push)
    ARXIV_CRON      - Cron schedule expression (default: "0 12 * * 1-5", weekdays at noon)
    ARXIV_RUN_ONCE  - Set to "1" to run once and exit (no scheduling)
"""

import os
import sys
import time
import logging
import subprocess
import schedule
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO
)

REPO_DIR = Path(__file__).resolve().parent
COMMIT_MESSAGE = "Automatic Update CV Arxiv Papers"


def run_command(cmd, cwd=None):
    result = subprocess.run(
        cmd, cwd=cwd or REPO_DIR,
        capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        logging.error(f"Command failed: {' '.join(cmd)}\nstderr: {result.stderr}")
    return result


def setup_git_remote():
    """Configure remote URL with token for authenticated push if GITHUB_TOKEN is set."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        logging.info("No GITHUB_TOKEN set, assuming SSH or credential-helper auth")
        return

    result = run_command(["git", "remote", "get-url", "origin"])
    if result.returncode != 0:
        return
    url = result.stdout.strip()

    if url.startswith("https://") and f"{token}@" not in url:
        authed_url = url.replace("https://", f"https://x-access-token:{token}@")
        run_command(["git", "remote", "set-url", "origin", authed_url])
        logging.info("Configured remote with GITHUB_TOKEN")


def git_pull():
    logging.info("Pulling latest changes...")
    result = run_command(["git", "pull", "--rebase", "origin", "main"])
    if result.returncode != 0:
        logging.warning(f"Pull failed, trying without rebase: {result.stderr}")
        run_command(["git", "pull", "origin", "main"])


def run_arxiv():
    logging.info("Running daily_arxiv.py ...")
    result = run_command(
        [sys.executable, "daily_arxiv.py", "--config_path", "config.yaml"],
        cwd=REPO_DIR
    )
    if result.returncode != 0:
        logging.error(f"daily_arxiv.py failed:\n{result.stderr}")
        return False
    logging.info("daily_arxiv.py completed successfully")
    return True


def git_commit_and_push():
    status = run_command(["git", "status", "--porcelain"])
    if not status.stdout.strip():
        logging.info("No changes to commit")
        return

    run_command(["git", "add", "-A"])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"{COMMIT_MESSAGE} ({now})"
    result = run_command(["git", "commit", "-m", msg])
    if result.returncode != 0:
        logging.error(f"Commit failed: {result.stderr}")
        return

    logging.info(f"Committed: {msg}")

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        result = run_command(["git", "push", "origin", "main"])
        if result.returncode == 0:
            logging.info("Pushed to origin/main")
            return
        logging.warning(f"Push failed (attempt {attempt}/{max_retries}): {result.stderr}")
        if attempt < max_retries:
            time.sleep(5 * attempt)
            git_pull()

    logging.error("Push failed after all retries")


def job():
    logging.info("=== Starting scheduled run ===")
    try:
        git_pull()
        success = run_arxiv()
        if success:
            git_commit_and_push()
    except Exception as e:
        logging.error(f"Job failed with exception: {e}")
    logging.info("=== Run complete ===")


def parse_cron_to_schedule(cron_expr):
    """Parse a simple cron expression and register with `schedule`.
    Supports: 'M H * * D' where D is day-of-week (0=Sun or 1-5 for weekdays).
    """
    parts = cron_expr.strip().split()
    if len(parts) != 5:
        raise ValueError(f"Invalid cron expression: {cron_expr}")

    minute, hour, _, _, dow = parts
    time_str = f"{int(hour):02d}:{int(minute):02d}"

    if dow == "*":
        schedule.every().day.at(time_str).do(job)
        logging.info(f"Scheduled: every day at {time_str}")
    elif dow == "1-5":
        for day_func in [schedule.every().monday, schedule.every().tuesday,
                         schedule.every().wednesday, schedule.every().thursday,
                         schedule.every().friday]:
            day_func.at(time_str).do(job)
        logging.info(f"Scheduled: weekdays at {time_str}")
    elif dow == "0-6":
        schedule.every().day.at(time_str).do(job)
        logging.info(f"Scheduled: every day at {time_str}")
    else:
        day_map = {"0": "sunday", "1": "monday", "2": "tuesday",
                   "3": "wednesday", "4": "thursday", "5": "friday", "6": "saturday"}
        for d in dow.split(","):
            d = d.strip()
            if d in day_map:
                getattr(schedule.every(), day_map[d]).at(time_str).do(job)
        logging.info(f"Scheduled: days={dow} at {time_str}")


def main():
    os.chdir(REPO_DIR)
    setup_git_remote()

    run_once = os.environ.get("ARXIV_RUN_ONCE", "0") == "1"

    if run_once:
        job()
        return

    cron_expr = os.environ.get("ARXIV_CRON", "0 12 * * 1-5")
    parse_cron_to_schedule(cron_expr)

    logging.info("Scheduler started. Press Ctrl+C to stop.")
    job()  # run immediately on start

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
