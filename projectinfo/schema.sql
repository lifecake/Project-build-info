--DROP TABLE IF EXISTS Package ;
--DROP TABLE IF EXISTS PackageLibrary;
--DROP TABLE IF EXISTS iOSProject ;
--DROP TABLE IF EXISTS Framework;


CREATE TABLE Package (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  package text NOT NULL,
  packageName TEXT NOT NULL,
  packageVersionCode INTEGER NOT NULL,
  productFlavorName TEXT,
  packageVersionName TEXT,
  packageTargetSdk TEXT,
  packageMiniSdk TEXT,
  packageMappingUrl TEXT,
  deepLinkScheme TEXT,
  date TIMESTAMP DEFAULT (datetime('now', 'localtime'))
);
CREATE TABLE PackageLibrary (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  package TEXT NOT NULL,
  packageName TEXT NOT NULL,
  productFlavorName TEXT,
  packageVersionName TEXT,
  libraryGroup TEXT NOT NULL,
  libraryName TEXT NOT NULL,
  libraryVersion TEXT NOT NULL,
  FOREIGN KEY (package) REFERENCES Package (package)
);

CREATE TABLE iOSProject (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  projectName TEXT NOT NULL,
  projectVersion TEXT NOT NULL,
  date TIMESTAMP DEFAULT (datetime('now', 'localtime'))
);

CREATE TABLE Framework (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  projectName TEXT NOT NULL,
  projectVersion TEXT NOT NULL,
  frameworkName TEXT NOT NULL,
  frameworkVersion TEXT NOT NULL
);

