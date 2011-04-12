#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__ ="$09-mar-2011 15:17:25$"

from dirgroup import *
from time import sleep
from graphic import *

fuera=0

listaporgrupo=parse_grupos()
if listaporgrupo == -1:
    exit(-1)
listapordirectorio=parse_dirs(['/svn'],'/svn')
# @type listapordirectorio list
listapordirectorio.sort()
listaporgrupo=dirtogroup(listapordirectorio)
listaporgrupo=grouptodir(listaporgrupo,listapordirectorio)
for a in listaporgrupo:
	print(a.gr_name)
for a in listapordirectorio:
	print(a)
sleep(2)
try:
    stdscr=inicia_curses()
    while fuera==0:
        c=stdscr.getch()
        if c == curses.KEY_RESIZE:
            stdscr.refresh()
        if c == ord('q') | c== ord('Q') | c == curses.KEY_EXIT:
            fuera=1
except :
    finaliza_curses(stdscr)
sleep(2)
finaliza_curses(stdscr)




