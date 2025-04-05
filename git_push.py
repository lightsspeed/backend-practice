import subprocess

def run_cmd(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        # Git may use stderr for normal output, so don't treat all stderr as errors
        if result.returncode != 0:
            print(f"[ERROR] {result.stderr.strip()}")
        else:
            print(f"[GIT OUTPUT] {result.stderr.strip()}")
    return result.returncode == 0

def git_push(commit_msg="Update via script", branch="main"):
    print("🌀 Staging all changes...")
    run_cmd("git add .")

    print("📝 Committing...")
    run_cmd(f'git commit -m "{commit_msg}"')

    print("🚀 Pushing to remote...")
    run_cmd(f"git push origin {branch}")

if __name__ == "__main__":
    git_push(commit_msg="Auto update", branch="main")
