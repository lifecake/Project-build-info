import os
import json
from flask import Flask, flash, render_template
from flask import request
from projectinfo.db import get_db
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Neulion Projects Info'

    @app.route('/NLAndroid/', methods=['GET', 'POST'])
    def projects():
        if request.method == 'POST':
            a = request.data
            templist = json.loads(a)

            dict1 = templist[0]
            db = get_db()
            error = None
            if dict1['package'] is None:
                error = 'Missing package'
            elif dict1['packageName'] is None:
                error = 'Missing packageName'
            elif dict1['packageVersionCode'] is None:
                error = 'Missing packageVersionCode'
            elif dict1['libraryCoordinateList'] is None:
                error = 'Missing Library info'
            # if already exist just update.
            elif db.execute(
                    'SELECT package, packageVersionName FROM Package WHERE package = ? and packageVersionName = ?',
                    (dict1['package'], dict1['packageVersionName'])).fetchone() is not None:
                # print('Found')
                db.execute(
                    'UPDATE Package SET packageName = ?, packageVersionCode = ?, packageTargetSdk = ?, '
                    'packageMiniSdk = ?, packageMappingUrl = ?, deepLinkScheme = ? WHERE package = ? and '
                    'packageVersionName = ?', (dict1['packageName'], dict1['packageVersionCode'],
                                               dict1['packageTargetSdk'], dict1['packageMiniSdk'],
                                               dict1['packageMappingUrl'], dict1['deepLinkScheme'], dict1['package'],
                                               dict1['packageVersionName'])
                )
                db.commit()

                id = db.execute(
                    'select id from PackageLibrary WHERE package = ? and packageVersionName = ?',
                    (dict1['package'], dict1['packageVersionName']))
                pids = [dict(id=row[0]) for row in id.fetchall()]
                ids = []

                for item in pids:
                    ids.append(item['id'])

                # print(ids)

                i = 0
                for dict2 in dict1['libraryCoordinateList']:
                    db.execute(
                        'UPDATE PackageLibrary SET package = ?, packageName = ?, packageVersionName = ?, '
                        'libraryGroup = ?, libraryName = ?, libraryVersion = ? WHERE package = ? and '
                        'packageVersionName = ? and id = ?', (dict1['package'], dict1['packageName'],
                                                              dict1['packageVersionName'], dict2['group'],
                                                              dict2['name'], dict2['currentVersion'],
                                                              dict1['package'], dict1['packageVersionName'], ids[i])
                        )
                    db.commit()
                    i = i + 1

                # print('Update')
                error = 'Project Info Updated'
                # print(error)
            # insert new data
            if error is None:
                db.execute(
                    'INSERT INTO Package (package, packageName , packageVersionCode, packageVersionName, '
                    'packageTargetSdk, packageMiniSdk, packageMappingUrl, deepLinkScheme) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (dict1['package'], dict1['packageName'],
                                                        dict1['packageVersionCode'], dict1['packageVersionName'],
                                                        dict1['packageTargetSdk'], dict1['packageMiniSdk'],
                                                        dict1['packageMappingUrl'], dict1['deepLinkScheme'])
                )
                db.commit()
                for dict2 in dict1['libraryCoordinateList']:
                    # print(dict2['libraryName'], dict2['libraryVersion'])
                    db.execute(
                        'INSERT INTO PackageLibrary (package, packageName, packageVersionName, libraryGroup, '
                        'libraryName, libraryVersion) VALUES (?, ?, ?, ?, ?, ?)',
                        (dict1['package'], dict1['packageName'],dict1['packageVersionName'],
                         dict2['group'], dict2['name'], dict2['currentVersion'])
                    )
                db.commit()
            flash(error)
            return 'Project info stored'
        else:
            return '<h1>只接受post请求！</h1>'

    from projectinfo import db
    db.init_app(app)

    from projectinfo import projects, projectdetail, upload
    app.register_blueprint(projects.bp)
    app.register_blueprint(projectdetail.bp)
    app.register_blueprint(upload.bp)

    return app
