from flask import Flask, jsonify, request

from GitHubHelper import GitHubHelper

app = Flask(__name__)
ghh = GitHubHelper()
@app.route('/api/push', methods=['POST'])
def pushChanges(pushRequest):
    isSuccessful = False
    try:
        ghh.submitChangesAutomatted(pushRequest.repo_remote_url, branch_name=pushRequest.branch_name, target_merge_branch=request.target_merge_branch, file_name=pushRequest.file_name, file_content=pushRequest.file_content, commit_message=pushRequest.commit_message)
        isSuccessful = True
    except:
        isSuccessful = False
    return isSuccessful
if __name__ == '__main__':
    app.run(debug=True, port=8009)