from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('iOSprojects', __name__, url_prefix='/NLiOS')


@bp.route('/iOSprojects/<g>')
def index(g):
    db = get_db()
    iosprojects = db.execute('select projectName, projectVersion, date from iOSProject where projectName = ? order by id desc', (g,)).fetchall()
    return render_template('projects/iosprojects.html', iosprojectname=g, iosprojects=iosprojects)
