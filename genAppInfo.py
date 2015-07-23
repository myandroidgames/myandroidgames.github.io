#! /usr/bin/env python
import zipfile
import json
import subprocess
from sys import argv
import os
from os.path import splitext,isfile,getsize,exists


SERVER_FILE_BASE_PATH = 'https://github.com/myandroidgames/myandroidgames.github.io/tree'

ICON_PATH_IN_APK='res/drawable/icon.png'

STR_CREATED = " created!"
STR_EXIST = " already exist!"
ICON_SUFFIX='.icon.png'
JSON_SUFFIX='.json'
APK_SUFFIX = '.apk'
VERSION_NAME_PREFIX='versionName='
PACKAGE_NAME_PREFIX='name='

JSON_KEY_NAME='name'
JSON_KEY_PACKAGE='packagename'
JSON_KEY_SIZE='size'
JSON_KEY_ICON='iconlink'
JSON_KEY_LINK='downloadlink'
JSON_KEY_VERSION='version'

APP_READY_PATH='apps/ready'

'''
name,
size,
downloadlink,
iconlink,
version,
'''

def genIcon(apkin,appOutPath,packageName):
    zf=zipfile.ZipFile(apkin)
    iconOut = appOutPath+ '/' + packageName + ICON_SUFFIX
    if isfile(iconOut):
        print iconOut + STR_EXIST
        return
    try:
        data = zf.read(ICON_PATH_IN_APK)
    except KeyError:
        print 'ERROR: not found %s in zip' % filename 
    target = open(iconOut,'w')
    target.write(data)
    target.close()
    print iconOut + STR_CREATED

def getNameAndVersion(apkPath):
    p = subprocess.Popen(['./aaptdump.sh',apkPath],stdout=subprocess.PIPE)
    output = p.communicate()
    strr =  output[0].split('\n')
    #parse version
    #version out put will be : package: name='com.king.candycrushsaga' versionCode='1054002' versionName='1.54.0.2' platformBuildVersionName='4.0.2-238991'
    version = strr[0]
    #print version
    #genJson(apkPath)
    #remove package: prefix
    version = version.split(':')[1]
    version = version.split()
    packageName = version[0]
    versionName = version[2]
    versionName = versionName[len(VERSION_NAME_PREFIX)+1:-1]
    packageName = packageName[len(PACKAGE_NAME_PREFIX)+1:-1]
    #parse name
    #package name format: application-label:'Candy Crush Saga'
    name = strr[1]
    name = name.split(':')[1]
    #remove start and end '
    name = name[1:len(name)-1]
    print versionName,"|",name,"|",packageName
    return [name,versionName,packageName]
def genJson(apkin, appOutPath, packageName, version, name):
    apkOut = appOutPath + '/' + packageName + APK_SUFFIX
    os.rename(apkin,apkOut)
    jsonPath = appOutPath + '/' + packageName + JSON_SUFFIX
    if isfile(jsonPath):
        print jsonPath + STR_EXIST
        return
    data = {}
    #print name,version
    data[JSON_KEY_NAME] =  name
    data[JSON_KEY_VERSION] = version
    data[JSON_KEY_SIZE] =  getsize(apkOut)
    data[JSON_KEY_ICON] =  appOutPath + '/' + packageName + ICON_SUFFIX
    data[JSON_KEY_LINK] =  apkOut
    data[JSON_KEY_PACKAGE] = packageName
    outfile=open(jsonPath,'w')
    json.dump(data,outfile,indent=4)
    print jsonPath + STR_CREATED
def createDirs(path):
    if not exists(path):    
        os.makedirs(path)
        print path + STR_CREATED
    else:
        print path + STR_EXIST

def main(argv):
    helpmsg ='genInfo.py apkpath'
    if len(argv) != 2 :
        print helpmsg
        exit()
    else:
        #print argv
        pass

    apkPath = argv[1]
    outPath = APP_READY_PATH

    #dirPath, apkName = split(apkPath)

    #apkName = apkName[:-len('.apk')]

    #print apkName,'|',dirPath
    if not isfile(apkPath):
        print apkPath + ' not exist!'
        return -1
    path,ext=splitext(apkPath)
    name,version,packageName = getNameAndVersion(apkPath)
    appOutPath = outPath + '/' + packageName + '/' + version
    createDirs(appOutPath)
    genIcon(apkPath,appOutPath,packageName)
    genJson(apkPath,appOutPath,packageName,version,name)

if __name__ == '__main__':
    main(argv)




