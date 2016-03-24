#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
Construct and return Futoshiki CSP models.
'''

from cspbase import *
import itertools

def futoshiki_csp_model_1(initial_futoshiki_board):
    '''Return a CSP object representing a Futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_1 and
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


    The input board is specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.

    Each list is of length 2n-1, with each space on the board being separated
    by the potential inequality constraints. '>' denotes that the previous
    space must be bigger than the next space; '<' denotes that the previous
    space must be smaller than the next; '.' denotes that there is no
    inequality constraint.

    E.g., the board

    -------------------
    | > |2| |9| | |6| |
    | |4| | | |1| | |8|
    | |7| <4|2| | | |3|
    |5| | | | | |3| | |
    | | |1| |6| |5| | |
    | | <3| | | | | |6|
    |1| | | |5|7| |4| |
    |6> | |9| < | |2| |
    | |2| | |8| <1| | |
    -------------------
    would be represented by the list of lists

    [[0,'>',0,'.',2,'.',0,'.',9,'.',0,'.',0,'.',6,'.',0],
     [0,'.',4,'.',0,'.',0,'.',0,'.',1,'.',0,'.',0,'.',8],
     [0,'.',7,'.',0,'<',4,'.',2,'.',0,'.',0,'.',0,'.',3],
     [5,'.',0,'.',0,'.',0,'.',0,'.',0,'.',3,'.',0,'.',0],
     [0,'.',0,'.',1,'.',0,'.',6,'.',0,'.',5,'.',0,'.',0],
     [0,'.',0,'<',3,'.',0,'.',0,'.',0,'.',0,'.',0,'.',6],
     [1,'.',0,'.',0,'.',0,'.',5,'.',7,'.',0,'.',4,'.',0],
     [6,'>',0,'.',0,'.',9,'.',0,'<',0,'.',0,'.',2,'.',0],
     [0,'.',2,'.',0,'.',0,'.',8,'.',0,'<',1,'.',0,'.',0]]


    This routine returns Model_1 which consists of a variable for each cell of
    the board, with domain equal to [1,...,n] if the board has a 0 at that
    position, and domain equal [i] if the board has a fixed number i at that
    cell.

    Model_1 also contains BINARY CONSTRAINTS OF NOT-EQUAL between all relevant
    variables (e.g., all pairs of variables in the same row, etc.).

    All of the constraints of Model_1 MUST BE binary constraints (i.e.,
    constraints whose scope includes two and only two variables).
    '''

#IMPLEMENT

    n = len(initial_futoshiki_board) # Size of initial futoshiki board
    dom_all = [a+1 for a in range(n)] # Domain of unassigned variable
    num_array = []
    ineq_array = []
    cons = []
    variable_array = [[] for i in range(n)] # Create empty nxn array
    
    for row in initial_futoshiki_board: # Build num_array and ineq_array
        num_array.append(row[::2]) # Append even columns (variables integer values)
        ineq_array.append(row[1::2]) # Append odd columns (constraint characters)
        
    for i in range(n): # Construct variable_array based on whether variable is initially assigned
        for j in range(n):
            variable_array[i].append(Variable('V{},{}'.format(i,j), dom_all if num_array[i][j] == 0 else [num_array[i][j]]))
    
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
                    for t in itertools.product(dom_v1, dom_v2): # Iterate over all possible domain pairs of both variables
                        if t[0] != t[1]: # Append t if not-equal constraint satisfied
                            sat_tuples.append(t)
                    con.add_satisfying_tuples(sat_tuples)
                    cons.append(con)
        r_c += 1
       
    #BUILD INEQUALITY CONSTRAINTS
    r = 0
    var_ineq_zipped = zip(variable_array, ineq_array)
    for row_var,row_ineq in var_ineq_zipped:
        for i in range(n-1): # Iterate over all inequality constraints
            if row_ineq[i] == '.':
                continue
                
            con = Constraint('C(V{},{},V{},{})'.format(r,i,r,i+1), [row_var[i], row_var[i+1]])
            sat_tuples = []
            dom_v1 = row_var[i].domain()
            dom_v2 = row_var[i+1].domain()
            for t in itertools.product(dom_v1, dom_v2): # Iterate over all possible domain pairs of both variables
                if (row_ineq[i] == '<' and t[0] < t[1]) or (row_ineq[i] == '>' and t[0] > t[1]): # Append t if inequality constraint satisfied
                    sat_tuples.append(t)
            con.add_satisfying_tuples(sat_tuples)
            cons.append(con)
        r += 1
        
    vars = [row[i] for row in variable_array for i in range(n)] # List of variable objects for csp
    futoshiki_csp = CSP('Futoshiki-M1', vars) # Create futoshiki_csp object
    for c in cons: # Add all constraints to futoshiki_csp
        futoshiki_csp.add_constraint(c)
    
    return futoshiki_csp, variable_array
    
##############################

def futoshiki_csp_model_2(initial_futoshiki_board):
    '''Return a CSP object representing a futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_2 and
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

    The input board takes the same input format (a list of n lists of size 2n-1
    specifying the board) as futoshiki_csp_model_1.

    The variables of Model_2 are the same as for Model_1: a variable for each
    cell of the board, with domain equal to [1,...,n] if the board has a 0 at
    that position, and domain equal [i] if the board has a fixed number i at
    that cell.

    However, Model_2 has different constraints. In particular, instead of
    binary non-equals constaints Model_2 has 2*n all-different constraints:
    all-different constraints for the variables in each of the n rows, and n
    columns. Each of these constraints is over n-variables (some of these
    variables will have a single value in their domain). Model_2 should create
    these all-different constraints between the relevant variables, and then
    separately generate the appropriate binary inequality constraints as
    required by the board. There should be j of these constraints, where j is
    the number of inequality symbols found on the board.  
    '''

#IMPLEMENT

    n = len(initial_futoshiki_board) # Size of initial futoshiki board
    dom_all = [a+1 for a in range(n)] # Domain of unassigned variable
    num_array = []
    ineq_array = []
    cons = []
    variable_array = [[] for i in range(n)] # Create empty nxn array
    
    for row in initial_futoshiki_board: # Build num_array and ineq_array
        num_array.append(row[::2]) # Append even columns (variables integer values)
        ineq_array.append(row[1::2]) # Append odd columns (constraint characters)
        
    for i in range(n): # Construct variable_array based on whether variable is initially assigned
        for j in range(n):
            variable_array[i].append(Variable('V{},{}'.format(i,j), dom_all if num_array[i][j] == 0 else [num_array[i][j]]))
    
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
            
    
    #BUILD INEQUALITY CONSTRAINTS
    r = 0
    var_ineq_zipped = zip(variable_array, ineq_array)
    for row_var,row_ineq in var_ineq_zipped:
        for i in range(n-1): # Iterate over all inequality constraints
            if row_ineq[i] == '.':
                continue
                
            con = Constraint('C(V{},{},V{},{})'.format(r,i,r,i+1), [row_var[i], row_var[i+1]])
            sat_tuples = []
            dom_v1 = row_var[i].domain()
            dom_v2 = row_var[i+1].domain()
            for t in itertools.product(dom_v1, dom_v2): # Iterate over all possible domain pairs of both variables
                if (row_ineq[i] == '<' and t[0] < t[1]) or (row_ineq[i] == '>' and t[0] > t[1]): # Append t if inequality constraint satisfied
                    sat_tuples.append(t)
            con.add_satisfying_tuples(sat_tuples)
            cons.append(con)
        r += 1
        
    vars = [row[i] for row in variable_array for i in range(n)] # List of variable objects for csp
    futoshiki_csp = CSP('Futoshiki-M2', vars) # Create futoshiki_csp object
    for c in cons: # Add all constraints to futoshiki_csp
        futoshiki_csp.add_constraint(c)
    
    return futoshiki_csp, variable_array