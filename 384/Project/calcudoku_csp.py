from cspbase import *
import itertools

str_to_op = {'*':'multiply', '+':'sum', '-':'subtract', '/':'divide'}

def multiply(args):
    product = 1
    for arg in args:
        product *= arg
    return product
    
def sum(args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
    
def subtract(args):
    args = list(args)
    args.sort()
    diff = args[-1]
    for arg in args[:-1]:
        diff -= arg
    return diff
    
def divide(args):
    args = list(args)
    args.sort()
    quot = args[-1]
    for arg in args[:-1]:
        quot /= arg
    return quot

def calcudoku_csp_model_1(initial_board, cages_array):
    '''Return a CSP object representing a Calcudoku CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_1,
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1)) 
    
    cage_array:
    [(<cage_1>), (<cage_2>) , ...], 
    where <cage_i> = [positions, result, operation],
    positions = [p1,p2,...] where the pi = (xi,yi) (counting from the top left) are the cell positions of a cage
    result = <int>, the value that the cage's operation should result in
    operation = <str>, the string literal representing the operation of the cage

    inital_board: Specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.
    '''
    
    # INITIALIZE VARIABLES AND CONSTRAINTS
    n = len(initial_board) # Size of initial calcudoku board
    dom_all = [a+1 for a in range(n)] # Domain of unassigned variable
    cons = [] # Constraints list
    variable_array = [[] for i in range(n)] # Create empty nxn array
    
    for i in range(n): # Construct variable_array based on whether variable is initially assigned
        for j in range(n):
            variable_array[i].append(Variable('V{},{}'.format(i,j), dom_all if initial_board[i][j] == 0 else [initial_board[i][j]])) # Initialize vars
            
    # BUILD NOT-EQUAL CONSTRAINTS
    r_c = 0
    variable_array_T = [[variable_array[j][i] for j in range(n)] for i in range(n)] # Compute transpose of variable_array
    var_zipped = zip(variable_array,variable_array_T) # Zip variable_array and its transpose for parallel constructions of row/column constraints
    for row,col in var_zipped: # Iterate over rows and columns of variable_array in parallel
        for i in range(n): # Iterate over all possible pairs of variables in row/column
            for j in range(i+1,n):
                for k in range(2): # If k == 0, construct column constraint, else construct row constraint
                    row_col,v1_row,v1_col,v2_row,v2_col = (row,r_c,i,r_c,j) if k else (col,i,r_c,j,r_c)
                    con = Constraint('C(V{},{},V{},{})'.format(v1_row,v1_col,v2_row,v2_col), [row_col[i], row_col[j]]) # Create constraint
                    sat_tuples = [] # Initialize satisfying tuples
                    dom_v1 = row_col[i].domain() # Domain of first variable
                    dom_v2 = row_col[j].domain() # Domain of second variable
                    for t in itertools.product(dom_v1, dom_v2): # Iterate over all possible domain pairs of both variables to construct sat_tuples
                        if t[0] != t[1]: # Append t if not-equal constraint satisfied
                            sat_tuples.append(t)
                    con.add_satisfying_tuples(sat_tuples)
                    cons.append(con) # Append current constraint to list of constraints
        r_c += 1
        
    # BUILD CAGE CONSTRAINTS
    i = 0
    for cage in cages_array: # Iterate over all cages
        doms = [] # Initialize current cage's domain
        vars = [] # Initialize current list of variables within current cage
        for pos in cage[0]: # Iterate over variable positions held in cage
            x, y = pos # Get x and y positions of current variable of cage
            var = variable_array[x][y]
            doms.append(var.domain()) # Append domain list of current variable to doms list
            vars.append(var) # Append variable to current list of variables
        con = Constraint('C(C{})'.format(i), vars) # Initialize constraint for current cage
        sat_tuples = [] # Initialize satisfying tuples for current constraint
        for t in itertools.product(*doms): # Iterate over all possible combinations of variables in cage
            if globals()[str_to_op[cage[2]]](t) == cage[1]: # Check if constraint is matched by current assignments to variables
                sat_tuples.append(t)
        con.add_satisfying_tuples(sat_tuples) # Add satisfying tuples to current constraint
        cons.append(con) # Append constraint to list of constraints
        i += 1
        
    vars = [row[i] for row in variable_array for i in range(n)] # List of variable objects for csp
    calcudoku_csp = CSP('Calcudoku', vars) # Create futoshiki_csp object
    for c in cons: # Add all constraints to futoshiki_csp
        calcudoku_csp.add_constraint(c)
    
    return calcudoku_csp, variable_array

def calcudoku_csp_model_2(initial_board, cages_array):
    '''Return a CSP object representing a Calcudoku CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_1,
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1)) 
    
    cage_array:
    [(<cage_1>), (<cage_2>) , ...], 
    where <cage_i> = [positions, result, operation],
    positions = [p1,p2,...] where the pi = (xi,yi) (counting from the top left) are the cell positions of a cage
    result = <int>, the value that the cage's operation should result in
    operation = <str>, the string literal representing the operation of the cage

    inital_board: Specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.
    '''
    
    # INITIALIZE VARIABLES AND CONSTRAINTS
    n = len(initial_board) # Size of initial calcudoku board
    dom_all = [a+1 for a in range(n)] # Domain of unassigned variable
    cons = [] # Constraints list
    variable_array = [[] for i in range(n)] # Create empty nxn array
    
    for i in range(n): # Construct variable_array based on whether variable is initially assigned
        for j in range(n):
            variable_array[i].append(Variable('V{},{}'.format(i,j), dom_all if initial_board[i][j] == 0 else [initial_board[i][j]])) # Initialize vars
            
    #BUILD ALL-DIFFERENT CONSTRAINTS
    r_c = 0
    variable_array_T = [[variable_array[j][i] for j in range(n)] for i in range(n)] # Compute transpose of variable_array
    var_zipped = zip(variable_array,variable_array_T) # Zip variable_array and its transpose for parallel constructions of row/column constraints
    for row,col in var_zipped: # Iterate over rows and columns of variable_array in parallel
        for k in range(2): # If k == 0, construct column constraint, else construct row constraint
            row_col,R_C = (row,'R') if k else (col,'C')
            con = Constraint('C({}{})'.format(R_C,r_c), [row_col[i] for i in range(n)]) # Create constraint object
            sat_tuples = [] # Initialize satisfying tuples
            doms = [row_col[i].domain() for i in range(n)] # Create list of domain lists for each variable in row/column
            for t in itertools.product(*doms): # Iterate over all combinations of all n variables
                if len(set(t)) == len(t): # Append t if all-different constraint satisfied
                    sat_tuples.append(t)
            con.add_satisfying_tuples(sat_tuples)
            cons.append(con)
        r_c += 1
        
    # BUILD CAGE CONSTRAINTS
    i = 0
    for cage in cages_array: # Iterate over all cages
        doms = [] # Initialize current cage's domain
        vars = [] # Initialize current list of variables within current cage
        for pos in cage[0]: # Iterate over variable positions held in cage
            x, y = pos # Get x and y positions of current variable of cage
            var = variable_array[x][y]
            doms.append(var.domain()) # Append domain list of current variable to doms list
            vars.append(var) # Append variable to current list of variables
        con = Constraint('C(C{})'.format(i), vars) # Initialize constraint for current cage
        sat_tuples = [] # Initialize satisfying tuples for current constraint
        for t in itertools.product(*doms): # Iterate over all possible combinations of variables in cage
            if globals()[str_to_op[cage[2]]](t) == cage[1]: # Check if constraint is matched by current assignments to variables
                sat_tuples.append(t)
        con.add_satisfying_tuples(sat_tuples) # Add satisfying tuples to current constraint
        cons.append(con) # Append constraint to list of constraints
        i += 1
        
    vars = [row[i] for row in variable_array for i in range(n)] # List of variable objects for csp
    calcudoku_csp = CSP('Calcudoku', vars) # Create futoshiki_csp object
    for c in cons: # Add all constraints to futoshiki_csp
        calcudoku_csp.add_constraint(c)
    
    return calcudoku_csp, variable_array
