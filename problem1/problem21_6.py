import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

for line in sys.stdin.readlines():
	state = False
	current = make_tuple(line)
	stack = []
	path = []
	pathQ = []
	#print line
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
			#print "Part6:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start)
			break
		else:
			#print "Current state still needs cleaning ::"
			#print node

			if node[2] == 0:
				if node[0] == 1:
				#is in room 1 and room 1 is dirty
					stack.append(LRS(2,node))
					path.append(LRS(2,node))
					pathQ.append(pathS + "S")
				else:
					stack.append(LRS(1,node))
					path.append(LRS(1,node))
					pathQ.append(pathS + "R")
			if node[2] == 1:
				if node[1] == 1:
					#is in room 2 and room 2 is dirty
					stack.append(LRS(2,node))
					path.append(LRS(2,node))
					pathQ.append(pathS + "S")
				else:
					stack.append(LRS(0,node))
					path.append(LRS(0,node))
					pathQ.append(pathS + "L")
