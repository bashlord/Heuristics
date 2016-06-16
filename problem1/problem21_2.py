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
	queue = Queue()
	path = []
	pathQ = Queue()
	if check_clean(current):
		#print "Done cleaning"
		break
	else:
		#print "better start cleaning"
		#print "---------ENTERING THE STATES------------"
		queue.enqueue(current)
		path.append(current)
		pathQ.enqueue("")
		start = timer()

	while state != True:
		node = queue.dequeue()
		pathS = pathQ.dequeue()
		if check_clean(node):
			#print "Done cleaning after tries"
			print pathS
			state = True
			#print "Part2:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start)
			break
		else:
			#print "Current state still needs cleaning ::"
			#print node
			if LRS(0,node) not in path and LRS(0,node) != node:
				queue.enqueue(LRS(0,node))
				path.append(LRS(0,node))
				pathQ.enqueue(pathS + "L")
				#print "moved left"
			if LRS(1,node) not in path and LRS(1,node) != node:	
				queue.enqueue(LRS(1,node))
				path.append(LRS(1,node))
				pathQ.enqueue(pathS + "R")
				#print "moved right"
			if LRS(2,node) not in path and LRS(2,node) != node:
				queue.enqueue(LRS(2,node))
				path.append(LRS(2,node))
				pathQ.enqueue(pathS + "S")
				#print "moved suck"
