from flask import Flask, Blueprint, render_template, request,redirect, url_for
from werkzeug.utils import secure_filename
import os

bp = Blueprint('upload', __name__, url_prefix='/NLAndroid')


@bp.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No such file'
        else:
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            upload_path = os.path.join(basepath, 'static/uploads', secure_filename(f.filename))
            f.save(upload_path)
            print(f.filename)
        # return redirect(url_for('upload'))
            return 'Filed uploaded'
    return 'No file'
