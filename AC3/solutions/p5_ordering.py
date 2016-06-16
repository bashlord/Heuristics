# -*- coding: utf-8 -*-
from p2_is_consistent import is_consistent
from p1_is_complete import is_complete
from copy import deepcopy
from operator import itemgetter
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'


def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """
    smallest = -1
    largest = 0
    multiple = False
    returned = None

    for unass in csp.variables:
        if not unass.is_assigned():
            if len(unass.domain) < smallest or smallest == -1:
                smallest = len(unass.domain)
                multiple = False
                returned = unass
            if len(unass.domain) == smallest:
                multiple = True

    if multiple == False:
        return returned
    else:
        for unass in csp.variables:
            if not unass.is_assigned():
                if len(unass.domain) == smallest:
                    if len(csp.constraints[unass]) > largest:
                        largest = len(csp.constraints[unass])
                        returned = unass
        return returned





    # TODO implement this
    pass



def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """
    domain = variable.domain
    returned = []
    """
    print variable
    for a in csp.constraints[variable]:
        print a
    """
    for x in domain:
        returned.append(conflict_count(csp, variable,x))

    ret = sorted(returned, key=itemgetter(1))
    rett = []
    for x in ret:
        rett.append(x[0])
        
    return rett
    # TODO implement this
    pass

def conflict_count(csp, variable, val):
    count = 0
    assignment = deepcopy(variable)
    assignment.assign(val)
    for x in csp.constraints[variable]:
        for val2 in x.var2.domain:
            #print "CONSTARINT: " +str(x)
            #print "VALUES: " + str(val) + " -- " + str(val2)
            if not x.is_satisfied(val, val2):
                #print str(val)
                count += 1

    return (val, count)




