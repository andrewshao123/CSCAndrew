from __future__ import print_function;
import random; rse = "print('NopeNopeNope')"; random.seed(rse);
from cspbase import *
import propagators;
import calcudoku_csp;
import time

propagators.prop_BT
propagators.prop_FC
propagators.prop_GAC

def test_1x1(model,prop):
    print("Testing 1x1 board with given number...", end='');
    size = 1
    puzzle = [[0]];
    cage = [[[(0,0)],1,'+']]
    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
        
    btracker = BT(csp)
    btracker.bt_search(prop);
    
    for row in vars_array:
        assigned = [v.get_assigned_value() for v in row];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, row uniqueness violated";
    for j in range(size):
        assigned = [];
        for i in range(size):
            assigned += [vars_array[j][i].get_assigned_value()];
        for i in range(1,size+1):

            if i not in assigned:

                return "Invalid assignment, column uniqueness violated";

    constraints = []
    constraints = list(csp.get_all_cons())
    for c in constraints:
        assigned = [v.get_assigned_value() for row in vars_array for v in row if v in c.get_scope()]
        if not c.check(assigned):
            return "Violated constraint"

    return "Passed";
    
    
def test_2x2_1(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    puzzle = [[0,0],[0,0]];
    cage = [[[(0,0),(0,1)],3,'+'],[[(1,0),(1,1)],1,'-']]
    size = 2
    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
        
    btracker = BT(csp)
    btracker.bt_search(prop);
    
    for row in vars_array:
        assigned = [v.get_assigned_value() for v in row];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, row uniqueness violated";
    for j in range(size):
        assigned = [];
        for i in range(size):
            assigned += [vars_array[j][i].get_assigned_value()];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, column uniqueness violated";

    constraints = []
    constraints = list(csp.get_all_cons())
    for c in constraints:
        assigned = [v.get_assigned_value() for row in vars_array for v in row if v in c.get_scope()]
        if not c.check(assigned):
            return "Violated constraint"

    return "Passed";
    
def test_2x2_2(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    puzzle = [[0,0],[0,0]];
    cage = [[[(0,0),(0,1)],2,'*'],[[(1,0),(1,1)],2,'/']]
    size = 2
    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
        
    btracker = BT(csp)
    btracker.bt_search(prop);
    
    for row in vars_array:
        assigned = [v.get_assigned_value() for v in row];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, row uniqueness violated";
    for j in range(size):
        assigned = [];
        for i in range(size):
            assigned += [vars_array[j][i].get_assigned_value()];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, column uniqueness violated";

    constraints = []
    constraints = list(csp.get_all_cons())
    for c in constraints:
        assigned = [v.get_assigned_value() for row in vars_array for v in row if v in c.get_scope()]
        if not c.check(assigned):
            return "Violated constraint"

    return "Passed";

def test_2x2_3(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    puzzle = [[0,0],[0,0]];
    cage = [[[(0,0),(0,1)],3,'*'],[[(1,0),(1,1)],3,'/']]
    size = 2
    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
        
    btracker = BT(csp)
    btracker.bt_search(prop);
    
    for row in vars_array:
        assigned = [v.get_assigned_value() for v in row];
        if None in assigned:
            print(assigned)
            return "No Solution"
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, row uniqueness violated";
    for j in range(size):
        assigned = [];
        for i in range(size):
            assigned += [vars_array[j][i].get_assigned_value()];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, column uniqueness violated";

    constraints = []
    constraints = list(csp.get_all_cons())
    for c in constraints:
        assigned = [v.get_assigned_value() for row in vars_array for v in row if v in c.get_scope()]
        if not c.check(assigned):
            return "Violated constraint"

    return "Passed";


def test_5x5(model, prop):
    '''
(0,0),(1,0),(2,0),(3,0),(4,0)
36x 6+ 6+ 11+ 11+>>          3 4 2 5 1
(0,1),(1,1),(2,1),(3,1),(4,1)
36x 36x 3+ 3+ 11+>>          4 3 1 2 5
(0,2),(1,2),(2,2),(3,2),(4,2)
10x 2/ 11+ 11+ 1->>          5 1 4 3 2
(0,3),(1,3),(2,3),(3,3),(4,3)
10x 2/ 75x 11+ 1->>          1 2 5 4 3
(0,4),(1,4),(2,4),(3,4),(4,4)
10x 75x 75x 4x 4x>>          2 5 3 1 4
    '''
    print("Testing 5x5 empty board...", end='');
    size = 5
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1),(1,1)],36,'*'],[[(1,0),(2,0)],6,'+'],[[(3,0),(4,0),(4,1)],11,'+'],[[(2,1),(3,1)],3,'+'],[[(0,2),(0,3),(0,4)],10,'*'],[[(1,2),(1,3)],2,'/'],[[(2,2),(3,2),(3,3)],11,'+'],[[(4,2),(4,3)],1,'-'],[[(1,4),(2,4),(2,3)],75,'*'],[[(3,4),(4,4)],4,'*']]

    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
    t0 = time.time()
    btracker = BT(csp)
    btracker.bt_search(prop);
    t1 = time.time()
    time_difference = t1-t0
    print('The time difference for {} is:'.format(prop))
    print(time_difference)
    for row in vars_array:
        assigned = [v.get_assigned_value() for v in row];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, row uniqueness violated";
    for j in range(size):
        assigned = [];
        for i in range(size):
            assigned += [vars_array[j][i].get_assigned_value()];
        for i in range(1,size+1):
            if i not in assigned:
                return "Invalid assignment, column uniqueness violated";

    constraints = []
    constraints = list(csp.get_all_cons())
    for c in constraints:
        assigned = [v.get_assigned_value() for row in vars_array for v in row if v in c.get_scope()]
        if not c.check(assigned):
            return "Violated constraint"

    return "Passed"


###################main code#####################################
models = [calcudoku_csp.calcudoku_csp_model_1, calcudoku_csp.calcudoku_csp_model_2]
#propagators.prop_BT
#propagators.prop_FC
#propagators.prop_GAC
#print(test_1x1(m))
#print(test_2x2_1(m))
#print(test_2x2_2(m,propagators.prop_BT))
#print(test_2x2_3(m))
for m in models:
    for p in [propagators.prop_FC]:
        test_5x5(m,p)
'''
for p in (propagators.prop_FC, propagators.prop_GAC):
    for (m = calcudoku_csp.calcudoku_csp_model, calcudoku_csp.calcudoku_csp_model):
        print("Model " + m.__name__);
        print("===========================");
        #print(test_1x1(m));
        #print(test_2x2_1(m));
        #print(test_2x2_2(m));
        print(test_5x5(m));
        # Be careful1! test_with_constraints doesn't actually know if there is a solution or not!
        # If your model/propogator returns a solution, then it checks if the solution is valid
        # Otherwise it just says CSP not solved
        # I have annotated the test cases that I found should be unsolvable (insoluable?).
        ## Execute one line at a time and check console
        
        print(test_with_constraints(m, p)); # Should be solvable
        print(test_with_constraints(m, p, size=3, num_constraints=3)); # Probably solvable
        print(test_with_constraints(m, p, size=2, num_constraints=2), "\nThe line above should say indeterminate ^^"); # Should not be solvable
        print(test_with_constraints(m, p, size=2, num_givens=2, num_constraints=0)); # Solvable
        print(test_with_constraints(m, p, size=4, num_constraints=3)); # Solvable
        print(test_with_constraints(m, p, size=5, num_givens=4, num_constraints=3)); # Solvable
        print(test_with_constraints(m, p, size=7, num_givens=4, num_constraints=15)); # Solvable
        print("\n");
'''
