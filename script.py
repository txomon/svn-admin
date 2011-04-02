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
            print("Found "+item.gr_name)
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
    for group in groups:
        a=group.gr_name
        a.replace('-', '/')
        if not group in dirs:
            i=i+1
            print ("se crea la carpeta "+a)
          #  os.makedirs(a, 4777)
    return i

def dirtogroup(groups, dirs):
    for dir in dirs:
        # @type a str
        a=dir
        a.replace('-', '/')
        a[0]=' '
        a=a.rstrip()
        if not dir in groups:
           i=i+1
	   print("Se crea el grupo "+dir)
	   # creargrupo()
    return i
