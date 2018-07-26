from flask import Flask, Blueprint, render_template
from projectinfo.db import get_db

bp = Blueprint('projectlist', __name__, url_prefix='/NLAndroid')


@bp.route('/projectlist/')
def index():
    db = get_db()
    projectlist = db.execute('select distinct package, packageName from Package order by id desc').fetchall()
    return render_template('projects/projectlist.html', projectlist=projectlist)
