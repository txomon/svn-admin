#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__ ="$09-mar-2011 15:17:25$"

from script import *
import os

listaporgrupo=parse_grupos()
listapordirectorio=parse_dirs(['/svn'],'/svn')
# @type listapordirectorio list
print("el usuario actual es "+os.geteuid().__str__())
listaporgrupo.sort()
listapordirectorio.sort()
grouptodir(listaporgrupo,listapordirectorio)
dirtogroup(listaporgrupo,listapordirectorio)
for a in listaporgrupo:
	print(a.gr_name)
for a in listapordirectorio:
	print(a)
