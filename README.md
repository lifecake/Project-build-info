# Project-build-info
A website for displaying Build info using flask
Receive post request to get Build info we need and display.
Example:
[
  {
    "package": "com.android.test",
    "packageName": "test",
    "packageVersionCode": "100",
    "packageVersionName": "8.0607",
    "packageTargetSdk": "27",
    "packageMiniSdk": "20",
    "packageMappingUrl": "test",
    "deepLinkScheme": "test",
    "libraryCoordinateList": [
      {
        "group": "com.android.tools.lint",
        "name": "lint-gradle",
        "currentVersion": "26.1.1"
      },
      {
        "group": "com.jakewharton",
        "name": "butterknife-compiler",
        "currentVersion": "8.8.1"
      },
      {
        "group": "com.android.support",
        "name": "appcompat-v7",
        "currentVersion": "26.1.0"
      },
      {
        "group": "com.google.code.gson",
        "name": "gson",
        "currentVersion": "2.8.2"
      }
      }
    ]
  }
]
