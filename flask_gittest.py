from git import Repo
from flask import render_template, current_app
import datetime
from flask import Blueprint

gittest = Blueprint('git', __name__,
                        template_folder='templates')

@gittest.route("/git", methods=['GET'])
def git():
    GIT_PATH = current_app.config.get('GIT_PATH', '.')
    repo = Repo.init(GIT_PATH)

    current_branch = str(repo.head.ref)

    latest_commits = [(c.hexsha[:6], c.message, str(c.author), str(datetime.datetime.fromtimestamp(c.committed_date))) for c in repo.iter_commits('master', max_count=10)]

    is_dirty = repo.is_dirty()

    context_dict = {
        'current_branch': current_branch,
        'is_dirty': is_dirty,
        'latest_commits': latest_commits
    }

    return render_template('git.html', 
                       **context_dict)

