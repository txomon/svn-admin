#!/usr/bin/python
# vim: set fileencoding=UTF-8 
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="javier"
__date__="$12-abr-2011 10:46:47$"

from time import sleep
import curses
import curses.wrapper

#hotkey_attr = curses.A_BOLD | curses.A_UNDERLINE
#menu_attr = curses.A_NORMAL

#variables de grupos y directorios actuales
grupos=['svn','svn-actividades','svn-actividades-sensor','svn-actividades-sensor-ksensor','svn-prueba','svn-prueba-ejemplo1']
dirs=['/svn','/svn/actividades','/svn/actividades/sensor','/svn/actividades/sensor/ksensor','/svn/prueba','/svn/prueba/ejemplo1']

        # @type stdscr window
        # @type screen window
        # @type grupos list
        # @type workspace window
        # @type infobar window

def cursa(stdscr):
    #Las llamadas a cada menu
    umenu=("User",user_menu)
    gmenu=("Group","group_menu")
    rmenu=("Repository","repo_menu")
    #Las junto todas en uno
    menus=(umenu,gmenu,rmenu)
    global screen
    while 1:
        # @type stdscr window
        # @type screen window
        # @type grupos list
        dim=stdscr.getmaxyx() #mido cuanto mide la terminal actual
        screen = stdscr.subwin(dim[0], dim[1], 0, 0)#creo una ventana con esas dimensiones
        iniciacolores()#Habilito los colores, e inicializo los mios
        curses.curs_set(0)
        screen.refresh()#Hago efectivos los cambios
        index=0#-1 si no hay ningun menu
        while 1:
            opciones=bartool(menus,screen,index)#paso el menu seleccionado al creador de la barra de arriba
            #main(arbol,index,up)
            #info(index)
            c=screen.getch()#capturamos el caracter
            # @type opciones dict
            while chr(c) in opciones:#en el bucle de las opciones admitidas
                    debug("Ha entrado con la tecla "+chr(c)+" a la función "+opciones[chr(c)].__str__()+" index="+str(index))
                    c=opciones[chr(c)]()#nos metemos en el menú que toca y almacenamos la tecla que nos saca de el
                    debug("Ha salido pulsando la tecla "+c.__str__()+": c=q/Q(0)")
                    if c in (curses.KEY_LEFT, curses.KEY_RIGHT):#Si la tecla recibida es un cambio de menu (flechas)
                        if c == curses.KEY_LEFT:#Si hemos pulsado la tecla hacia la izquierda
                            if index==0:# si estamos a la izq del todo
                                index=len(menus)#pasamos a la derecha del todo +1
                            index=index-1#nos movemos 1 hacia la izq
                        if c == curses.KEY_RIGHT:#Si es la derecha
                            if index== (len(menus)-1):#si estamos a la derecha del todo
                                index=-1#nos pasamos a la izquierda del todo -1
                            index=index+1#nos movemos 1 hacia la derecha
                        c=ord(menus[index][0][0])#Emulamos una pulsacion hacia el menu que apunta la flecha


            if c in (ord('q'), ord('Q'), 0,curses.KEY_RESIZE):
                break#salimos del bucle si cambia la ventana o si se presiona la q
            else:#si no, decimos que la opción no esta implementada
                info("La opcion para "+chr(c).__str__()+" no está implementada")
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

    #Creamos los menus
    createumenu=("Create user","create_user()")
    addumenu=("Add user","add_user()")
    unaddumenu=("Unadd user","unadd_user()")
    deleteumenu=("Delete user","delete_user()")

    #juntamos los menus
    usermenu=(createumenu,addumenu,unaddumenu,deleteumenu)

    #miramos cual es la palabra mas larga en el menú
    x=0
    for a in usermenu:
        if len(a[0])>x:
            x=len(a[0])

    #creamos una ventana nueva
    umenu=curses.newwin(len(usermenu)+2, x+2, 1, 0)

    #activamos el reconocimiento de flechas
    umenu.keypad(1)
    
    index=0
    while 1:
        #creamos el borde de la ventana
        box(umenu,menu_color)

        #averiguamos cuales son las teclas que tenemos que reconocer
        dict=menutool(usermenu,umenu,1,1,index)
        c=umenu.getch()
        debug("Dentro de User se ha pulsado "+c.__str__())
	if c in (ord('q'),ord('Q')):#Si ha presionado la q o la Q
            umenu.erase()
            return 0
        if c in (curses.KEY_RESIZE, curses.KEY_LEFT, curses.KEY_RIGHT):#Si ha presionado una flechita o ha redimensionado la pantalla
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
    #ul='┌'
    #ur='┐'
    #dl='└'
    #dr='┘'
    #h='─'
    #v='│'
    ul='#'
    ur='#'
    dl='#'
    dr='#'
    h='#'
    v='#'
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
