import os.path
import os
from grp import getgrall

"""
In this file, I am going to store all the functions refering to the interaction
 to the system
"""

class grupos:
def parse_grupos():
    """Parses groups and filters the ones that have gid>9999 (this svn-admin is
       supposed to work from 10000 and ahead """
    a=getgrall()
    lista=[]
    # @type a tuple
    a.sort()
    for item in a:
        # @type item grp
        if ('svn' in item.gr_name) and (item.gr_gid > 9999):
            lista.append(item)
    if len(lista) == 0:
        print("No svn structure in groups file")
        return(-1)
    return lista

def parse_dirs(lista,basedir):
    """Parses the basepath recurrently and checks if there is any README.txt in
       the directory as a simple way of checkin if it is a svn repo. It also 
       filters the lost+found dir, as if it is a self partition, it will
       probably have one"""
    a=os.walk(basedir)
    # @type list list
    for (path, dirs, files) in a:
        if (not 'README.txt' in files):
            for dir in dirs:
                b=basedir+'/'+dir
                if (not 'lost+found' in dir):
                    lista.append(b);
                    lista=parse_dirs(lista,b)
            break
    return lista

def grouptodir(groups, dirs):
    """Checks if the groups are one-to-one with the directories, and if not, it
       offers to delete the remaining groups"""
    i=0
    for group in groups:
        a=group.gr_name
        a=a.replace('-', '/')
        a='/'+a
        try:
            dirs.index(a)
        except ValueError:
            i=i+1
            print ("WARNING!: Extra group ("+i.__str__()+") in your /etc/group file! => "+a)
            opcion=raw_input("Do you want to delete the group? [S/n]")
            if opcion != 'n' and opcion != 'N':
                delgroup(group.gr_name)
                groups=parse_grupos()
                
    return groups 

def dirtogroup(dirs):
    """Creates a group for each dir, checking if already doesn't exist"""
    i=0
    x=-1
    for dir in dirs:
        # @type a str
        if i!=x:
            x=i;
            lista=[]
            listaxgrupos=parse_grupos()
            for a in listaxgrupos:
                lista.append(a.gr_name)
        a=dir
        a=a.replace('/', '', 1)
        a=a.replace('/', '-')
        if not (a in lista):
            i=i+1
            print("se crea el grupo "+a)
            creategroup(a,listaxgrupos)
    return listaxgrupos

def creategroup(group,groups):
    """Creates a group with the name group and puts the last gid+1"""
    lista=[]
    for a in groups:
        lista.append(a.gr_gid)
    lista.sort()
    gid=lista.pop()+1
    os.system("addgroup --gid "+gid.__str__()+" "+group)
    #os.system("addgroup --gid "+gid+" "+group)

def delgroup(group):
    """Deletes the group"""
    os.system("delgroup "+group)


