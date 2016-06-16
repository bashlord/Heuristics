import collections
import sys
from utils import *
import re
from ast import literal_eval as make_tuple
import sys

array2d = []
for file in sys.stdin.readlines():
    line = make_tuple(file)
    #print line
    row = []
    for x in line:
        row.append(x)
    array2d.append(row)


#print array2d

for x in range(len(array2d)-1):
    for y in range(len(array2d)-1):
        if array2d[x][y] > 1 or array2d[x][y] < 0:
            print "invalid input"
            #quit()

if array2d[len(array2d)-1][0] < 0 or array2d[len(array2d)-1][0] > len(array2d)-2:
    print "invalid input"
elif array2d[len(array2d)-1][1] < 0 or array2d[len(array2d)-1][1] > len(array2d)-2:
    print "invalid input"
else:
    for x in range(len(array2d)-1):
        for y in range(len(array2d)-1):
            if array2d[x][y] == 1:
                print False
                #quit()
    print True

