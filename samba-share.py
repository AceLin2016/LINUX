#!/usr/bin/env python3

"""
# Author : Joseph Lin
# E-main : joseph.lin@aliyun.com
# 
###
###
### 
"""


###
### import packages
###
import os, sys, io

import jinja2
from jinja2 import Template


###
### functions define
###
def checkSambaHadInstalled():
	pass

def checkSharNameHadExist():
	pass

def checkShareDirectoryHadExist():
	pass


def checkUserNameHadAdded():
	pass


def smbAddUser( username ):
	os.system("smbpasswd -a {}".format( username ))


def smbRestart ():
	os.system( "/etc/init.d/smbd restart" )
	os.system( "/etc/init.d/nmbd restart" )


class ConfigInfo(object):
	"""docstring for ConfigInfo"""
	__curUser = None
	__smbUsername = None
	__smbDir = None
	__smbComment = None
	__smbShareName = None

	def __init__(self):
		# self.arg = arg
		pass
		
	def getLoginUserName(self):
		"""
		-[o] 注意 `$ ***.py` 和使用 `$ sudo ***,py` 启动的冲突！
		"""
		self.__curUser = os.system("whoami")

	def getUsername(self):
		return self.__smbUsername
	def getDirectory(self):
		return self.__smbDir
	def getComment(self):
		return self.__smbComment
	def getShareName(self):
		return self.__smbShareName

	def setShareName(self, shareName):
		self.__smbShareName = shareName

	def setComment(self, comment):
		self.__smbComment = comment

	def setDirectory(self, _dir):
		self.__smbDir = _dir

	def setUsername(self, username):
		self.__smbUsername = username



###
### global varibales
###
doDebug = True

sharFormat = "\
[{{ v_dispName }}]\n\
    comment = {{ v_comment }}\n\
    path = {{ v_shareDir}}\n\
    writable = yes\n\
    read only = no\n\
    browseable = yes\n\
    username = {{ v_username }}\n\
    "

###
### running logical
###
def main():
	global doDebug

	if doDebug:
		print( "sharFormat = \n%s"%sharFormat )

	"""
	v0.0.1: $ ./samba-share.py  ~    JosephLin   josephlin
	          [program name]  [dir] [share name] [username]
	"""
	argc = len(sys.argv)
	if argc != 4:
		print( "usage: %s <directory you want to share by smaba> <share Name> <login username>" )
		sys.exit(1) ## Command error.

	smbConfInfo = ConfigInfo()
	smbConfInfo.setShareName(sys.argv[2])
	smbConfInfo.setComment("N/A")
	smbConfInfo.setDirectory(sys.argv[1])
	smbConfInfo.setUsername(sys.argv[3])

	smbConfigTpl = Template(sharFormat)
	smbConfigStr = smbConfigTpl.render( 
							v_dispName = smbConfInfo.getShareName(),
							v_comment = smbConfInfo.getComment(), 
							v_shareDir = smbConfInfo.getDirectory(),
							v_username = smbConfInfo.getUsername() ) 
	if doDebug:
		print (smbConfigStr)


	pass

#end main

if __name__=="__main__":
	main()

#fi.
