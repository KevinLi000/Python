class Repostory:
    def __init__(self, github):
       self.github = github
    def __new__(cls, value):
        print("Creating new instance...")
        instance = super(ExampleClass, cls).__new__(cls)
        return instance
    def getRepository(self, repoName):
    # Authenticate using your GitHub token
        g = self.github(config.AccessToken)


