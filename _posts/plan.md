---
layout: post
title:  "Welcome to Android Games!"
date: Tue Jul 14 10:26:01 
published: false
categories: 
---

list plan of features!

##Feature most important
### display games as list, give downloads links. how to implement this?

Edit index info in server save as (json/yaml), pass to client, client parse it and show it.
Need define info areas (name,icon,source,link,summary)

Already have a json contains needed info.

### server structure:
- index file give the list(package_name,version,updated?,app-json)
- input should be an folder contains app, script will parse it and put it to right position,update icon/json,update index list.
- file structure:
-----apps
     |
--------queue[apks]
--------[packagename]:->[version]->[apk+icon+json]
--------index.json

### client app:
- construct list app
- using http request get json, parse info.
- download app icon. 
- download app/install.





