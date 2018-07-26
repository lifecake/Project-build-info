from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('projectdetail', __name__, url_prefix='/NLAndroid')


@bp.route('/projectdetail/<a>?<b>?<c>')
def index(a, b, c):
    print(a, b, c)
    # ufc-tv prod 8.0613
    db = get_db()
    # package
    # packageName
    # productFlavorName
    # packageVersionName
    projectdetails = db.execute('select package, packageName, productFlavorName, packageVersionName, libraryGroup, '
                                'libraryName, libraryVersion from PackageLibrary WHERE package = ? '
                                'and productFlavorName = ? and packageVersionName = ?', (a, b, c,)).fetchall()
    items = [dict(pname=row[1], pFlavor=row[2], pversion=row[3]) for row in projectdetails]
    names = []
    versions = []
    flavors = []
    for item in items:
        # print('item: ' + item)
        names.append(item['pname'])
        versions.append(item['pversion'])
        flavors.append(item['pFlavor'])
    # print(names, versions)
    name = names[0]
    version = versions[0]
    flavor = flavors[0]
    # print(projectdetails)
    return render_template('projects/projectdetail.html', name=name, flavor=flavor, version=version, projectdetails=projectdetails)
