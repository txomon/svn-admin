#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__ ="$09-mar-2011 15:17:25$"

from script import *

listaporgrupo=parse_grupos()
if listaporgrupo == -1:
    exit(-1)

listapordirectorio=parse_dirs(['/svn'],'/svn')
# @type listapordirectorio list
listapordirectorio.sort()
listaporgrupo=dirtogroup(listapordirectorio)
grouptodir(listaporgrupo,listapordirectorio)
for a in listaporgrupo:
	print(a.gr_name)
for a in listapordirectorio:
	print(a)
