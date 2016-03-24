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
    return run_csp(model, prop, size, puzzle, cage)
    
    
def test_2x2_1(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    size = 2
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1)],3,'+'],[[(1,0),(1,1)],1,'-']]
    size = 2
    return run_csp(model, prop, size, puzzle, cage)
    
def test_2x2_2(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    size = 2
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1)],2,'*'],[[(1,0),(1,1)],2,'/']]
    size = 2
    return run_csp(model, prop, size, puzzle, cage)

def test_2x2_3(model, prop):
    '''
    3 1>>1 2
    3 1>>2 1
    '''
    print("Testing 2x2 empty board...", end='');
    size = 2
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1)],3,'*'],[[(1,0),(1,1)],3,'/']]
    size = 2
    return run_csp(model, prop, size, puzzle, cage)

def test_3x3(model, prop):
    '''
    (0,0) (1,0) (2,0)
    2- 2- 2+>>
    (0,1) (1,1) (2,1)
    2/ 3/ 3/>>
    (0,2) (1,2) (2,2)
    2/ 1- 1->>
    '''
    print("Testing 3x3 empty board...", end='');
    size = 3
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(1,0)],2,'-'],[[(2,0)],2,'+'],[[(0,1),(0,2)],2,'/'],[[(1,1),(2,1)],3,'/'],[[(1,2),(2,2)],1,'-']]
    return run_csp(model, prop, size, puzzle, cage)

def test_4x4(model, prop):
    '''
    (0,0) (1,0) (2,0) (3,0)
    4+ 2/ 2/ 12x>> 1 2 4 3
    (0,1) (1,1) (2,1) (3,1)
    4+ 3- 6+ 12x>>3 1 2 4
    (0,2) (1,2) (2,2) (3,2)
    2+ 3- 6+ 6+ >>2 4 3 1
    (0,3) (1,3) (2,3) (3,3)
    7+ 7+ 2/ 2/ >>4 3 1 2
    '''
    print("Testing 4x4 empty board...", end='');
    size = 4
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1)],4,'+'],[[(1,0),(2,0)],2,'/'],[[(3,0),(3,1)],12,'*'],[[(1,1),(1,2)],3,'-'],[[(2,1),(2,2),(3,2)],6,'+'],[[(0,3),(1,3)],7,'+'],[[(2,3),(3,3)],2,'/']]
    return run_csp(model, prop, size, puzzle, cage)

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
    return run_csp(model, prop, size, puzzle, cage)
    

def run_csp(model, prop, size, puzzle, cage):
    csp, vars_array = model(puzzle,cage);

    if len(csp.vars) != size*size:
        return "Incorrect number of variables in csp";
    t0 = time.time()

    btracker = BT(csp)
    btracker.bt_search(prop);

    t1 = time.time()
    time_difference = t1-t0


    #print(time_difference)

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
    print('passed!')
    print('The time difference for {} and {} is:'.format(model, prop))
    print(time_difference)
    return time_difference


###################main code#####################################
models = [calcudoku_csp.calcudoku_csp_model_1, calcudoku_csp.calcudoku_csp_model_2]
propagator_types = [propagators.prop_FC,propagators.prop_GAC, propagators.prop_BT]
for m in models:
    time_list = []
    for p in propagator_types:
        time_list.append(test_1x1(m,p))
        time_list.append(test_2x2_1(m,p))
        time_list.append(test_2x2_2(m,p))
        #time_list.append(test_2x2_3(m,p))
        time_list.append(test_3x3(m,p))
        time_list.append(test_4x4(m,p))
        time_list.append(test_5x5(m,p))
        if p == propagator_types[0] and m == models[0]:
            FC_time_list_m1 = time_listS
            
            print(FC_time_list_m1)
        if p == propagator_types[1] and m == models[0]:
            GAC_time_list_m1 = time_list
            print(GAC_time_list_m1)
        if p == propagator_types[2] and m == models[0]:
            BT_time_list_m1 = time_list
            print(BT_time_list_m1)
        if p == propagator_types[0] and m == models[1]:
            FC_time_list_m2 = time_list
            print(FC_time_list_m2)
        if p == propagator_types[1] and m == models[1]:
            GAC_time_list_m2 = time_list
            print(GAC_time_list_m2)
        if p == propagator_types[2] and m == models[1]:
            BT_time_list_m2 = time_list
            print(BT_time_list_m2)
