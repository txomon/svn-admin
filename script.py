import os.path
import os
from grp import getgrall

def parse_grupos():
    a=getgrall()
    lista=()
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

def parse_dirs(basedir):
    a=os.walk(basedir)
    # @type list list
    lista=[]
    for (path, dirs, files) in a:
        for dir in dirs:
            b=basedir+'/'+dir
            lista.append(b);
            parse_dirs(b)
        break
