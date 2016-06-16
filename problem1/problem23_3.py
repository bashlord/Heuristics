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
"""
for x in range(len(current)-1):
    for y in range(len(current)-1):
        if current[x][y] != 0 and current[x][y] != 1:
            print "not valid"
            quit()

if current[len(current)-1][0] < 0 or current[len(current)-1][0] > len(current)-2:
    print False
    quit()
elif current[len(current)-1][1] < 0 or current[len(current)-1][1] > len(current[0])-1:
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
	#print "Done cleaning"
	print ""
	#exit()
else:
	start = timer()
	stack.append(current)
	path.append(current)
	pathQ.append(pathString)
	#print path

	while state != True:
		node = stack.pop()
		pathS = pathQ.pop()
		if check_clean_alpha(node):
			#print "Done cleaning after tries"
			state = True
			print pathS
			#print "Part3:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start)
			break
		else:
			path.append(node);
			#print node
			#print pathS
			if LRS_alpha(4,node) not in path and LRS_alpha(4,node) != node:
				stack.append(LRS_alpha(4,node))
				#path.append(LRS_alpha(4,node))
				pathQ.append(pathS + "S")
				#print "moved suck"
			if LRS_alpha(3,node) not in path and LRS_alpha(3,node) != node:	
				stack.append(LRS_alpha(3,node))
				#path.append(LRS_alpha(3,node))
				pathQ.append(pathS + "D")
				#print "moved down"
			if LRS_alpha(2,node) not in path and LRS_alpha(2,node) != node:
				stack.append(LRS_alpha(2,node))
				#path.append(LRS_alpha(2,node))
				pathQ.append(pathS + "R")
				#print "moved right"
			if LRS_alpha(1,node) not in path and LRS_alpha(1,node) != node:
				stack.append(LRS_alpha(1,node))
				#path.append(LRS_alpha(1,node))
				pathQ.append(pathS + "U")
				#print "moved up"
			if LRS_alpha(0,node) not in path and LRS_alpha(0,node) != node:
				stack.append(LRS_alpha(0,node))
				#path.append(LRS_alpha(0,node))
				pathQ.append(pathS + "L")
				#print "moved left"





