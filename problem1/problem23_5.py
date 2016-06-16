import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
import utils
from timeit import default_timer as timer
current = []
for file in sys.stdin.readlines():
    line = make_tuple(file)
    #print line
    row = []
    for x in line:
        row.append(x)
    current.append(row)

#print(current)
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
    #exit()
	print ""
else:
    stack.append(current)
    path.append(current)
    pathQ.append(pathString)
    for x in range(0,11):
        stacktemp = copy.deepcopy(stack)
        pathtemp = copy.deepcopy(path)
        pathQtemp = copy.deepcopy(pathQ)
        start = timer()
        found = DLS_alpha(x, stacktemp, pathtemp, pathQtemp)
        if found != None:
           print found
           #print "Part5:: Number of nodes visited: " + str(len(pathtemp))
           end = timer()
           break
        else:
            print "None"
            break
           #print "Elapsed time-> " +str(end - start) 
           #exit()
         #print "============DONE WITH LOOP = " + str(x)
        #print "Part5:: Number of nodes visited: " + str(len(pathtemp))
        end = timer()
        #print "Elapsed time-> " +str(end - start) 