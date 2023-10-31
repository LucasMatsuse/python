#!usr/bin/env python3
#errors treatment

#EAFP - Easy to Ask Forgiveness than Permission
import sys
import os

try:
    names=open('names.txt').readlines()
except:
    print('[Error] File names.txt not found.')
    sys.exit(1)

try:
    print(names[2])
except:
    print('[Error] Missing name in the list')
    sys.exit(1)