#! /usr/bin/env python
import zipfile
from sys import argv

helpmsg='getIcon.py apk_path out_path'

if len(argv) != 3:
    print helpmsg
    exit()
else:
    print argv

apkPath=argv[1]
outPath=argv[2]

zf=zipfile.ZipFile(apkPath)
iconOut=outPath + '/icon.png'
ICON_PATH_IN_APK='res/drawable/icon.png'
try:
    data=zf.read(ICON_PATH_IN_APK)
except KeyError:
    print 'ERR: did not find %s in zip file' % filename
    exit()

target=open(iconOut,'w')
target.write(data)
target.close()

