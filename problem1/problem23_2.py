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
queue = Queue()
pathQ = Queue()
path = []



if check_clean_alpha(current):
	#print "Done cleaning"
	#exit()
	print ""
else:
	start = timer()
	queue.enqueue(current)
	path.append(current)
	pathQ.enqueue(pathString)
	#print path

	while state != True:
		node = queue.dequeue()
		pathS = pathQ.dequeue()
		if check_clean_alpha(node):
			end = timer()
			#print "Elapsed time-> " + str(end - start) 
			state = True
			print pathS
			#print "Part2:: Number of nodes visited: " + str(len(path))
			break
		else:
			#print node
			if LRS_alpha(0,node) not in path and LRS_alpha(0,node) != None:
				#print "0"
				queue.enqueue(LRS_alpha(0,node))
				path.append(LRS_alpha(0,node))
				pathQ.enqueue(pathS + "L")
				#print "moved left"
			if LRS_alpha(1,node) not in path and LRS_alpha(1,node) != None:
				#print "1"
				queue.enqueue(LRS_alpha(1,node))
				path.append(LRS_alpha(1,node))
				pathQ.enqueue(pathS + "U")
				#print "moved up"
			if LRS_alpha(2,node) not in path and LRS_alpha(2,node) != None:
				#print "2"
				queue.enqueue(LRS_alpha(2,node))
				path.append(LRS_alpha(2,node))
				pathQ.enqueue(pathS + "R")
				#print "moved right"
			if LRS_alpha(3,node) not in path and LRS_alpha(3,node) != None:	
				#print "3"
				queue.enqueue(LRS_alpha(3,node))
				path.append(LRS_alpha(3,node))
				pathQ.enqueue(pathS + "D")
				#print "moved down"
			if LRS_alpha(4,node) not in path and LRS_alpha(4,node) != None:
				#print "4"
				queue.enqueue(LRS_alpha(4,node))
				path.append(LRS_alpha(4,node))
				pathQ.enqueue(pathS + "S")
				#print "moved suck"


