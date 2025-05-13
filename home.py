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
status = repo.git.status()
print("status=",status) 

branch_name = "test_new"
target_branch = "main"
if branch_name in repo.heads:
    try:
        print(f"Switching to existing branch '{branch_name}'")
        repo.git.restore('--staged', '.')
        repo.git.checkout(branch_name)
        print(f"Switched to existing branch '{branch_name}'")
    except Exception as e:
        print(f"Error switching to branch '{branch_name}': {e}")
        # Handle the error (e.g., create a new branch or notify the user)
        # For example, you can create a new branch with a different name
        repo.git.restore('--staged', '.')
        repo.index.commit("Save staged changes before checkout")        
        new_branch_name = f"{branch_name}"
        repo.git.checkout('-b', new_branch_name)
        print(f"Created and switched to new branch '{new_branch_name}'")
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
    #Checkout and merge safely
    if safe_checkout_and_merge(repo, main_branch, current_branch):
        try:
            repo.git.push("origin", main_branch)
            print(f"Successfully merged {current_branch} into {main_branch} and pushed")
        except git.exc.GitCommandError as e:
            print(f"Push failed: {e}")
    else:
        print("Merge operation failed - please resolve conflicts manually")

    print(f"Successfully merged {current_branch} into {main_branch} and pushed to remote.")
else:
    #Filename and content to be added
    file_name = "index.py"
    file_content = "#This is the entrance to excute the main method\nPrint('Hello, World')\ndef main():\nprint('Hello, World') \ndef main():\nprint('Hello, World')"

    # Create or modify a file
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, 'w') as f:
        f.write(file_content)
    # Stage the file
    repo.git.add(file_name)
    # Commit changes
    repo.git.commit('-m', "Added a new feature 01")  
    print("Changes committed.")
    # Push changes
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
# This is a main class for project
def safe_checkout_and_merge(repo, target_branch, source_branch):
    try:
        # Check for uncommitted changes
        if repo.is_dirty(untracked_files=True):
            print(f"Stashing uncommitted changes before checkout")
            repo.git.stash('save', f"Temporary stash before switching to {target_branch}")
            has_stashed = True
        else:
            has_stashed = False

        # Checkout target branch
        print(f"Checking out {target_branch}")
        repo.git.checkout(target_branch)
        
        # Update target branch
        print(f"Pulling latest changes from {target_branch}")
        repo.git.pull('origin', target_branch)
        
        # Perform merge
        print(f"Merging {source_branch} into {target_branch}")
        merge_result = repo.git.merge(source_branch)
        
        # Restore stashed changes if any
        if has_stashed:
            try:
                repo.git.stash('pop')
                print("Successfully restored stashed changes")
            except git.exc.GitCommandError as e:
                print(f"Stash conflicts detected: {e}")
                print("Changes preserved in stash. Please resolve manually")
                return False
                
        return True
    # Handle the exception if the merge fails
    except git.exc.GitCommandError as e:
        print(f"Error during checkout/merge: {e}")
        # Cleanup
        if repo.git.status('--porcelain'):
            repo.git.merge('--abort')
        return False    
    except git.exc.GitCommandError as e:
        print(f"Error during checkout/merge: {e}")
        # Cleanup
        if repo.git.status('--porcelain'):
            repo.git.merge('--abort')
        return False