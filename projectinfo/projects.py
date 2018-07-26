from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/NLAndroid')


@bp.route('/projects/<f>')
def index(f):
    db = get_db()
    projects = db.execute('select moduleName, package, productFlavorName, packageVersionCode, packageVersionName, '
                          'packageTargetSdk, packageMiniSdk, packageMappingUrl, deepLinkScheme, gitSHACode, gitBranchName, date '
                          'from Package where packageName = ? order by id desc', (f,)).fetchall()
    return render_template('projects/projects.html', projectname=f, projects=projects)
