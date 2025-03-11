# This is a main class for project
# from github import Github
# from configs import app as config
# from github import InputGitTreeElement

# # Authenticate using your GitHub token
# g = Github(config.AccessToken)

# # Get a repository
# repo = g.get_repo("KevinLi000/Python")

# # Get the main branch
# main_ref = repo.get_git_ref("heads/main")
# main_sha = main_ref.object.sha

# file_path = "python/test.txt"
# file_content = "This is an automated commit."
# file_sha = repo.get_contents(file_path).sha if repo.get_contents(file_path) else None

# # Create a new commit
# repo.update_file(file_path, "Add new file", file_content, file_sha)
# print("File committed successfully!")
# pr = repo.create_pull(
#     title="Automated PR",
#     body="This is an automatically created pull request.",
#     head='heads/main',
#     base="main"
# )
# print(f"Pull Request created: {pr.html_url}")