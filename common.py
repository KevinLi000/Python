from github import Github
#generate github by access token
def generateGitHubByAccessToken(accessToken):
    return Github(accessToken)