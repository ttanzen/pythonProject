ignore = ["duplex", "alias", "configuration"]
from sys import argv
name = argv[1]
with open (name, 'r') as f:
    for line in f:
        if line[0] != '!':
           for i in ignore:
             if i in line:
                 break
           else:
                print (line.rstrip())