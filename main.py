#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__ ="$09-mar-2011 15:17:25$"

from script import *

listaporgrupo=parse_grupos()
listapordirectorio=parse_dirs([],'/svn')
# @type listapordirectorio list
listaporgrupo.sort()
listapordirectorio.sort()
for a in listaporgrupo:
	print(a.gr_name)
for a in listapordirectorio:
	print(a)
