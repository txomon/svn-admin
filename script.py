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
        if 'svn' in item.gr_name:
            print("Found",item.gr_name)
            lista.append(item)
    if len(lista) == 0:
        print("No svn structure in groups file")
        return(0)
    else:
        print (lista)
    return lista

def parse_dirs(lista,basedir):
    a=os.walk(basedir)
    # @type list list
    for (path, dirs, files) in a:
        if files.find()
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
        if dirs == false :
            os.makedirs(a, 4777)
    return

def dirtogroup(groups, dirs):
    for dir in dirs:
        a=dir
        a.replace('-', '/')
        if
