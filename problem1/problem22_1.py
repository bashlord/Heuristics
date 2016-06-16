import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
for line in sys.stdin.readlines():
    line = make_tuple(line)
    #current = (line[0], line[1], line[2])
    #print line
    length = len(line)-1
    for x in range(length-1):
        if line[x] != 0 and line[x] != 1:
            print("invalid input")

    if line[length] < 0 or line[length] > length-1:
            print "invalid input"
    else:
        for x in range(length):
            if line[x] != 0:
                print("False")
                #exit()

        print("True")