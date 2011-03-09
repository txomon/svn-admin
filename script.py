import string, pwd,grp

def parse_config():
    a =grp.getgrall()
    lista=[]
    # @type a list
    a.sort()
    for item in a:
        # @type item grp
        if 'svn' in item:
            lista.append(item)
    print (lista)
    