from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/NLAndroid')


@bp.route('/projects/')
def index():
    db = get_db()
    projects = db.execute('select package, packageName , packageVersionCode, packageVersionName, packageTargetSdk, '
                          'packageMiniSdk, packageMappingUrl, deepLinkScheme, date '
                          'from Package order by id desc').fetchall()
    return render_template('projects/projects.html', projects=projects)
