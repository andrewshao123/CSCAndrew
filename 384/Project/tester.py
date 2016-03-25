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

def test_5x5_plus(model, prop):
    '''
(0,0),(1,0),(2,0),(3,0),(4,0)
12+ 9+ 10+ 10+ 10+>>          
(0,1),(1,1),(2,1),(3,1),(4,1)
12+ 9+ 9+ 10+ 10+>>         
(0,2),(1,2),(2,2),(3,2),(4,2)
12+ 11+ 11+ 5+ 10+->>          
(0,3),(1,3),(2,3),(3,3),(4,3)
7+ 7+ 11+ 5+ 10+>>          
(0,4),(1,4),(2,4),(3,4),(4,4)
7+ 7+ 9+ 9+ 2+>>   
    '''
    print("Testing 5x5 empty board...", end='');
    size = 5
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(0,1),(0,2)],12,'+'],[[(1,0),(1,1),(2,1)],9,'+'],[[(2,0),(3,0),(4,0),(3,1)],10,'+'],[[(4,1),(4,2),(4,3)],10,'+'],[[(3,2),(3,3)],5,'+'],[[(1,2),(2,2),(2,3)],11,'+'],[[(0,3),(1,3),(0,4),(1,4)],7,'+'],[[(2,4),(3,4)],9,'+'],[[(4,4)],2,'+']]
    return run_csp(model, prop, size, puzzle, cage)
    
def test_5x5_plus_minus(model, prop):
    '''
(0,0),(1,0),(2,0),(3,0),(4,0)
2+ 12+ 12+ 12+ 2->>          
(0,1),(1,1),(2,1),(3,1),(4,1)
2- 11+ 11+ 8+ 2->>         
(0,2),(1,2),(2,2),(3,2),(4,2)
2- 11+ 8+ 8+ 8+>>          
(0,3),(1,3),(2,3),(3,3),(4,3)
9+ 2- 2- 3- 3->>          
(0,4),(1,4),(2,4),(3,4),(4,4)
9+ 9+ 1- 1- 5>>   
    '''
    print("Testing 5x5 empty board...", end='');
    size = 5
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0)],2,'+'],[[(1,0),(2,0),(3,0)],12,'+'],[[(4,0),(4,1)],2,'-'],[[(0,1),(0,2)],2,'-'],[[(1,1),(2,1),(1,2)],11,'+'],[[(3,1),(2,2),(3,2),(4,2)],8,'+'],[[(0,3),(0,4),(1,4)],9,'+'],[[(1,3),(2,3)],2,'-'],[[(3,3),(4,3)],3,'-'],[[(2,4),(3,4)],1,'-'],[[(4,4)],5,'+']]
    return run_csp(model, prop, size, puzzle, cage)

def test_5x5_multiply_divide(model, prop):
    '''
(0,0),(1,0),(2,0),(3,0),(4,0)
20* 20* 20* 40* 3>>          
(0,1),(1,1),(2,1),(3,1),(4,1)
20* 30* 12* 40* 40*>>         
(0,2),(1,2),(2,2),(3,2),(4,2)
30* 30* 12* 40* 10*>>          
(0,3),(1,3),(2,3),(3,3),(4,3)
2/ 2/ 60* 60* 10*>>          
(0,4),(1,4),(2,4),(3,4),(4,4)
6* 6* 6* 60* 10*>>   
    '''
    print("Testing 5x5 empty board...", end='');
    size = 5
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(1,0),(2,0),(0,1)],20,'*'],[[(3,0),(3,1),(4,1),(3,2)],40,'*'],[[(4,0)],3,'+'],[[(1,1),(1,2),(0,2)],30,'*'],[[(2,1),(2,2)],12,'*'],[[(4,2),(4,3),(4,4)],10,'*'],[[(0,3),(1,3)],2,'/'],[[(2,3),(3,3),(3,4)],60,'*'],[[(0,4),(1,4),(2,4)],6,'*']]
    return run_csp(model, prop, size, puzzle, cage)

