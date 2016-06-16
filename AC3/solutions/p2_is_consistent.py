# -*- coding: utf-8 -*-
import sys
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'


def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned.
    python solve_puzzle.py ../solutions/p1_is_complete.py < ../problems/p1/in/input1.txt
	
    print "\n----INITIAL PARAMETERS-----\n"
    print variable
    print value


    print "\n----VARIABLES-----\n"
    for x in csp.variables:
    	print x
    print "\n----CONSTRAINTS-----\n"
    for y in csp.constraints[variable]:
    	print y
    # TODO implement this
    print "\n----done-----\n"
    """
    for x in csp.constraints[variable]:
    	#print str(value) + " "  + str(x.var2)
    	if x.var2.is_assigned():
    		if x.is_satisfied(value, x.var2.value) == False:
    			#print False
    			return False
    for x in csp.variables:
    	if x == variable:
    		#print True
    		return True
    pass
