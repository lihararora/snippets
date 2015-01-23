#!/usr/bin/python

import os
import sys
print(os.name)
print(sys.platform)
print(os.getcwd())

#mf = open('/home/rahil/Python/pythonpractice/README.md', 'r')
#line = mf.readline()
#for line in mf.readlines():
#    print(line)

path = '/home/rahil/Python/pythonpractice'
for r,d,f in os.walk(path):
    for files in f:
        print(files)
