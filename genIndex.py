#! /usr/bin/env python
import os
import json
JSON_KEY_PACKAGE_NAME = "packageName"
JSON_KEY_VERSION = 'version'
JSON_KEY_UPDATE = 'update'
JSON_KEY_APK_JSON = 'appJson'

APK_SUFFIX = '.apk'
ICON_SUFFIX = '.icon.png'
JSON_SUFFIX = '.json'

INDEX_JSON = 'index.json'
BASE_PATH = 'apps/ready'

INDEX_JSON_KEY = 'gamelist'
lst = os.listdir(BASE_PATH)
outFile = open(INDEX_JSON,'w')
index= []
arraymap={}
for item in lst:
    versions=os.listdir(BASE_PATH + '/' + item)
    versions.sort()
    print versions[-1]
    data = {}
    data[JSON_KEY_PACKAGE_NAME] = item
    data[JSON_KEY_VERSION] = versions[-1]
    data[JSON_KEY_APK_JSON] = BASE_PATH + '/' + item + '/' + versions[-1] + '/' + item + JSON_SUFFIX
    print data
    index.append(data) 
print index
arraymap[INDEX_JSON_KEY] = index
json.dump(arraymap,outFile,indent=4)



        
