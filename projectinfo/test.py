import json
#
# {
#   "applicationId":"com.neulion.f",
#   "applicationName":"f",
#   "applicationVersion":"8.0602",
#   "librarys": [
#     {
#         "libraryName":"track-core",
#         "libraryVersion":"6"
#     },{
#         "libraryName":"track-ga",
#         "libraryVersion":"6"
#     },{
#         "libraryName":"player",
#         "libraryVersion":"5.0.0"
#     }
#   ]
# }
tempdata = [{"package":"com.neulion.firetv.ufc.android.amazon.dev","packageName":"ufc-tv","productFlavorName":"amazon","packageVersionCode":"103","packageVersionName":"8.0613","packageTargetSdk":"27","packageMiniSdk":"21","deepLinkScheme":"amazon_ufctv","packageMappingUrl":"","libraryCoordinateList":[{"group":"com.android.tools.lint","name":"lint-gradle","currentVersion":"26.1.2"},{"group":"org.jetbrains.kotlin","name":"kotlin-annotation-processing-gradle","currentVersion":"1.2.41"},{"group":"com.crashlytics.sdk.android","name":"crashlytics","currentVersion":"2.8.0"},{"group":"com.squareup.leakcanary","name":"leakcanary-android","currentVersion":"1.5.4"},{"group":"com.squareup.leakcanary","name":"leakcanary-android-no-op","currentVersion":"1.5.4"},{"group":"org.jetbrains.kotlin","name":"kotlin-stdlib-jdk8","currentVersion":"1.2.41"},{"group":"com.google.android.gms","name":"play-services-analytics","currentVersion":"11.8.0"},{"group":"com.android.databinding","name":"baseLibrary","currentVersion":"3.1.2"},{"group":"com.neulion.android.app","name":"core","currentVersion":"0.5.3-SNAPSHOT"},{"group":"com.neulion.android.iap","name":"iap-amazon","currentVersion":"2.1.0-SNAPSHOT"},{"group":"android.arch.lifecycle","name":"extensions","currentVersion":"1.1.1"},{"group":"com.android.support","name":"support-annotations","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"adapters","currentVersion":"3.1.2"},{"group":"com.android.support","name":"recyclerview-v7","currentVersion":"27.0.2"},{"group":"com.jakewharton","name":"butterknife-compiler","currentVersion":"8.8.1"},{"group":"com.neulion.android","name":"service-v5","currentVersion":"3.0.12"},{"group":"com.android.databinding","name":"library","currentVersion":"3.1.2"},{"group":"com.android.support","name":"appcompat-v7","currentVersion":"27.0.2"},{"group":"com.android.support","name":"leanback-v17","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"compiler","currentVersion":"3.1.2"},{"group":"com.jakewharton","name":"butterknife","currentVersion":"8.8.1"},{"group":"com.neulion.android.media","name":"NeuPlayer","currentVersion":"4.7.2-SNAPSHOT"},{"group":"com.android.support","name":"design","currentVersion":"27.0.2"},{"group":"com.android.support","name":"multidex-instrumentation","currentVersion":"1.0.2"},{"group":"com.android.support","name":"cardview-v7","currentVersion":"27.0.2"},{"group":"com.neulion.android.iap","name":"iap-google","currentVersion":"2.1.0-SNAPSHOT"},{"group":"com.neulion.android.tracking","name":"tracker-ga","currentVersion":"4.3.2"},{"group":"com.neulion.android","name":"uikit-fresco","currentVersion":"1.1.12-SNAPSHOT"},{"group":"com.neulion.android","name":"appengine","currentVersion":"2.4.0"},{"group":"com.android.support","name":"multidex","currentVersion":"1.0.2"},{"group":"com.android.support","name":"support-v4","currentVersion":"27.0.2"},{"group":"com.android.support.constraint","name":"constraint-layout","currentVersion":"1.1.0"},{"group":"uk.co.chrisjenx","name":"calligraphy","currentVersion":"2.3.0"},{"group":"com.neulion.android","name":"commonparser","currentVersion":"3.0.4"}]},{"package":"com.neulion.firetv.ufc.android.amazon.dev","packageName":"ufc-tv","productFlavorName":"google","packageVersionCode":"103","packageVersionName":"8.0613","packageTargetSdk":"27","packageMiniSdk":"21","deepLinkScheme":"google_ufctv","packageMappingUrl":"","libraryCoordinateList":[{"group":"com.android.tools.lint","name":"lint-gradle","currentVersion":"26.1.2"},{"group":"org.jetbrains.kotlin","name":"kotlin-annotation-processing-gradle","currentVersion":"1.2.41"},{"group":"com.crashlytics.sdk.android","name":"crashlytics","currentVersion":"2.8.0"},{"group":"com.squareup.leakcanary","name":"leakcanary-android","currentVersion":"1.5.4"},{"group":"com.squareup.leakcanary","name":"leakcanary-android-no-op","currentVersion":"1.5.4"},{"group":"org.jetbrains.kotlin","name":"kotlin-stdlib-jdk8","currentVersion":"1.2.41"},{"group":"com.google.android.gms","name":"play-services-analytics","currentVersion":"11.8.0"},{"group":"com.android.databinding","name":"baseLibrary","currentVersion":"3.1.2"},{"group":"com.neulion.android.app","name":"core","currentVersion":"0.5.3-SNAPSHOT"},{"group":"com.neulion.android.iap","name":"iap-amazon","currentVersion":"2.1.0-SNAPSHOT"},{"group":"android.arch.lifecycle","name":"extensions","currentVersion":"1.1.1"},{"group":"com.android.support","name":"support-annotations","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"adapters","currentVersion":"3.1.2"},{"group":"com.android.support","name":"recyclerview-v7","currentVersion":"27.0.2"},{"group":"com.jakewharton","name":"butterknife-compiler","currentVersion":"8.8.1"},{"group":"com.neulion.android","name":"service-v5","currentVersion":"3.0.12"},{"group":"com.android.databinding","name":"library","currentVersion":"3.1.2"},{"group":"com.android.support","name":"appcompat-v7","currentVersion":"27.0.2"},{"group":"com.android.support","name":"leanback-v17","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"compiler","currentVersion":"3.1.2"},{"group":"com.jakewharton","name":"butterknife","currentVersion":"8.8.1"},{"group":"com.neulion.android.media","name":"NeuPlayer","currentVersion":"4.7.2-SNAPSHOT"},{"group":"com.android.support","name":"design","currentVersion":"27.0.2"},{"group":"com.android.support","name":"multidex-instrumentation","currentVersion":"1.0.2"},{"group":"com.android.support","name":"cardview-v7","currentVersion":"27.0.2"},{"group":"com.neulion.android.iap","name":"iap-google","currentVersion":"2.1.0-SNAPSHOT"},{"group":"com.neulion.android.tracking","name":"tracker-ga","currentVersion":"4.3.2"},{"group":"com.neulion.android","name":"uikit-fresco","currentVersion":"1.1.12-SNAPSHOT"},{"group":"com.neulion.android","name":"appengine","currentVersion":"2.4.0"},{"group":"com.android.support","name":"multidex","currentVersion":"1.0.2"},{"group":"com.android.support","name":"support-v4","currentVersion":"27.0.2"},{"group":"com.android.support.constraint","name":"constraint-layout","currentVersion":"1.1.0"},{"group":"uk.co.chrisjenx","name":"calligraphy","currentVersion":"2.3.0"},{"group":"com.neulion.android","name":"commonparser","currentVersion":"3.0.4"}]},{"package":"com.neulion.firetv.ufc.android.amazon.dev","packageName":"ufc-tv","productFlavorName":"prod","packageVersionCode":"103","packageVersionName":"8.0613","packageTargetSdk":"27","packageMiniSdk":"21","deepLinkScheme":"prod_ufctv","packageMappingUrl":"","libraryCoordinateList":[{"group":"com.android.tools.lint","name":"lint-gradle","currentVersion":"26.1.2"},{"group":"org.jetbrains.kotlin","name":"kotlin-annotation-processing-gradle","currentVersion":"1.2.41"},{"group":"com.crashlytics.sdk.android","name":"crashlytics","currentVersion":"2.8.0"},{"group":"com.squareup.leakcanary","name":"leakcanary-android","currentVersion":"1.5.4"},{"group":"com.squareup.leakcanary","name":"leakcanary-android-no-op","currentVersion":"1.5.4"},{"group":"org.jetbrains.kotlin","name":"kotlin-stdlib-jdk8","currentVersion":"1.2.41"},{"group":"com.google.android.gms","name":"play-services-analytics","currentVersion":"11.8.0"},{"group":"com.android.databinding","name":"baseLibrary","currentVersion":"3.1.2"},{"group":"com.neulion.android.app","name":"core","currentVersion":"0.5.3-SNAPSHOT"},{"group":"com.neulion.android.iap","name":"iap-amazon","currentVersion":"2.1.0-SNAPSHOT"},{"group":"android.arch.lifecycle","name":"extensions","currentVersion":"1.1.1"},{"group":"com.android.support","name":"support-annotations","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"adapters","currentVersion":"3.1.2"},{"group":"com.android.support","name":"recyclerview-v7","currentVersion":"27.0.2"},{"group":"com.jakewharton","name":"butterknife-compiler","currentVersion":"8.8.1"},{"group":"com.neulion.android","name":"service-v5","currentVersion":"3.0.12"},{"group":"com.android.databinding","name":"library","currentVersion":"3.1.2"},{"group":"com.android.support","name":"appcompat-v7","currentVersion":"27.0.2"},{"group":"com.android.support","name":"leanback-v17","currentVersion":"27.0.2"},{"group":"com.android.databinding","name":"compiler","currentVersion":"3.1.2"},{"group":"com.jakewharton","name":"butterknife","currentVersion":"8.8.1"},{"group":"com.neulion.android.media","name":"NeuPlayer","currentVersion":"4.7.2-SNAPSHOT"},{"group":"com.android.support","name":"design","currentVersion":"27.0.2"},{"group":"com.android.support","name":"multidex-instrumentation","currentVersion":"1.0.2"},{"group":"com.android.support","name":"cardview-v7","currentVersion":"27.0.2"},{"group":"com.neulion.android.iap","name":"iap-google","currentVersion":"2.1.0-SNAPSHOT"},{"group":"com.neulion.android.tracking","name":"tracker-ga","currentVersion":"4.3.2"},{"group":"com.neulion.android","name":"uikit-fresco","currentVersion":"1.1.12-SNAPSHOT"},{"group":"com.neulion.android","name":"appengine","currentVersion":"2.4.0"},{"group":"com.android.support","name":"multidex","currentVersion":"1.0.2"},{"group":"com.android.support","name":"support-v4","currentVersion":"27.0.2"},{"group":"com.android.support.constraint","name":"constraint-layout","currentVersion":"1.1.0"},{"group":"uk.co.chrisjenx","name":"calligraphy","currentVersion":"2.3.0"},{"group":"com.neulion.android","name":"commonparser","currentVersion":"3.0.4"}]}]

print(type(tempdata))
print(len(tempdata))
for data in tempdata:
  print(data)
  print(type(data))

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
        'SELECT package, packageVersionName, productFlavorName FROM Package WHERE package = ? and '
        'packageVersionName = ? and productFlavorName = ?',
        (dict1['package'], dict1['packageVersionName'], dict1['productFlavorName'])).fetchone() is not None:
  # print('Found')
  db.execute(
    'UPDATE Package SET packageName = ?, packageVersionCode = ?,productFlavorName = ?, packageTargetSdk = ?, '
    'packageMiniSdk = ?, packageMappingUrl = ?, deepLinkScheme = ? WHERE package = ? and '
    'packageVersionName = ?', (dict1['packageName'], dict1['packageVersionCode'], dict1['productFlavorName'],
                               dict1['packageTargetSdk'], dict1['packageMiniSdk'],
                               dict1['packageMappingUrl'], dict1['deepLinkScheme'], dict1['package'],
                               dict1['packageVersionName'])
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
      'packageVersionName = ? and id = ?', (dict1['package'], dict1['packageName'], dict1['productFlavorName'],
                                            dict1['packageVersionName'], dict2['group'],
                                            dict2['name'], dict2['currentVersion'],
                                            dict1['package'], dict1['packageVersionName'],
                                            ids[i])
    )
    db.commit()
    i = i + 1

  # print('Update')
  error = 'Project Info Updated'
  # print(error)
# insert new data

