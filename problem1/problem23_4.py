import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

current = []
for file in sys.stdin.readlines():
    line = make_tuple(file)
    #print line
    row = []
    for x in line:
        row.append(x)
    current.append(row)
#print(len(current))
"""
for x in range(len(current)-1):
    for y in range(len(current)-1):
        if current[x][y] != 0 and current[x][y] != 1:
            print "not valid"
            quit()

if current[len(current)-1][0] < 0 or current[len(current)-1][0] > len(current)-2:
    print False
    quit()
elif current[len(current)-1][1] < 0 or current[len(current)-1][1] > len(current)-2:
    print False
    quit()
else:
    print True
"""
pathString = ""
pathHolder = []
state = False
stack = []
pathQ = []
path = []



if check_clean_alpha(current):
    #break
	print ""
else:
    #print current
    start = timer()
    stack.append(current)
    pathQ.append(pathString)
    found = DLS_alpha_pure(7, stack, path, pathQ)
    if found != None:
        print found
    else:
        print found
#print "Part4:: Number of nodes visited: " + str(len(path))
end = timer()
#print "Elapsed time-> " + str(end - start) 


