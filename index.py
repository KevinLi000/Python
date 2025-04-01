from flask import Flask, jsonify, render_template, request
from GitHubHelper import GitHubHelper

app = Flask(__name__)
ghh = GitHubHelper()
@app.route("/")
def home():
    data = {
        "id": 1,
        "title": 'test title',
        "completed": False
    }
    return render_template("index.html", todo=data)  # 渲染页面并传递数据

@app.route('/api/push', methods=['POST'])
def pushChanges():
    repoUrl = request.form.get('repoUrl')
    lbranchName = request.form.get('lbranchName')
    tbranchName = request.form.get('tbranchName')
    filename = request.form.get('filename')
    filecontent = request.form.get('filecontent')
    commitmsg = request.form.get('commitmsg')
    # result = f"repoUrl: {data}"
    GitHubHelper.submitChangesAutomatted(repo_remote_url=repoUrl, repo_path_name="testRepository", branch_name=lbranchName, target_merge_branch=tbranchName, file_name=filename, file_content=filecontent,commit_message=commitmsg)
    
    return jsonify({'result': True})
    # isSuccessful = False
    # try:
    #     ghh.submitChangesAutomatted(pushRequest.repo_remote_url, branch_name=pushRequest.branch_name, target_merge_branch=request.target_merge_branch, file_name=pushRequest.file_name, file_content=pushRequest.file_content, commit_message=pushRequest.commit_message)
    #     isSuccessful = True
    # except:
    #     isSuccessful = False
    # return isSuccessful
if __name__ == '__main__':
    app.run(debug=True, port=8009)