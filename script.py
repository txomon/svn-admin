import os.path
import os
from grp import getgrall

def parse_grupos():
    a=getgrall()
    lista=[]
    # @type a tuple
    a.sort()
    for item in a:
        # @type item grp
        if 'svn' in item.gr_name and item.gr_gid > 9999:
            lista.append(item)
    if len(lista) == 0:
        print("No svn structure in groups file")
        return(0)
    return lista

def parse_dirs(lista,basedir):
    a=os.walk(basedir)
    # @type list list
    for (path, dirs, files) in a:
        if (not 'README.txt' in files):
            for dir in dirs:
                b=basedir+'/'+dir
                lista.append(b);
                lista=parse_dirs(lista,b)
            break
    return lista

def grouptodir(groups, dirs):
    i=0
    for group in groups:
        a=group.gr_name
        a=a.replace('-', '/')
        a='/'+a
        try:
            dirs.index(a)
	except ValueError:
            i=i+1
            print ("se crea la carpeta "+a)
            #  os.makedirs(a, 4777)
    return i

def dirtogroup(groups, dirs):
    i=0
    lista=[]
    for a in groups:
	lista.append(a.gr_name) 
    for dir in dirs:
        # @type a str
        a=dir
        a=a.replace('/', '', 1)
        a=a.replace('/', '-')
        if not (a in lista):
            i=i+1
            print("se crea el grupo "+a)
            # creargrupo()
    return i
