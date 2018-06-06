from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('projectdetail', __name__, url_prefix='/NLAndroid')


@bp.route('/projectdetail/<a>?<b>')
def index(a, b):
    # print(a, b)
    db = get_db()
    projectdetails = db.execute('select package, packageName, packageVersionName, libraryGroup, '
                                'libraryName, libraryVersion from PackageLibrary WHERE package = ? '
                                'and packageVersionName = ?', (a, b)).fetchall()
    items = [dict(pname=row[1], pversion=row[2]) for row in projectdetails]
    names = []
    versions = []
    for item in items:
        names.append(item['pname'])
        versions.append(item['pversion'])
    # print(names, versions)
    name = names[0]
    version = versions[0]
    # print(projectdetails)
    return render_template('projects/projectdetail.html', name=name, version=version, projectdetails=projectdetails)