def test_9x9_multiply_divide(model, prop):
    '''
(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0)
3/    3/    24+   24+   2-    2-    56*   56*   7-
(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)
4-    4-    24+   1-    4-    2/    2/    1     7-
(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)
11+   11+   24+   1-    4-    8*    4/    4/    12+
(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3)
5-    5-    3/    3/    2/    8*    63*   63*   12+
(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)
5-    21+   15*   15*   2/    5-    5-    17+   12+
(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5)
5-    21+   21+   15*   42*   17+   17+   17+   17+
(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)
20*   56*   56*   15*   42*   3-    17+   18*   18*
(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)
20*   20*   16+   16+   42*   3-    3-    3-    2+
(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)
8-    8-    16+   2/    2/    3/    2/    4-    4-
    '''
    print("Testing 9x9 empty board...", end='');
    size = 9
    puzzle = [([0]*size) for x in range(size)];
    cage = [[[(0,0),(1,0)],3,'/'],[[(2,0),(3,0),(2,1),(2,2)],24,'+'],[[(4,0),(5,0)],2,'-'],[[(6,0),(7,0)],56,'*'],[[(8,0),(8,1)],7,'-'],[[(0,1),(1,1)],4,'-'],[[(3,1),(3,2)],1,'-'],[[(4,1),(4,2)],4,'-'],[[(5,1),(6,1)],2,'/'],[[(7,1)],1,'+'],[[(0,2),(1,2)],11,'+'],[[(5,2),(5,3)],8,'*'],[[(6,2),(7,2)],4,'/'],[[(8,2),(8,3),(8,4)],12,'+'],[[(0,3),(1,3)],5,'-'],[[(2,3),(3,3)],3,'/'],[[(4,3),(4,4)],2,'/'],[[(6,3),(7,3)],63,'*'],[[(0,4),(0,5)],5,'-'],[[(1,4),(1,5),(2,5)],21,'+'],[[(2,4),(3,4),(3,5),(3,6)],15,'*'],[[(5,4),(6,4)],5,'-'],[[(7,4),(7,5),(8,5)],17,'+'],[[(4,5),(4,6),(4,7)],42,'*'],[[(5,5),(6,5),(6,6)],17,'+'],[[(0,6),(0,7),(1,7)],20,'*'],[[(1,6),(2,6)],56,'*'],[[(5,6),(5,7)],3,'-'],[[(7,6),(8,6)],18,'*'],[[(2,7),(3,7),(2,8)],16,'+'],[[(6,7),(7,7)],3,'-'],[[(8,7)],2,'+'],[[(0,8),(1,8)],8,'-'],[[(3,8),(4,8)],2,'/'],[[(5,8),(6,8)],3,'/'],[[(7,8),(8,8)],4,'-']]
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
    #time, variable assignments, pruned variables
    return time_difference, btracker.nDecisions, btracker.nPrunings


###################main code#####################################
models = [calcudoku_csp.calcudoku_csp_model_1, calcudoku_csp.calcudoku_csp_model_2]
propagator_types = [propagators.prop_FC,propagators.prop_GAC]

t2 = time.time()
for m in models:
    for p in propagator_types:
        info_list = []
        #info_list.append(test_1x1(m,p))
        #info_list.append(test_2x2_1(m,p))
        #info_list.append(test_2x2_2(m,p))
        
        #info_list.append(test_3x3(m,p))
        #info_list.append(test_4x4(m,p))
        #info_list.append(test_5x5(m,p))
        info_list.append(test_9x9_multiply_divide(m,p))
        #time, variable assignments, pruned variables
        
        if p == propagator_types[0] and m == models[0]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using FC
            FC_info_list_m1 = list(info_list)
            print('FC m1::::::::::::::::::::::::')          
            print(FC_info_list_m1)
        if p == propagator_types[1] and m == models[0]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using GAC
            GAC_info_list_m1 = list(info_list)
            print('GAC m1::::::::::::::::::::::::')
            print(GAC_info_list_m1)
        '''
        if p == propagator_types[2] and m == models[0]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using BT
            BT_info_list_m1 = list(info_list)
            print('BT m1::::::::::::::::::::::::')
            print(BT_info_list_m1)
        '''
        if p == propagator_types[0] and m == models[1]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using FC
            FC_info_list_m2 = list(info_list)
            print('FC m2::::::::::::::::::::::::')
            print(FC_info_list_m2)
        if p == propagator_types[1] and m == models[1]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using GAC
            GAC_info_list_m2 = list(info_list)
            print('GAC m2::::::::::::::::::::::::')
            print(GAC_info_list_m2)
        '''
        if p == propagator_types[2] and m == models[1]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using BT
            BT_time_list_m2 = list(info_list)
            print('BT m2::::::::::::::::::::::::')
            print(BT_time_list_m2)
        '''
t3 = time.time()
for_loop_difference = t3-t2
print('total time for everything is: ',for_loop_difference)
'''
t4 = time.time()
for m in models:
    for p in propagator_types:
        #order: plus only, plus&minus, multiply&divide, all four
        info_list = []
        info_list.append(test_5x5_plus(m, p))
        info_list.append(test_5x5_plus_minus(m, p))
        info_list.append(test_5x5_multiply_divide(m, p))
        info_list.append(test_5x5(m,p))
        if p == propagator_types[0] and m == models[0]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using FC
            FC_info_list_m1 = list(info_list)            
            print(FC_info_list_m1)
        if p == propagator_types[1] and m == models[0]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using GAC
            GAC_info_list_m1 = list(info_list)
            print(GAC_info_list_m1)
        #if p == propagator_types[2] and m == models[0]:
        #    #time, variable assignments, pruned variables tupple lists for 6 tests by using BT
        #    BT_info_list_m1 = list(info_list)
        #    print(BT_info_list_m1)
        if p == propagator_types[0] and m == models[1]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using FC
            FC_info_list_m2 = list(info_list)
            print(FC_info_list_m2)
        if p == propagator_types[1] and m == models[1]:
            #time, variable assignments, pruned variables tupple lists for 6 tests by using GAC
            GAC_info_list_m2 = list(info_list)
            print(GAC_info_list_m2)
        #if p == propagator_types[2] and m == models[1]:
        #    #time, variable assignments, pruned variables tupple lists for 6 tests by using BT
        #    BT_time_list_m2 = list(info_list)
        #    print(BT_time_list_m2)
t5 = time.time()
for_loop_difference = t5-t4
print('total time for operations is: ',for_loop_difference)
'''
