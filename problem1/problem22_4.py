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
	if check_clean(current):
		#print "Done cleaning"
		break
	else:
		start = timer()
		stack.append(current)
		path.append(current)
		pathQ.append(pathS)
		ret = (DLS_beta_pure(5, stack, path, pathQ))
		print ret
		#print "Part4:: Number of nodes visited: " + str(len(path))
		end = timer()
		#print "Elapsed time-> " + str(end - start)
		#print pathString



