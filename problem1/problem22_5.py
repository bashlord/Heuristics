import collections
import sys
from utils import *
import utils
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
	if check_clean(current):
		#print "Done cleaning"
		break
	else:
		#print "better start cleaning"
		#print "---------STARTING DEPTH LIMITED search------------"
		stack.append(current)
		path.append(current)
		pathQ.append("")
		start = timer()
		for x in range(0, 9):
			#print x
			stacktemp = copy.deepcopy(stack)
			pathtemp = copy.deepcopy(path)
			pathQtemp = copy.deepcopy(pathQ)
			found = DLS_beta(x, stacktemp, pathtemp, pathQtemp)
			if found != None:
				#print "Part5:: Number of nodes visited: " + str(len(pathtemp))
				end = timer()
				#print "Elapsed time-> " + str(end - start)
				print found
				#exit()
				break
			else:
				print found
				break
			#print "============DONE WITH LOOP = " + str(x)


