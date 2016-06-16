import collections
from collections import Counter
import sys
import re
from ast import literal_eval as make_tuple
for line in sys.stdin.readlines():
    current = make_tuple(line)
    #print line
    if current[0] != 0 and current[0] != 1:
        print("invalid input")
    elif current[1] != 0 and current[1] !=1:
        print("invalid input")
    elif current[2] != 0 and current[2] != 1:
        print "invalid input"
    else:
        if current[0] != 0 or current[1] != 0:
            print "False"
        else:
            print "True" 