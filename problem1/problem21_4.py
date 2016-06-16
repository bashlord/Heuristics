import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
from timeit import default_timer as timer


for line in sys.stdin.readlines():
	#print line
	depth = 0
	state = False
	current = make_tuple(line)
	#print line
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
		DLS(5, stack, path, pathQ)
		#print "Part4:: Number of nodes visited: " + str(len(path))
		end = timer()
		#print "Elapsed time-> " + str(end - start)

