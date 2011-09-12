import os.path
import os
from grp import getgrall

"""
In this file, I am going to store all the functions refering to the interaction
 to the system
"""

class svn_state:
    basedir='svn'
    def __init__(self):
        self.parse_dirs()
        self.parse_groups()
        self.dirtogroup()
        self.grouptodir()
        
    def parse_groups():
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

    def parse_dirs():
        return self.__get_parser_dirs(self.basedir,[self.basedir])
    
    def __get_parser_dirs(basedir,lista):
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
                        lista=self.__get_parser_dirs(b,lista)
                break
        return lista

    def grouptodir():
        """Checks if the groups are one-to-one with the directories, and if not, it
           offers to delete the remaining groups"""
        i=0
        for group in self.bygroups:
            a=group.gr_name
            a=a.replace('-', '/')
            a='/'+a
            try:
                self.bydirs.index(a)
            except ValueError:
                i=i+1
                print ("WARNING!: Extra group ("+i.__str__()+") in your /etc/group file! => "+a)
                opcion=raw_input("Do you want to delete the group? [S/n]")
                if opcion != 'n' and opcion != 'N':
                    self.__delgroup(group.gr_name)
                    self.bygroups=self.parse_groups()
                    
        return groups 

    def dirtogroup():
        """Creates a group for each dir, checking if already doesn't exist"""
        i=0
        x=-1
        for dir in self.bydirs:
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
                self.__creategroup(a,listaxgrupos)
        return listaxgrupos

    def __creategroup(group,groups):
        """Creates a group with the name group and puts the last gid+1"""
        lista=[]
        for a in groups:
            lista.append(a.gr_gid)
        lista.sort()
        gid=lista.pop()+1
        os.system("addgroup --gid "+gid.__str__()+" "+group)
        #os.system("addgroup --gid "+gid+" "+group)

    def __delgroup(group):
        """Deletes the group"""
        os.system("delgroup "+group)


