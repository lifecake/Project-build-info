DROP TABLE IF EXISTS Package ;
DROP TABLE IF EXISTS PackageLibrary;


CREATE TABLE Package (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  package text NOT NULL,
  packageName TEXT NOT NULL,
  packageVersionCode INTEGER NOT NULL,
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
  packageVersionName TEXT,
  libraryGroup TEXT NOT NULL,
  libraryName TEXT NOT NULL,
  libraryVersion TEXT NOT NULL,
  FOREIGN KEY (package) REFERENCES Package (package)
);

