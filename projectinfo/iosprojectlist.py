from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('iosprojectlist', __name__, url_prefix='/NLiOS')


@bp.route('/iosprojectlist/')
def index():
    db = get_db()
    iosprojectlist = db.execute('select distinct projectName from iOSProject order by id desc').fetchall()
    return render_template('projects/iosprojectlist.html', iosprojectlist=iosprojectlist)
