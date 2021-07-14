from sys import argv
name = argv[1]
with open (name, 'r') as f:
    for line in f:
        if line[0] != '!':
            print (line.rstrip())