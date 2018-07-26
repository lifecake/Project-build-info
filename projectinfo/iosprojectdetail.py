from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('iosprojectdetail', __name__, url_prefix='/NLiOS')


@bp.route('/iosprojectdetail/<d>?<e>')
def index(d, e):
    db = get_db()
    iosprojectdetails = db.execute('select projectName, projectVersion, frameworkName, frameworkVersion from Framework '
                                   'WHERE projectName = ? and projectVersion = ?', (d, e,)).fetchall()
    items = [dict(pname=row[0], pversion=row[1]) for row in iosprojectdetails]
    names = []
    versions = []
    for item in items:
        names.append(item['pname'])
        versions.append(item['pversion'])
    # print(names, versions)
    name = names[0]
    version = versions[0]
    # print(projectdetails)
    return render_template('projects/iosprojectdetail.html', name=name, version=version, iosprojectdetails=iosprojectdetails)
