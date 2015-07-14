#! /usr/bin/env python
import zipfile
import json
import subprocess
from sys import argv
from os.path import splitext,isfile,getsize


SERVER_FILE_BASE_PATH = 'https://github.com/myandroidgames/myandroidgames.github.io/tree'

ICON_PATH_IN_APK='res/drawable/icon.png'

ICON_SUFFIX='.icon.png'

JSON_KEY_NAME='name'
JSON_KEY_SIZE='size'
JSON_KEY_ICON='iconlink'
JSON_KEY_LINK='downloadlink'

'''
name,
size,
downloadlink,
iconlink,
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

def genJson(apkin):
    data = {}
    path,ext=splitext(apkin)
    data[JSON_KEY_NAME] =  'test-game'
    data[JSON_KEY_SIZE] =  getsize(apkin)
    data[JSON_KEY_ICON] =  path+ ICON_SUFFIX
    data[JSON_KEY_LINK] =  apkin

    outfile=open('testjson.json','w')
    json.dump(data,outfile,indent=4)


helpmsg ='genInfo.py apkpath'

if len(argv) != 2 :
    print helpmsg
    exit()
else:
    #print argv
    pass

apkPath=argv[1]


#genJson(apkPath)
p = subprocess.Popen(['./aaptdump.sh',apkPath],stdout=subprocess.PIPE)
output = p.communicate()
strr =  output[0].split('\n')
version = strr[0]
name = strr[1]
name = name.split(':')[1]
name = name[1:len(name)-1]
print version,"|",name


exit()

#dirPath, apkName = split(apkPath)

#apkName = apkName[:-len('.apk')]

#print apkName,'|',dirPath

path,ext=splitext(apkPath)
#print 'path:',path,"|",ext
if isfile(path+ICON_SUFFIX):
    print path+ICON_SUFFIX,'already exist!\n'
else:
    genIcon(apkPath,path)



