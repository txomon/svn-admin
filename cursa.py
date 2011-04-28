#!/usr/bin/python3.1
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__="$12-abr-2011 10:46:47$"

from time import sleep
import curses
import curses.wrapper

#hotkey_attr = curses.A_BOLD | curses.A_UNDERLINE
#menu_attr = curses.A_NORMAL


grupos=['svn','svn-actividades','svn-actividades-sensor','svn-actividades-sensor-ksensor','svn-prueba','svn-prueba-ejemplo1']
dirs=['/svn','/svn/actividades','/svn/actividades/sensor','/svn/actividades/sensor/ksensor','/svn/prueba','/svn/prueba/ejemplo1']

        # @type stdscr window
        # @type screen window
        # @type grupos list
        # @type workspace window
        # @type infobar window

def cursa(stdscr):
    umenu=("User",user_menu)
    gmenu=("Group","group_menu")
    rmenu=("Repository","repo_menu")
    menus=(umenu,gmenu,rmenu)
    global screen
    while 1:
        # @type stdscr window
        # @type screen window
        # @type grupos list
        dim=stdscr.getmaxyx()
        screen = stdscr.subwin(dim[0], dim[1], 0, 0)
        iniciacolores()
        screen.refresh()
        index=-1
        while 1:
            opciones=bartool(menus,screen,index)
            #main(arbol,index,up)
            #info(index)
            temp=0
            c=screen.getch()
            # @type opciones dict
            if chr(c) in opciones:
                while c!=temp:
                    if temp!=0:# We want to know if we have been called by another menu, or by the main window
                        if c == curses.KEY_LEFT:
                            if index==0:
                                index=len(menus)
                            index=index-1
                        if c == curses.KEY_RIGHT:
                            if index== len(menus):
                                index=-1
                            index=index+1
                        c=ord(menus[index][0][0])
                    temp=c
                    debug("Ha entrado con la tecla "+chr(temp)+"a la función "+opciones[chr(temp)].__str__()+" index="+str(index))
                    sleep(3)
                    c=opciones[chr(temp)]()

            if c==ord('q') or c==curses.KEY_RESIZE:
                break
            else:
                info("La opción para "+chr(c).__str__()+" no está implementada")
                debug(opciones.items().__str__())
        stdscr.erase()
        if c==ord('q'):
            return 0


def bartool(menus,screen,index):
    left = 0
    x=0
    dict={}
    for menu in menus:
        menu_name = menu[0]
        menu_hotkey = menu_name[0]
        menu_no_hot = menu_name[1:]
        if x==index:
            screen.addstr(0, left, menu_hotkey,menu_color|curses.A_BOLD|curses.A_REVERSE)
            screen.addstr(0, left+1, menu_no_hot,menu_color|curses.A_REVERSE)

        screen.addstr(0, left, menu_hotkey,menu_color|curses.A_BOLD)
        screen.addstr(0, left+1, menu_no_hot,menu_color)
        left = left + len(menu_name)
        screen.addstr(0, left,' '*3,menu_color)
        left=left+3
        # Añadimos los manipuladores para la tecla
        # @type dict dict
        dict[menu_hotkey.upper()]= menu[1]
        dict[menu_hotkey.lower()]= menu[1]
    # Little aesthetic thing to display application title
    # screen.addstr(1, left-1,">"*(52-left)+ " Txt2Html Curses Interface",curses.A_STANDOUT)
    screen.addstr(0,left,' '*(screen.getmaxyx()[1]-left),menu_color)
    screen.refresh()
    return dict

def menutool(menus,window,startx,starty,i):
    up=starty
    dict={}
    for menu in menus:
        menu_name = menu[0]
        menu_hotkey = menu_name[0]
        menu_no_hot = menu_name[1:]
        # @type menus tuple
        a=0
        if menus.index(menu)==i:
            a=curses.A_REVERSE
        window.addstr(up,startx,menu_hotkey,menu_color|curses.A_BOLD|a)
        window.addstr(up,startx+1,menu_no_hot,menu_color|a)
        up=up+1
        dict[menu_hotkey.upper()]= menu[1]
        dict[menu_hotkey.lower()]= menu[1]
    window.refresh()
    return dict

def user_menu():
    # @type screen window
    info("La opción para u está implementada con la funcion user_menu")

    createumenu=("Create user","create_user()")
    addumenu=("Add user","add_user()")
    unaddumenu=("Unadd user","unadd_user()")
    deleteumenu=("Delete user","delete_user()")

    usermenu=(createumenu,addumenu,unaddumenu,deleteumenu)
    x=0
    for a in usermenu:
        if len(a[0])>x:
            x=len(a[0])
    umenu=curses.newwin(len(usermenu)+2, x+2, 1, 0)
    umenu.keypad(1)
    index=0
    while 1:
        box(umenu,menu_color)
        dict=menutool(usermenu,umenu,1,1,index)
        c=umenu.getch()
        if c in (ord('q'),curses.KEY_RESIZE, curses.KEY_LEFT, curses.KEY_RIGHT):
            return c
        elif c == curses.KEY_DOWN:
            # @type dict dict
            index=index+1
            if len(usermenu)==index:
                index=0
        elif c == curses.KEY_UP:
            if index==0:
                index=len(usermenu)
            index=index-1
        elif c == curses.KEY_ENTER:
            usermenu[index]()
        elif c in dict:
            dict[chr(c)]()
        else:
            info("Has pulsado "+chr(c)+" con codigo "+c.__str__())
        


def iniciacolores():

    if curses.has_colors():
        # @type screen window
        #screen.bkgd(curses.COLOR_BLUE)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLUE)
    global normal_color
    global menu_color
    global error_color
    global debug_color
    global info_color

    if curses.has_colors():
        normal_color=curses.color_pair(0)
        menu_color=curses.color_pair(1)
        info_color=curses.color_pair(2)
        error_color=curses.color_pair(3)
        debug_color=curses.color_pair(4)
    else:
        normal_color=''
        menu_color=''
        info_color=''
        error_color=''
        debug_color=''
    return

def box(window,attr):
    # ┌┐└┘─│
    ul='┌'
    ur='┐'
    dl='└'
    dr='┘'
    h='─'
    v='│'
    # @type window window
    b=0
    dim=window.getmaxyx()
    y=dim[0]-1
    x=dim[1]-1
    while b<=y: #| b==y:
        a=0
        while a<=x:# | a==x:
            if b==0:
                if a==0:
                    window.insstr(b, a, ul, attr)
                elif a==x:
                    window.insstr(b, a, ur, attr)
                else:
                    window.insstr(b, a, h, attr)
            elif b==y:
                if a==0:
                    window.insstr(b, a, dl, attr)
                elif a==x:
                    window.insstr(b, a, dr, attr)
                else:
                    window.insstr(b, a, h, attr)
            else:
                if a==0:
                    window.insstr(b, a, v, attr)
                elif a==x:
                    window.insstr(b, a, v, attr)
                else:
                    window.insstr(b, a,' ',attr)
            a=a+1
        b=b+1
    return

def debug(str):
    dim=screen.getmaxyx()
    screen.addnstr(dim[0]-1,0,' '*dim[1],dim[1]-1,debug_color)
    screen.addnstr(dim[0]-1,0,str,dim[1]-1,debug_color)
    screen.refresh()

def info(str):
    dim=screen.getmaxyx()
    screen.addnstr(dim[0]-2,0,' '*dim[1],dim[1]-1,info_color)
    screen.addnstr(dim[0]-2,0,str,dim[1]-1,info_color)
    screen.refresh()

curses.wrapper(cursa)
