import os
import json
from flask import Flask, flash, render_template
from flask import request
from projectinfo.db import get_db
import datetime
from flask_bootstrap import Bootstrap
import re

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
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

    # index page
    @app.route('/')
    def hello():
        return render_template('projects/index.html')

    @app.route('/NLAndroid/', methods=['GET', 'POST'])
    def projects():
        if request.method == 'POST':
            a = request.data
            templist = json.loads(a)
            # dict1 = templist[0]
            db = get_db()
            for dict1 in templist:
                #print(dict1)
                if db.execute(
                        'SELECT package, packageVersionName, productFlavorName, moduleName FROM Package WHERE package = ? and packageVersionName = ? and productFlavorName = ? and moduleName = ?',
                        (dict1['package'], dict1['packageVersionName'], dict1['productFlavorName'], dict1['moduleName'])).fetchone() is not None:
                    # print('Found')
                    db.execute(
                        'UPDATE Package SET packageName = ?, packageVersionCode = ?,productFlavorName = ?, packageTargetSdk = ?, '
                        'packageMiniSdk = ?, packageMappingUrl = ?, deepLinkScheme = ?, gitSHACode = ?, gitBranchName = ? WHERE package = ? and packageVersionName = ? and productFlavorName = ? and moduleName = ?',
                        (dict1['packageName'], dict1['packageVersionCode'], dict1['productFlavorName'],
                         dict1['packageTargetSdk'], dict1['packageMiniSdk'],
                         dict1['packageMappingUrl'], dict1['deepLinkScheme'], dict1['gitSHACode'], dict1['gitBranchName'], dict1['package'],
                         dict1['packageVersionName'], dict1['productFlavorName'], dict1['moduleName'])
                    )
                    db.execute(
                        'UPDATE Package SET date = datetime(\'now\', \'localtime\') WHERE package = ? and '
                        'packageVersionName = ?', (dict1['package'], dict1['packageVersionName'])
                    )
                    db.commit()

                    id = db.execute(
                        'select id from PackageLibrary WHERE package = ? and packageVersionName = ? and productFlavorName = ?',
                        (dict1['package'], dict1['packageVersionName'], dict1['productFlavorName']))
                    pids = [dict(id=row[0]) for row in id.fetchall()]
                    ids = []

                    for item in pids:
                        ids.append(item['id'])

                    # print(ids)

                    i = 0
                    for dict2 in dict1['libraryCoordinateList']:
                        db.execute(
                            'UPDATE PackageLibrary SET package = ?, packageName = ?, productFlavorName = ?, packageVersionName = ?, '
                            'libraryGroup = ?, libraryName = ?, libraryVersion = ? WHERE package = ? and '
                            'packageVersionName = ? and id = ?',
                            (dict1['package'], dict1['packageName'], dict1['productFlavorName'],
                             dict1['packageVersionName'], dict2['group'],
                             dict2['name'], dict2['currentVersion'],
                             dict1['package'], dict1['packageVersionName'],
                             ids[i])
                        )
                        db.commit()
                        i = i + 1

                # insert new data
                else:
                    print(dict1)
                    db.execute(
                        'INSERT INTO Package (package, packageName , productFlavorName, packageVersionCode, packageVersionName, '
                        'packageTargetSdk, packageMiniSdk, packageMappingUrl, deepLinkScheme, gitSHACode, gitBranchName, moduleName) '
                        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (dict1['package'], dict1['packageName'], dict1['productFlavorName'],
                                                            dict1['packageVersionCode'], dict1['packageVersionName'],
                                                            dict1['packageTargetSdk'], dict1['packageMiniSdk'],
                                                            dict1['packageMappingUrl'], dict1['deepLinkScheme'], dict1['gitSHACode'], dict1['gitBranchName'], dict1['moduleName'])
                    )
                    db.commit()
                    for dict2 in dict1['libraryCoordinateList']:
                        # print(dict2['libraryName'], dict2['libraryVersion'])
                        db.execute(
                            'INSERT INTO PackageLibrary (package, packageName, productFlavorName, packageVersionName, libraryGroup, '
                            'libraryName, libraryVersion) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (dict1['package'], dict1['packageName'], dict1['productFlavorName'], dict1['packageVersionName'],
                             dict2['group'], dict2['name'], dict2['currentVersion'])
                        )
                        db.commit()
            return 'Project info stored'
        else:
            return '<h1>Only accept post request！</h1>'

    @app.route('/NLiOS/', methods=['GET', 'POST'])
    def iosprojects():
        if request.method == 'POST':
            a = request.data
            templist = json.loads(a)
            dict1 = templist[0]
            print(dict1['projectName'])
            db = get_db()
            # if already exist just update.
            if db.execute(
                    'SELECT projectName, projectVersion FROM iOSProject WHERE projectName = ? and projectVersion = ?',
                    (dict1['projectName'], dict1['projectVersion'])).fetchone() is not None:
                # print('Found')
                db.execute(
                    'UPDATE iOSProject SET projectName = ?, projectVersion = ? WHERE projectName = ? and '
                    'projectVersion = ?', (dict1['projectName'], dict1['projectVersion'],
                                           dict1['projectName'], dict1['projectVersion'])
                )
                db.commit()
                db.execute(
                    'UPDATE iOSProject SET date = datetime(\'now\', \'localtime\') WHERE projectName = ? and '
                    'projectVersion = ?', (dict1['projectName'], dict1['projectVersion'])
                )
                db.commit()

                iosid = db.execute(
                    'select id from Framework WHERE projectName = ? and projectVersion = ?',
                    (dict1['projectName'], dict1['projectVersion'])
                )
                pids = [dict(id=row[0]) for row in iosid.fetchall()]
                iosids = []

                for item in pids:
                    iosids.append(item['id'])

                # print(ids)

                i = 0
                for dict2 in dict1['frameworks']:
                    db.execute(
                        'UPDATE Framework SET projectName = ?, projectVersion = ?, frameworkName = ?, '
                        'frameworkVersion = ? WHERE projectName = ? and projectVersion = ? and id = ?',
                        (dict1['projectName'], dict1['projectVersion'], dict2['frameworkName'],
                         dict2['frameworkVersion'], dict1['projectName'], dict1['projectVersion'], iosids[i])
                        )
                    db.commit()
                    i = i + 1
                return 'Project info Updated'
            # insert new data
            else:
                db.execute(
                    'INSERT INTO iOSProject (projectName, projectVersion) VALUES (?, ?)',
                    (dict1['projectName'], dict1['projectVersion'])
                )
                db.commit()
                for dict2 in dict1['frameworks']:
                    # print(dict2['libraryName'], dict2['libraryVersion'])
                    db.execute(
                        'INSERT INTO Framework (projectName, projectVersion, frameworkName, frameworkVersion) '
                        'VALUES (?, ?, ?, ?)',
                        (dict1['projectName'], dict1['projectVersion'], dict2['frameworkName'],
                         dict2['frameworkVersion'])
                    )
                db.commit()
                return 'Project info stored'
        else:
            return '<h1>Only accept post request！</h1>'

    from projectinfo import db
    db.init_app(app)

    from projectinfo import projects, projectdetail, upload, iosprojects, iosprojectdetail, projectlist, iosprojectlist
    app.register_blueprint(projects.bp)
    app.register_blueprint(projectdetail.bp)
    app.register_blueprint(upload.bp)
    app.register_blueprint(iosprojects.bp)
    app.register_blueprint(iosprojectdetail.bp)
    app.register_blueprint(projectlist.bp)
    app.register_blueprint(iosprojectlist.bp)

    @app.template_filter('checkLibraryVersion')
    def checkLibraryVersion(libraryVersion):
        if re.match(r'\d+.\d+.0\d+', libraryVersion) or 'x' in str(libraryVersion):
            return True

    @app.template_filter('isUseSnapshot')
    def isUseSnapshot(pVName, pK):
        # print(pVName)
        # print(pK)
        db = get_db()
        lVersion = db.execute('select libraryVersion from PackageLibrary WHERE packageVersionName = ? and package = ?', 
        (pVName, pK)).fetchall()
        items = [dict(libraryVersion=row[0]) for row in lVersion]
        for item in items:
            print (item['libraryVersion'])
            if '-SNAPSHOT' in item['libraryVersion']:
                return True
        print('Not found')
        return False

    @app.template_filter('xframeWork')
    def xframeWork(iOSPV,iOSPN):
        # print(iOSPV)
        # print(iOSPN)
        db = get_db()
        iOSlVersion = db.execute('select frameworkVersion from Framework WHERE projectName = ? and projectVersion = ?', 
        (iOSPV, iOSPN)).fetchall()
        items = [dict(iOSFrameworkVersion=row[0]) for row in iOSlVersion]
        for item in items:
            print (item['iOSFrameworkVersion'])
            if re.match(r'\d+.\d+.0\d+', item['iOSFrameworkVersion']) or 'x' in str(item['iOSFrameworkVersion']):
                return True
        print('Not found')
        return False

    return app
