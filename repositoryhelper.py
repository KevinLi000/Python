from github import GithubException
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