from sys import argv
from os import system

if system('ping ' + argv[1] + ' > nul') == 0: 
    print('UP !') 
else:
    print('DOWN !')