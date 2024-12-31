import os
import subprocess
from datetime import datetime, timedelta

# === CONFIG ===
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 3, 31)
auto_push_every = 10     # Tự động push sau mỗi n commit

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def stage_all_changes():
    run_cmd("git add .")
    run_cmd("git add -u")

def make_commit(commit_date, commit_msg):
    env = os.environ.copy()
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", commit_msg], env=env)

def auto_commit_push():
    total_commits = 0
    current_date = start_date

    while current_date <= end_date:
        stage_all_changes()

        # Check nếu không có gì để commit thì bỏ qua
        status = run_cmd("git status --porcelain")
        if not status:
            print(f"[!] No changes to commit on {current_date.strftime('%Y-%m-%d')}")
            break

        commit_msg = f"Auto commit on {current_date.strftime('%Y-%m-%d')}"
        make_commit(current_date, commit_msg)
        print(f"[+] Committed: {commit_msg}")
        total_commits += 1

        if total_commits % auto_push_every == 0:
            run_cmd("git push origin master")
            print("[↑] Auto pushed to remote.")

        current_date += timedelta(days=7)

    run_cmd("git push origin master")
    print("[✓] Final push done.")

if __name__ == "__main__":
    auto_commit_push()
