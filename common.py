from github import Github
import subprocess
#generate github by access token
def generateGitHubByAccessToken(accessToken):
    return Github(accessToken)
def run_command(command):
    """Excute shell command and return re"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()
"""
# branch_name: the branch name
"""
def push_branch(branch_name, remote="origin"):
    """Commit the current changes and push it to remote branch"""
    # Add all files
    run_command("git add .")
    
    # Commit the changes
    commit_message = f"Auto commit changes to {branch_name}"
    run_command(f'git commit -m "{commit_message}"')
    
    # Push to remote
    run_command(f"git push {remote} {branch_name}")
    print(f"Branch {branch_name} pushed to {remote}")