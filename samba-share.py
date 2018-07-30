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

	def __init__(self, arg):

		self.arg = arg
		
	def getLoginUserName(self):
		"""
		-[o] 注意 `$ ***.py` 和使用 `$ sudo ***,py` 启动的冲突！
		"""
		self.__curUser = os.system("whoami")

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

	pass

#end main

if __name__=="__main__":
	main()

#fi.
