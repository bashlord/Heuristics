import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

for line in sys.stdin.readlines():
	depth = 0
	state = False
	pathHolder = []
	line.replace(" ", "")
	pathS = ""
	line = make_tuple(line)
	#line = re.sub('[,]', '', line)
	current = ()
	for x in range(len(line)):
		temp = (line[x])
		current = current + (line[x],)
	stack = []
	path = []
	pathQ = []
	index = len(current)-1
	if check_clean(current):
		##print "Done cleaning"
		break
	else:
		#print "better start cleaning"
		#print "---------ENTERING THE STATES------------"
		stack.append(current)
		path.append(current)
		pathQ.append(pathS)
		start = timer()

	while state != True:
		node = stack.pop()
		pathS = pathQ.pop()
		if check_clean_beta(node):
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

			if node[node[index]] == 1:
				stack.append(LRS_beta(2,node))
				path.append(LRS_beta(2,node))
				pathQ.append(pathS + "S")
				#print "moved suck"
			else:
				if heur_search(node) == 0:
					stack.append(LRS_beta(0,node))
					path.append(LRS_beta(0,node))
					pathQ.append(pathS + "L")
					#print "moved left"
				else:
					stack.append(LRS_beta(1,node))
					path.append(LRS_beta(1,node))
					pathQ.append(pathS + "R")
					#print "moved right"
