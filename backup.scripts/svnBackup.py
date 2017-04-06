#!/usr/bin/env python

from fullBackupLib import bashRsync,checkLog,sendMail
from time import strftime
import os
import yaml

with open('svnConf.yaml','r') as yamlFile:
	conf = yaml.load(yamlFile)
	address = conf['address']
	dest = address['dest']
        destDir = dest + strftime("%Y%m%d-%H%M") + '/'
        log = dest + 'logs/' + strftime("%Y%m%d-%H%M") + '.rsync.log'
	mail = conf['mail']

bashRsync(address['src'],destDir,'22',log)

checkLog(log,conf['err'])
	
sendMail(mail['from'],mail['receiver'],mail['summary'],log)