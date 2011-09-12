import os.path
import os
from grp import getgrall

"""
In this file, I am going to store all the functions refering to the interaction
 to the system
"""
class svn_state():
    basedir='/svn'
    def __init__(self):
        self.parse_dirs()
        self.printdebug('self.bydirs at the beggining '+self.bydirs.__str__())
        self.parse_groups()
        self.printdebug('self.bygroups at the beggining '+self.bygroups.__str__())
        self.dirtogroup()
        self.printdebug('self.bygroups after dirtogroup() '+self.bygroups.__str__())
        self.grouptodir()
        self.printdebug('self.bydirs after grouptodir() '+self.bydirs.__str__())
        
    def printdebug(self,string):
        try:
            if os.environ['DEBUG']:
                print("[DEBUG]"+string)
        except:
            return

    def parse_groups(self):
        """Parses groups and filters the ones that have gid>9999 (this svn-admin is
           supposed to work from 10000 and ahead """
        a=getgrall()
        lista=[]
        # @type a tuple
        a.sort()
        for item in a:
            # @type item grp
            if ('svn' in item.gr_name) and (item.gr_gid > 9999):
                lista.append(item.gr_name)
        if len(lista) == 0:
            print("No svn structure in groups file")
            return(-1)
        self.bygroups=lista

    def parse_dirs(self):
        self.bydirs = self.__get_parser_dirs(self.basedir,[self.basedir])
    
    def __get_parser_dirs(self,basedir,lista):
        """Parses the basepath recurrently and checks if there is any README.txt in
        the directory as a simple way of checkin if it is a svn repo. It also 
        filters the lost+found dir, as if it is a self partition, it will
        probably have one"""
            
        a=os.walk(basedir)
        # @type list list
        for (path, dirs, files) in a:
            self.printdebug('dirs in '+basedir+' '+dirs.__str__())
            if (not 'README.txt' in files):
                for dir in dirs:
                    b=basedir+'/'+dir
                    if (not 'lost+found' in dir):
                        lista.append(b);
                        lista=self.__get_parser_dirs(b,lista)
                break
        return lista

    def grouptodir(self):
        """Checks if the groups are one-to-one with the directories, and if not, it
           offers to delete the remaining groups"""
        i=0
        for group in self.bygroups:
            a=group
            a='/'+a.replace('-', '/')
            if not (a in self.bydirs):
                i=i+1
                print ("WARNING!: Extra group ("+i.__str__()+") in your /etc/group file! => "+a)
                opcion=input("Do you want to delete the group? [s/N]")
                if 'Y' in opcion.upper():
                    self.__delgroup(self,group)
                    

    def dirtogroup(self):
        """Creates a group for each dir, checking if already doesn't exist"""
        for dir in self.bydirs:
            temp=dir
            temp=temp.replace('/','',1)
            temp=temp.replace('/','-')
            if not (temp in self.bygroups):
                self.__creategroup(temp)


    def __creategroup(self,group):
        """Creates a group with the name group and puts the last gid+1"""
        a=getgrall()
        lista=[]
        # @type a tuple
        for item in a:
            # @type item grp
            if ('svn' in item.gr_name) and (item.gr_gid > 9999):
                lista.append(item.gr_gid)
        lista.sort()
        gid=lista.pop()+1
        self.printdebug('I am going to try to add '+ group + ' to the groups file')
        os.system("addgroup --gid "+gid.__str__()+" "+group)
        self.parse_groups()

    def __delgroup(self,group):
        """Deletes the group"""
        os.system("delgroup "+group)
        self.parse_groups()


