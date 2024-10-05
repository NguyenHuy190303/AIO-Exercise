import os
import subprocess
import random
from datetime import datetime, timedelta

# === CONFIG ===
start_date = datetime(2024, 6, 1)
end_date = datetime(2025, 3, 31)
max_commits_per_day = 2  # Số commit tối đa mỗi ngày (để tránh spam quá nhiều)
auto_push_every = 10     # Tự động push sau mỗi n commit

# === GIT FUNCTION ===
def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def stage_all_changes():
    run_cmd("git add .")
    run_cmd("git add -u")  # Cập nhật cả file deleted

def make_commit(commit_date, commit_msg):
    env = os.environ.copy()
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", commit_msg], env=env)

def auto_commit_push():
    total_commits = 0
    while total_commits < 50:  # Có thể thay đổi tùy số lượng commit muốn tạo
        commit_date = random_date(start_date, end_date)
        stage_all_changes()
        commit_msg = f"Auto commit on {commit_date.strftime('%Y-%m-%d')}"
        make_commit(commit_date, commit_msg)
        total_commits += 1
        print(f"[+] Committed: {commit_msg}")

        if total_commits % auto_push_every == 0:
            run_cmd("git push origin master")
            print("[↑] Auto pushed to remote.")

    run_cmd("git push origin master")
    print("[✓] Final push done.")

if __name__ == "__main__":
    auto_commit_push()
