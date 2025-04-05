import subprocess

def run_cmd(command):
    """Runs a shell command and prints output"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("[ERROR]", result.stderr)
    return result.returncode == 0

def git_push(commit_msg="Update via script"):
    print("🌀 Staging all changes...")
    run_cmd("git add .")

    print("📝 Committing...")
    run_cmd(f'git commit -m "{commit_msg}"')

    print("🚀 Pushing to remote...")
    run_cmd(f"git push origin {branch}")

# Customize your message and branch
if __name__ == "__main__":
    git_push(commit_msg="Auto update")

