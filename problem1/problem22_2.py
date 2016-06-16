import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

for line in sys.stdin.readlines():
	pathString = ""
	pathHolder = []
	state = False
	line.replace(" ", "")
	line = make_tuple(line)
	#line = re.sub('[,]', '', line)
	current = ()
	for x in range(len(line)):
		temp = (line[x])
		current = current + (line[x],)
	queue = Queue()
	pathQ = Queue()
	path = []
	if check_clean_beta(current):
		#print "Done cleaning"
		break
	else:
		#print "better start cleaning"
		#print "---------ENTERING THE STATES------------"
		queue.enqueue(current)
		path.append(current)
		pathQ.enqueue(pathString)
		start = timer()

	while state != True:
		node = queue.dequeue()
		pathS = pathQ.dequeue()
		if check_clean_beta(node):
			#print "Done cleaning after tries"
			state = True
			print pathS
			#print "Part2:: Number of nodes visited: " + str(len(path))
			end = timer()
			#print "Elapsed time-> " + str(end - start)
			break
		else:
			#print node
			flag = 0
			if LRS_beta(0,node) not in path:
				queue.enqueue(LRS_beta(0,node))
				path.append(LRS_beta(0,node))
				pathQ.enqueue(pathS + "L")
				#print "moved left"
			if LRS_beta(1,node) not in path:	
				queue.enqueue(LRS_beta(1,node))
				path.append(LRS_beta(1,node))
				pathQ.enqueue(pathS + "R")
				#print "moved right"
			if LRS_beta(2,node) not in path:
				queue.enqueue(LRS_beta(2,node))
				path.append(LRS_beta(2,node))
				pathQ.enqueue(pathS + "S")
				#print "moved suck"

