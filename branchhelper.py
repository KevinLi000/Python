
class BranchHelper:
    """
    # Intialize the contructor method
    """
    def __init__(self, repo):
        self.repo = repo
    def getOrCreateBranch(self, branch_name):
        branches = [branch.name for branch in self.repo.get_branches()]
        if branch_name in branches:
            print('branch exists')
            # Get the main branch
            branch_ref = self.repo.get_git_ref("heads/"+branch_name)
            branch_sha = branch_ref.object.sha
            print(branch_sha)
        else:
            new_branch = self.repo.git.create_head(branch_name)
            self.repo.git.push('origin', branch_name)
