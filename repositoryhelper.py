from github import GithubException
import git
import os
import subprocess

class RepositoryHelper:
    def __init__(self, github):
       self.github = github
    def getRepository(self, repoName):
        try:
            repo = self.github.get_repo(repoName)
            return repo
        except GithubException as e:
            print(e)
            if e.status == 404:
                user = self.github.get_user()
                print(user)
                # repo does not exist, create it
                repo = user.create_repo(repoName)
                return repo
            else:
                # Other excetions
                return
    def push_new_branch(repo_path, branch_name, commit_message, file_name, file_content, remote_name="origin"):
        try:
            # Open the existing repository or clone if not present
            if not os.path.exists(repo_path):
                print(f"Repository path '{repo_path}' does not exist.")
                return
            
            repo = git.Repo(repo_path)
            
            # Fetch the latest updates
            repo.git.fetch()
            
            # Check if branch exists locally
            if branch_name in repo.heads:
                repo.git.checkout(branch_name)
                print(f"Switched to existing branch '{branch_name}'.")
            else:
                repo.git.checkout('-b', branch_name)
                print(f"Created and switched to new branch '{branch_name}'.")
            
            # Create or modify a file
            file_path = os.path.join(repo_path, file_name)
            with open(file_path, 'w') as f:
                f.write(file_content)
            
            # Add changes
            repo.git.add(file_name)
            
            # Commit changes
            repo.git.commit('-m', commit_message)
            print(f"Committed changes: {commit_message}")
            
            # Push the branch to remote repository
            repo.git.push(remote_name, branch_name, set_upstream=True)
            print(f"Branch '{branch_name}' successfully pushed to remote '{remote_name}'.")

        except Exception as e:
            print(f"Error: {e}")

    def switch_or_create_branch(self,repo, branch_name, remote_name='origin'):
        # Check whether the branch exists
        branches = [branch.name for branch in repo.get_branches()]
        for branch in branches:
            print(branch.strip())
        if branch_name in branches:
            print(f"分支 '{branch_name}' 已存在，切换到该分支。")
            repo.checkout(branch_name)
        else:
            print(f"分支 '{branch_name}' 不存在，创建新分支。")
            repo.checkout('-b', branch_name)

        # 推送分支到远端
        repo.push(remote_name, branch_name, set_upstream=True)
        print(f"分支 '{branch_name}' 已成功推送到远程 '{remote_name}'。")