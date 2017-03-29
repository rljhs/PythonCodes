#!/usr/bin/env python

from time import strftime

LOG = "/data/dev_svn_backup/logs/" + strftime("%Y%m%d-%H%M") + ".log"
SRC = "backup_robot@util2.21vtech.com:/var/ssvn"
DEST = "/data/dev_svn_backup/"
ERR_FILE = "/root/error.msg"

from remote_sync import bash_rsync
bash_rsync(LOG,SRC,DEST)
from remote_sync import check_log
check_log(LOG,ERR_FILE)

SUBJECT = 'SVN REPO BACKUP ' + strftime("%x,%X")
MSG = LOG
FROM = 'xps@21vtech.com'
TO = open('/root/john.mail.list',"r").read()

from send_email import send_email
send_email(FROM,TO,SUBJECT,MSG)
