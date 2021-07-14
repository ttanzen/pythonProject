ignore = ["duplex", "alias", "configuration"]
from sys import argv
src = argv[1]
dst = argv[2]

with open (src, 'r') as f, open(dst, 'w') as f2:
    for line in f:
        if line[0] != '!':
           for i in ignore:
             if i in line:
                 break
           else:
                f2.write (line)