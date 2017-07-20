#!/usr/bin/env python

import subprocess
import os
import smtplib
import tarfile
from email.mime.text import MIMEText

def noDelRsync(src,dest,port,log):
	'use Unix shell to run rsync'
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no -p' + str(port) +  '" --log-file=' + log + ' ' + src + ' ' + dest
	subprocess.call(rsync, shell=True)

def rsync(src,dest,port,log):
	'use Unix shell to run rsync'
	rsync = 'rsync -avze "ssh -o StrictHostKeyChecking=no -p' + str(port) +  '"  --delete --log-file=' + log + ' ' + src + ' ' + dest
	subprocess.call(rsync, shell=True)

def checkLog(log,errFile):
	'print errors into the error log'
	if os.path.exists(log):
		with open(log,'r') as Log:
			open(errFile,'w').close()
			with open(errFile,'a') as Err:
				for line in Log:
					if 'err' in line:
						Err.write(line)
					if 'Err' in line:
						Err.write(line)
					if 'ERR' in line:
						Err.write(line)
					if 'fail' in line:
						Err.write(line)

def sendMail(From,to,summary,log):
	with open(log, 'r') as content:
		msg = MIMEText(content.read())
		msg['Subject'] = summary
		msg['From'] = From
		msg['To'] = to

		s = smtplib.SMTP('localhost')
		s.sendmail(From, [to], msg.as_string())
		s.quit()

def tarGz(Dir,gz):
	tar = tarfile.open(gz,'w:gz')
	tar.add(Dir)
	tar.close()
