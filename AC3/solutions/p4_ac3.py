# -*- coding: utf-8 -*-
from p2_is_consistent import is_consistent
from p1_is_complete import is_complete
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque


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

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    flag = False
    for x in xi.domain:
        count = 0
        for constrain in csp.constraints[xi]:
            #print "THIS IS THE CONSTRAINT " + str(constrain) + "AND THIS IS VAL " + x
            for y in xj.domain:
                #print str(x) + " &*&*(^& WHAT THE ACTUAL FUCK " + str(y)
                if (constrain.var2 == xj and (constrain.is_satisfied(x, y))):
                    count += 1
        if count == 0:
            flag = True
            xi.domain.remove(x)
    #print "THIS IS THE REVISE FLAG RETURNED " + str(flag)
    return flag





"""
    flag = False
    exists = 0
    print str(xi) + " revised with " + str(xj)
    print csp.constraints[xi]
    for x in xi.domain:
        print x
        if not any([(con.is_satisfied(x,y) for con in csp.constraints[xi]) for y in xj.domain]):
            print "REVISE CONSR3R12385780&&*(^798"
            flag = True
            xi.domain.remove(x)
            for q in csp.variables:
                if q == xi:
                    q.domain.remove(x)
    return flag
   if exists == 0:
        flag = True
        for val in csp.variables:
            if val == xj:
                val.domain.remove(x)

    if flag = True:
        for var in csp.variables:
            if var = xi:
                csp.
    pass
"""