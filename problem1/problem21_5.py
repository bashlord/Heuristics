import collections
import sys
from utils import *
import re
import utils
from ast import literal_eval as make_tuple
from timeit import default_timer as timer

for line in sys.stdin.readlines():
	#print line
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
	if check_clean(current):
		#print "Done cleaning"
		break
	else:
		start = timer()
		stack.append(current)
		path.append(current)
		pathQ.append("")
		for x in range(0, 9):
			stacktemp = copy.deepcopy(stack)
			pathtemp = copy.deepcopy(path)
			pathQtemp = copy.deepcopy(pathQ)
			#print x
			found = DLS_beta(x, stacktemp, pathtemp, pathQtemp)
			if found != None:
				print found
				break
		#print "Part5:: Number of nodes visited: " + str(len(path))
		end = timer()
		#print "Elapsed time-> " + str(end - start)



