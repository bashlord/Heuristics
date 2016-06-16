# -*- coding: utf-8 -*-
from p5_ordering import select_unassigned_variable
from p5_ordering import order_domain_values
from p2_is_consistent import is_consistent
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    if len(csp.assignment) == len(csp.variables):
        return True

    variable = select_unassigned_variable(csp)
    value = order_domain_values(csp, variable)
    #print variable
    #print value
    flag = 0
    for x in value:
        csp.variables.begin_transaction()
        if is_consistent(csp, variable, x):
            #print "past is_consistent"
            for var in csp.variables:
                if var == variable:
                    var.assign(x)
                    var.is_assigned()
                    solution = backtrack(csp)
                    if solution != False:
                        return True
        csp.variables.rollback()
    return False


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""
    #print "============BEGIN=================="

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    """
    print "QUEUE ARCS"
    for x in queue_arcs:
        print x
    print "fin queue arcs"
    print "\nconstraints"
    for x in csp.constraints:
        print x
    print "end constraints"
    """
    while queue_arcs:
        (v1, v2) = queue_arcs.pop()
        #print str(v1) + "---"+ str(v2)
        if revise(csp, v1, v2):
            if not v1.domain:
                return False
            #print str(v1)+ "LOOK HEREREREREREREAFVSD"
            for c in csp.constraints[v1]:
                #print "WTF IS THE ARC" + str(c)
                if c.var2 != v1 and c.var2 != v2:
                    queue_arcs.append((c.var2,v1))

    """print "AC3 IS RETURNING TRUE"
    for x in queue_arcs:
        print x"""

    return True
    

    # TODO implement this
    pass