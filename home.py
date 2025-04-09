# This is a main class for project
from github import Github
from github import InputGitTreeElement
import common as c
# from repositoryhelper import RepositoryHelper
from branchhelper import BranchHelper
import git
# import git
import os

repo_url = "https://github.com/KevinLi000/.NetCore.git"  # Replace with your GitHub repository
repo_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "testRepository")
if not os.path.exists(repo_path):
    os.makedirs(repo_path)
    repo = git.Repo.clone_from(repo_url, repo_path)
else:
    repo = git.Repo(repo_path)

print(repo.git.status()) 

branch_name = "test3"
target_branch = "main"
if branch_name in repo.heads:
    repo.git.checkout(branch_name)
    print(f"Switched to existing branch '{branch_name}'")
else:
    repo.git.checkout('-b', branch_name)
    print(f"Created and switched to new branch '{branch_name}'")
current_branch = branch_name
# Get the base merge
merge_base = repo.merge_base(current_branch, target_branch)

# Get the latest branch
current_commit = repo.commit(current_branch)
target_commit = repo.commit(target_branch)
canMerge = False
if merge_base and merge_base[0] != current_commit:
    print(f"{current_branch} has unmerged changes to {target_branch}")
    canMerge = True
else:
    print(f"{current_branch} already merged {target_branch}")

if canMerge :
    # Get the active branch
    current_branch = repo.active_branch
    print(f"Current branch: {current_branch}")

    # Switch to main branch
    main_branch = "main"
    repo.git.checkout(main_branch)

    # Pull latest changes from remote main
    repo.git.pull("origin", main_branch)

    # Merge the current branch into main
    repo.git.merge(current_branch)

    # Push merged changes to remote
    repo.git.push("origin", main_branch)

    print(f"Successfully merged {current_branch} into {main_branch} and pushed to remote.")
else:
    file_name = "home.a.py"
    file_content = "#This is the entrance to excute the main method\nPrint('Hello, World')\ndef main():\nprint('Hello, World') \ndef main():\nprint('Hello, World')"

    # Create or modify a file
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, 'w') as f:
        f.write(file_content)

    repo.git.add(file_name)  # Stage the file
    repo.git.commit('-m', "Added a new feature 01")  # Commit changes
    print("Changes committed.")

    repo.git.push("origin", branch_name, set_upstream=True)
    print(f"Pushed branch '{branch_name}' to GitHub.")

    # Get the active branch
    current_branch = repo.active_branch
    print(f"Current branch: {current_branch}")

    # Switch to main branch
    main_branch = "main"
    repo.git.checkout(main_branch)

    # Pull latest changes from remote main
    repo.git.pull("origin", main_branch)

    # Merge the current branch into main
    repo.git.merge(current_branch)

    # Push merged changes to remote
    repo.git.push("origin", main_branch)

    print(f"Successfully merged {current_branch} into {main_branch} and pushed to remote.")