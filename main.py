#! /usr/bin/python3.1

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__ ="$09-mar-2011 15:17:25$"

from functions import *
from time import sleep

fuera=0
basedir='/svn'

listaporgrupo=parse_grupos()
if listaporgrupo == -1:
    exit(-1)
listapordirectorio=parse_dirs([basedir],basedir)
# @type listapordirectorio list
listapordirectorio.sort()
listaporgrupo=dirtogroup(listapordirectorio)
listaporgrupo=grouptodir(listaporgrupo,listapordirectorio)

x=len(listapordirectorio)
a=0
try:
    while a<x:
        print(listapordirectorio[a] + ' <==> ' + listaporgrupo[a].gr_name)
        a=a+1
except:
    print('There is no one-to-one relationship between groups and '+
    'directories so please fix it')


sleep(2)

quit


