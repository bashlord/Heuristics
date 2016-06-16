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
	#exit()
	print ""
	#print "Done cleaning"
else:
	start = timer()
	stack.append(current)
	path.append(current)
	pathQ.append(pathString)

	while state != True:
		node = stack.pop()
		pathS = pathQ.pop()
		if check_clean_alpha(node):
			#print "Done cleaning after tries"
			state = True
			print pathS
			#print "Part6:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start) 
			break
		else:
			#print "Current state still needs cleaning ::"
			#print node
			path.append(node)
			flag = heur_search_meta(node)
			if flag == 4:
				stack.append(LRS_alpha(4,node))
				#path.append(LRS_alpha(4,node))
				pathQ.append(pathS + "S")
				#print "moved suck"
			if flag == 0:
				stack.append(LRS_alpha(0,node))
				#path.append(LRS_alpha(0,node))
				pathQ.append(pathS + "L")
				#print "moved left"
			if flag == 1:
				stack.append(LRS_alpha(1,node))
				#path.append(LRS_alpha(1,node))
				pathQ.append(pathS + "U")
				#print "moved up"
			if flag == 2:
				stack.append(LRS_alpha(2,node))
				#path.append(LRS_alpha(2,node))
				pathQ.append(pathS + "R")
				#print "moved right"
			if flag == 3:
				stack.append(LRS_alpha(3,node))
				#path.append(LRS_alpha(3,node))
				pathQ.append(pathS + "D")
				#print "moved down"