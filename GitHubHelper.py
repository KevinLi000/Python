import os
import git
class GitHubHelper:
    def __init__(self):
        pass
    def submitChangesAutomatted(repo_remote_url, repo_path_name, branch_name, target_merge_branch = 'main', file_name='', file_content='',commit_message=''):
        current_branch = branch_name
        repo_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), repo_path_name)
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
            repo = git.Repo.clone_from(repo_remote_url, repo_path)
        else:
            repo = git.Repo(repo_path)
        # Get the base merge
        merge_base = repo.merge_base(branch_name, target_merge_branch)
        # Get the latest branch
        current_commit = repo.commit(branch_name)
        target_commit = repo.commit(target_merge_branch)
        canMerge = False
        if merge_base and merge_base[0] != current_commit:
            print(f"{current_branch} has unmerged changes to {target_merge_branch}")
            canMerge = True
        else:
            print(f"{current_branch} already merged {target_merge_branch}")

        if canMerge :
            # Get the active branch
            current_branch = repo.active_branch
            print(f"Current branch: {current_branch}")
            # Switch to main branch
            main_branch = target_merge_branch
            repo.git.checkout(main_branch)
            # Pull latest changes from remote main
            repo.git.pull("origin", main_branch)
            # Merge the current branch into main
            repo.git.merge(current_branch)
            # Push merged changes to remote
            repo.git.push("origin", main_branch)
            print(f"Successfully merged {current_branch} into {main_branch} and pushed to remote.")
        else:
            file_name = file_name
            file_content = file_content

            # Create or modify a file
            file_path = os.path.join(repo_path, file_name)
            with open(file_path, 'w') as f:
                f.write(file_content)
            # Stage the file
            repo.git.add(file_name)
            # Commit changes
            repo.git.commit('-m', commit_message)
            print("Changes committed.")
            repo.git.push("origin", branch_name, set_upstream=True)
            print(f"Pushed branch '{branch_name}' to GitHub.")
            # Get the active branch
            current_branch = repo.active_branch
            print(f"Current branch: {current_branch}")
            # Switch to main branch
            main_branch = target_merge_branch
            repo.git.checkout(main_branch)
            # Pull latest changes from remote main
            repo.git.pull("origin", main_branch)
            # Merge the current branch into main
            repo.git.merge(current_branch)
            # Push merged changes to remote
            repo.git.push("origin", main_branch)
            print(f"Successfully merged {current_branch} into {main_branch} and pushed to remote.")