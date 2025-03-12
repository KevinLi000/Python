class Repostory:
    def __init__(self, github):
       self.github = github
    def getRepository(self, repoName):
    # Authenticate using your GitHub token
        repo = self.github.get_repo(repoName)
        return repo


