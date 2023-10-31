#!usr/bin/env python3
#errors treatment

#EAFP - Easy to Ask Forgiveness than Permission
import sys
import os

try:
    names=open('names.txt').readlines() #FileNotFoundError
    1/1 #ZeroDivisionError
    print(names.abuble) #AttributeError
except FileNotFoundError: 
    print('[Error] File names.txt not found.')
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You can't divide by zero!")
    sys.exit(1)
except AttributeError:
    print("[Error] List don't have abuble attribute.")
    sys.exit(1)

try:
    print(names[2])
except:
    print('[Error] Missing name in the list')
    sys.exit(1)