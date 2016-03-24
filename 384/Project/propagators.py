from collections import deque

#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
This file will contain different constraint propagators to be used within
bt_search.

propagator == a function with the following template
    propagator(csp, newly_instantiated_variable=None)
        ==> returns (True/False, [(Variable, Value), (Variable, Value) ...])

    csp is a CSP object---the propagator can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    newly_instaniated_variable is an optional argument.
    if newly_instantiated_variable is not None:
        then newly_instantiated_variable is the most
        recently assigned variable of the search.
    else:
        propagator is called before any assignments are made
        in which case it must decide what processing to do
        prior to any variables being assigned. SEE BELOW

    The propagator returns True/False and a list of (Variable, Value) pairs.

    Returns False if a deadend has been detected by the propagator.
        in this case bt_search will backtrack
    Returns True if we can continue.

    The list of variable values pairs are all of the values
    the propagator pruned (using the variable's prune_value method).
    bt_search NEEDS to know this in order to correctly restore these
    values when it undoes a variable assignment.

    NOTE propagator SHOULD NOT prune a value that has already been
    pruned! Nor should it prune a value twice

    PROPAGATOR called with newly_instantiated_variable = None
        PROCESSING REQUIRED:
            for plain backtracking (where we only check fully instantiated
            constraints) we do nothing...return (true, [])

            for forward checking (where we only check constraints with one
            remaining variable) we look for unary constraints of the csp
            (constraints whose scope contains only one variable) and we
            forward_check these constraints.

            for gac we establish initial GAC by initializing the GAC queue with
            all constaints of the csp

    PROPAGATOR called with newly_instantiated_variable = a variable V
        PROCESSING REQUIRED:
            for plain backtracking we check all constraints with V (see csp
            method get_cons_with_var) that are fully assigned.

            for forward checking we forward check all constraints with V that
            have one unassigned variable left

            for gac we initialize the GAC queue with all constraints containing
            V.
'''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar): # Iterate through each constraint c such that newVar is a variable of c
        if c.get_n_unasgn() == 0: # All of the other variables in constraint c's scope must be assigned
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking.  That is, check constraints with only one
    uninstantiated variable, and prune appropriately.  (i.e., do not prune a
    value that has already been pruned; do not prune the same value twice.)
    Return if a deadend has been detected, and return the variable/value pairs
    that have been pruned.  See beginning of this file for complete description
    of what propagator functions should take as input and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to
        access the variables and constraints.

        newVar is an optional argument.
        if newVar is not None:
            then newVar is the most recently assigned variable of the search.
            run FC on all constraints that contain newVar.
        else:
            propagator is called before any assignments are made in which case
            it must decide what processing to do prior to any variable
            assignment.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

        boolean is False if a deadend has been detected, and True otherwise.

        list is a set of variable/value pairs that are all of the values the
        propagator pruned.
    '''

#IMPLEMENT
    prunings = []

    # If newVar is None, forward check all constraints. Else, if newVar=var only check constraints containing newVar   
    if not newVar:
        cons_list = csp.get_all_cons()
    else:
        cons_list = csp.get_cons_with_var(newVar)
        
    for c in cons_list:
        if c.get_n_unasgn() == 1: # Constraint c must contain only one uninstantiated variable
            x = c.get_unasgn_vars()[0] # Get the one unassigned variable of c
            
            vals = []
            for var in c.get_scope(): # Build list of c's assigned variable values, including the unassigned variable value (= None)
                vals.append(var.get_assigned_value())
            unasgn_index = vals.index(None) # Index of unassigned variable
            
            for d in x.cur_domain(): # Iterate over unassigned variable's current domain
                vals[unasgn_index] = d # Propagate unassigned variable's assignment
                
                if not c.check(vals): # Check if unassigned variable's propagated variable assignment satisfies c
                    x.prune_value(d) # Prune propagated value if constraint isn't satisfied by propagated variable assignment
                    prunings.append((x, d))
                
            if x.cur_domain_size() == 0: # Check if DWO occured
                return False, prunings
                        
    return True, prunings

def prop_GAC(csp, newVar=None):
    '''Do GAC propagation, as described in lecture. See beginning of this file
    for complete description of what propagator functions should take as input
    and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to access the variables
        and constraints.

        newVar is an optional argument.
        if newVar is not None:
            do GAC enforce with constraints containing newVar on the GAC queue.
        else:
            Do initial GAC enforce, processing all constraints.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

    boolean is False if a deadend has been detected, and True otherwise.

    list is a set of variable/value pairs that are all of the values the
    propagator pruned.
    '''

#IMPLEMENT
    GACQueue = deque()
    prunings = []

    # If newVar is None, forward check all constraints. Else, if newVar=var only check constraints containing newVar   
    if not newVar:
        cons_list = csp.get_all_cons()
    else:
        cons_list = csp.get_cons_with_var(newVar)
        
    for c in cons_list: # Build GACQueue
        GACQueue.append(c)
        
    while GACQueue: # Enforce GAC while GACQueue is not empty
        c = GACQueue.pop() # Extract constraint c fom GACQueue
        
        for var in c.get_scope():
            for d in var.cur_domain():
                if not c.has_support(var, d): # Find an assignment A for all other variables in scope(C) such that C(A ∪ var=d) is True
                    var.prune_value(d)
                    prunings.append((var, d))
                    
                    if var.cur_domain_size() == 0: # Check if DWO occurred
                        GACQueue.clear() # Empty queue
                        return False, prunings
                    else:
                        for cons in csp.get_cons_with_var(var): # Iterate through all constraints with var in scope
                            if not cons in GACQueue and cons.name != c.name: # Only push constraints not c and not already in GACQueue
                                GACQueue.append(cons)
    return True, prunings