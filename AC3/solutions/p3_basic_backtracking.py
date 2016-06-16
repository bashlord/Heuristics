# -*- coding: utf-8 -*-
from p2_is_consistent import is_consistent
import sys
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'


def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
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

"""
        variable.assign(x)
        variable.is_assigned()
        if is_consistent(csp, variable, x):
            flag = 1
            for x in csp.variables:
                if x == variable:
                    x.value = variable.value
                    x.is_assigned()


    if flag == 1:
        for x in csp.variables:
            if x == variable:
                x.value = variable.value
        return True
    else:
        csp.variables.rollback()
        return False

    # TODO implement this
    pass
"""


