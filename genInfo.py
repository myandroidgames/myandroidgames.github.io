#! /usr/bin/env python
import zipfile
import json
import subprocess
from sys import argv
from os.path import splitext,isfile,getsize


SERVER_FILE_BASE_PATH = 'https://github.com/myandroidgames/myandroidgames.github.io/tree'

ICON_PATH_IN_APK='res/drawable/icon.png'

ICON_SUFFIX='.icon.png'
JSON_SUFFIX='.json'
VERSION_NAME_PREFIX='versionName='

JSON_KEY_NAME='name'
JSON_KEY_SIZE='size'
JSON_KEY_ICON='iconlink'
JSON_KEY_LINK='downloadlink'
JSON_KEY_VERSION='version'

'''
name,
size,
downloadlink,
iconlink,
version,
'''

def genIcon(apkin,iconOut):
    zf=zipfile.ZipFile(apkin)
    iconOut=iconOut+ICON_SUFFIX
    try:
        data = zf.read(ICON_PATH_IN_APK)
    except KeyError:
        print 'ERROR: not found %s in zip' % filename 
    target = open(iconOut,'w')
    target.write(data)
    target.close()

def getNameAndVersion(apkPath):
    p = subprocess.Popen(['./aaptdump.sh',apkPath],stdout=subprocess.PIPE)
    output = p.communicate()
    strr =  output[0].split('\n')
    #parse version
    #version out put will be : package: name='com.king.candycrushsaga' versionCode='1054002' versionName='1.54.0.2' platformBuildVersionName='4.0.2-238991'
    version = strr[0]
    #genJson(apkPath)
    #remove package: prefix
    version = version.split(':')[1]
    versionName = version.split()[2]
    versionName = versionName[len(VERSION_NAME_PREFIX)+1:-1]
    #parse name
    #package name format: application-label:'Candy Crush Saga'
    name = strr[1]
    name = name.split(':')[1]
    #remove start and end '
    name = name[1:len(name)-1]
    #print versionName,"|",name
    return [name,versionName]
def genJson(apkin):
    data = {}
    path,ext=splitext(apkin)
    name,version =  getNameAndVersion(apkin)
    #print name,version
    data[JSON_KEY_NAME] =  name
    data[JSON_KEY_VERSION] = version
    data[JSON_KEY_SIZE] =  getsize(apkin)
    data[JSON_KEY_ICON] =  path + ICON_SUFFIX
    data[JSON_KEY_LINK] =  apkin

    outfile=open(path+JSON_SUFFIX,'w')
    json.dump(data,outfile,indent=4)


helpmsg ='genInfo.py apkpath'

if len(argv) != 2 :
    print helpmsg
    exit()
else:
    #print argv
    pass

apkPath=argv[1]


#dirPath, apkName = split(apkPath)

#apkName = apkName[:-len('.apk')]

#print apkName,'|',dirPath

path,ext=splitext(apkPath)
#print 'path:',path,"|",ext
if isfile(path+ICON_SUFFIX):
    print path+ICON_SUFFIX,'already exist!'
else:
    genIcon(apkPath,path)
    print path + ICON_SUFFIX, " created!"

if isfile(path + JSON_SUFFIX):
    print path + JSON_SUFFIX, 'already exist!'
else:
    genJson(apkPath)
    print path + JSON_SUFFIX, ' created!'



