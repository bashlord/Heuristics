import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

for line in sys.stdin.readlines():
	#print line
	state = False
	current = make_tuple(line)
	stack = []
	path = []
	pathQ = []
	if check_clean(current):
		#print "Done cleaning"
		break
	else:
		#print "better start cleaning"
		#print "---------ENTERING THE STATES------------"
		stack.append(current)
		path.append(current)
		pathQ.append("")
		start = timer()

	while state != True:
		node = stack.pop()
		pathS = pathQ.pop()
		if check_clean(node):
			#print "Done cleaning after tries"
			state = True
			print pathS
			#print "Part3:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start)
			break
		else:
			#print "Current state still needs cleaning ::"
			#print node
			path.append(node)
			if LRS(2,node) not in path and LRS(2,node) != node:
				stack.append(LRS(2,node))
				#path.append(LRS(2,node))
				pathQ.append(pathS + "S")
				#print "moved suck"
			if LRS(1,node) not in path and LRS(1,node) != node:	
				stack.append(LRS(1,node))
				#path.append(LRS(1,node))
				pathQ.append(pathS + "R")
				#print "moved right"
			if LRS(0,node) not in path and LRS(0,node) != node:
				stack.append(LRS(0,node))
				#path.append(LRS(0,node))
				pathQ.append(pathS + "L")
				#print "moved left"
