#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.

'''
rushhour STATESPACE
'''
#   You may add only standard python imports---i.e., ones that are automatically
#   available on CDF.
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

from search import *
from random import randint

##################################################
# The search space class 'rushhour'             #
# This class is a sub-class of 'StateSpace'      #
##################################################

	
class rushhour(StateSpace):
    def __init__(self, action, gval, vehicle_statues, board_properties, parent = None):
	#IMPLEMENT
        """Initialize a rushhour search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.vehicle_statues = get_vehicle_statuses(self)
	self.board_properties = get_board_properties(self)

    def successors(self):
#IMPLEMENT
        '''Return list of rushhour objects that are the successors of the current object'''
        States = list()
        board = [[' ' for x in range(self.board_properties[0][0])] for x in range(self.board_properties[0][1])]
        print(board)
	for v in self.vehicle_statues:
            cut_counter = 0
            if v[3] == True:#is_horizontal = True
                for i in range(v[2]):#v_length
                    if v[1][0]+i <= board_properties[0][0]-1:#BE CAREFUL, ON BOARD DOUBLE LIST X AND Y ARE OPPOSITE
                        board[v[1][1]][v[1][0]+i] = v[0]
                    else:
                        board[v[1][1]][0+cut_counter] = v[0]
                        cut_counter = cut_counter + 1
            else: #is_horizontal = False
                for i in range(v[2]):#v_length
                    if v[1][1]+i <= board_properties[0][1]-1:
                        board[v[1][1]+i][v[1][0]] = v[0]
                    else:
                        board[0+cut_counter][v[1][0]] = v[0]
                        cut_counter = cut_counter + 1
    
        for v in self.vehicle_statues:
            index = 0
            v_x = v[1][0]
            v_y = v[1][1]
            board_xedge = self.board_properties[0][0]
            board_yedge = self.board_properties[0][1]
            if v[3] == True: #if the vehicle is horizontal
                if board[v_y][(v_x-1)%(board_xedge)] == ' ':
                    new_vehicle_statues = [v[0], (((v_x-1)%(board_xedge)),v_y), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',W)', self.gval +1, new_vehicle_statues, self.board_properties))

                if board[v_y][(v_x+1)%(board_xedge)] == ' ':
                    new_vehicle_statues = [v[0], ((v_x+1)%(board_xedge),v_y), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',E)', self.gval +1, new_vehicle_statues, self.board_properties))

            else: #if the vehicle is vertical
                if board[(v_y - 1)%(board_yedge)][v_x] == ' ':
                    new_vehicle_statues = [v[0], (v_x,(v_y-1)%(board_yedge)), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',N)', self.gval +1, new_vehicle_statues, self.board_properties))

                if board[(v_y + 1)%(board_yedge)][v_x] == ' ':
                    new_vehicle_statues = [v[0], (v_x,(v_y+1)%(board_yedge)), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',S)', self.gval +1, new_vehicle_statues, self.board_properties))

            index = index +1
        return States

"""
            if v[3] == True: #if the vehicle is horizontal
                if v_x - 1 >= 0 and board[v_y][v_x-1] == ' ':
                    new_vehicle_statues = [v[0], (v_x-1,v_y), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',W)', self.gval +1, new_vehicle_statues, self.board_properties))
                if v_x - 1 < 0 and board[v_y][board_xedge-1] == ' ':#board[y][x]
                    new_vehicle_statues = [v[0], (board_xedge-1,v_y), v[2], v[3], v[4]] #board_properties[0][0]-1 board x edge
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',W)', self.gval +1, new_vehicle_statues, self.board_properties))

                if v_x + 1 <= (board_xedge - 1) and board[v_y][v_x+1] == ' ':
                    new_vehicle_statues = [v[0], (v_x+1,v_y), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',E)', self.gval +1, new_vehicle_statues, self.board_properties))
                if v_x + 1 > (board_xedge - 1) and board[v_y][board_xedge-1] == ' ':#board[y][x]
                    new_vehicle_statues = [v[0], (board_xedge - 1,v_y), v[2], v[3], v[4]] #board_properties[0][0]-1 board x edge
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',E)', self.gval +1, new_vehicle_statues, self.board_properties))

            else: #if the vehicle is vertical
                if v_y - 1 >= 0 and board[v_y - 1][v_x] == ' ':
                    new_vehicle_statues = [v[0], (v_x,v_y-1), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',N)', self.gval +1, new_vehicle_statues, self.board_properties))
                if v_y - 1 < 0 and board[board_yedge-1][v_x] == ' ':#board[y][x]
                    new_vehicle_statues = [v[0], (v_x,board_yedge-1), v[2], v[3], v[4]] #board_properties[0][0]-1 board x edge
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',N)', self.gval +1, new_vehicle_statues, self.board_properties))

                if v_y + 1 <= (board_yedge - 1) and board[v_y+1][v_x] == ' ':
                    new_vehicle_statues = [v[0], (v_x,v_y+1), v[2], v[3], v[4]]
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',S)', self.gval +1, new_vehicle_statues, self.board_properties))
                if v_y + 1 > (board_yedge - 1) and board[board_yedge-1][v_x] == ' ':#board[y][x]
                    new_vehicle_statues = [v[0], (v_x,board_yedge-1), v[2], v[3], v[4]] #board_properties[0][0]-1 board x edge
                    self.vehicle_statues[index] = new_vehicle_statues
                    States.append(rushhour('move_vehicle('+v[0]+',S)', self.gval +1, new_vehicle_statues, self.board_properties))"""

    def hashable_state(self):
#IMPLEMENT
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        return (self.vehicle_statues, self.board_properties)

    def print_state(self):
        #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
        #and in generating sample trace output.
        #Note that if you implement the "get" routines
        #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
        #properly, this function should work irrespective of how you represent
        #your state.

        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))

        print("Vehicle Statuses")
        for vs in sorted(self.get_vehicle_statuses()):
            print("    {} is at ({}, {})".format(vs[0], vs[1][0], vs[1][1]), end="")
        board = get_board(self.get_vehicle_statuses(), self.get_board_properties())
        print('\n')
        print('\n'.join([''.join(board[i]) for i in range(len(board))]))

#Data accessor routines.

    def get_vehicle_statuses(self):
#IMPLEMENT
        '''Return list containing the status of each vehicle
           This list has to be in the format: [vs_1, vs_2, ..., vs_k]
           with one status list for each vehicle in the state.
           Each vehicle status item vs_i is itself a list in the format:
                 [<name>, <loc>, <length>, <is_horizontal>, <is_goal>]
           Where <name> is the name of the robot (a string)
                 <loc> is a location (a pair (x,y)) indicating the front of the vehicle,
                       i.e., its length is counted in the positive x- or y-direction
                       from this point
                 <length> is the length of that vehicle
                 <is_horizontal> is true iff the vehicle is oriented horizontally
                 <is_goal> is true iff the vehicle is a goal vehicle
        '''
        return self.vehicle_list

    def get_board_properties(self):
#IMPLEMENT
        '''Return (board_size, goal_entrance, goal_direction)
           where board_size = (m, n) is the dimensions of the board (m rows, n columns)
                 goal_entrance = (x, y) is the location of the goal
                 goal_direction is one of 'N', 'E', 'S' or 'W' indicating
                                the orientation of the goal
        '''
        return self.board_properties

#############################################
# heuristics                                #
#############################################


def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_min_moves(state):
#IMPLEMENT
    '''rushhour heuristic'''
    #We want an admissible heuristic. Getting to the goal requires
    #one move for each tile of distance.
    #Since the board wraps around, there are two different
    #directions that lead to the goal.
    #NOTE that we want an estimate of the number of ADDITIONAL
    #     moves required from our current state
    #1. Proceeding in the first direction, let MOVES1 =
    #   number of moves required to get to the goal if it were unobstructed
    #2. Proceeding in the second direction, let MOVES2 =
    #   number of moves required to get to the goal if it were unobstructed
    #
    #Our heuristic value is the minimum of MOVES1 and MOVES2 over all goal vehicles.
    #You should implement this heuristic function exactly, even if it is
    #tempting to improve it.
"""
    for v in rushhour.vehicle_statues:
        cut_counter = 0
        if v[3] == True:#is_horizontal = True
	    for i in range(v[2]):#v_length
	        if v[1][0]+i <= board_properties[0][0]-1:#BE CAREFUL, ON BOARD DOUBLE LIST X AND Y ARE OPPOSITE
	            board[v[1][1]][v[1][0]+i] = v[0]
	        else:
	            board[v[1][1]][0+cut_counter] = v[0]
	            cut_counter = cut_counter + 1
        else: #is_horizontal = False
	    for i in range(v[2]):#v_length
	        if v[1][1]+i <= board_properties[0][1]-1:
	            board[v[1][1]+i][v[1][0]] = v[0]
	        else:
	            board[0+cut_counter][v[1][0]] = v[0]
	            cut_counter = cut_counter + 1
"""
    goal_entrance = rushhour.board_properties[2]
    goal_orientation = rushhour.board_properties[3]
    board_xedge = rushhour.board_properties[0][0]
    board_yedge = rushhour.board_properties[0][1]
    MOVES1 = 0
    MOVES2 = 0
    MIN = max(board_xedge, board_yedge)
    for v in rushhour.vehicle_statues:
        is_horizontal = v[3]
        if v[4] == True:
            if is_horizontal:
                if goal_orientation == 'E' or goal_orientation == 'W':
                    if v[1][0] == goal_entrance[0]:
                        MOVES1 = abs(v[1][0]-goal_entrance[0])
                        MOVES2 = board_xedge-MOVES1
            else:
                if goal_orientation == 'N' or goal_orientation == 'S':
                    if v[1][1] == goal_entrance[1]:
                        MOVES1 = abs(v[1][1]-goal_entrance[1])
                        MOVES2 = board_yedge-MOVES1
            MIN = min(MIN, MOVES1, MOVES2)
        else:
            continue
                
    return MIN

def rushhour_goal_fn(state):
#IMPLEMENT
    '''Have we reached a goal state'''
    if heur_min_moves(state) == 0:
        return True

def make_init_state(board_size, vehicle_list, goal_entrance, goal_direction):
#IMPLEMENT
    '''Input the following items which specify a state and return a rushhour object
       representing this initial state.
         The state's its g-value is zero
         The state's parent is None
         The state's action is the dummy action "START"
       board_size = (m, n)
          m is the number of rows in the board
          n is the number of columns in the board
       vehicle_list = [v1, v2, ..., vk]
          a list of vehicles. Each vehicle vi is itself a list
          vi = [vehicle_name, (x, y), length, is_horizontal, is_goal] where
              vehicle_name is the name of the vehicle (string)
              (x,y) is the location of that vehicle (int, int)
              length is the length of that vehicle (int)
              is_horizontal is whether the vehicle is horizontal (Boolean)
              is_goal is whether the vehicle is a goal vehicle (Boolean)
      goal_entrance is the coordinates of the entrance tile to the goal and
      goal_direction is the orientation of the goal ('N', 'E', 'S', 'W')

   NOTE: for simplicity you may assume that
         (a) no vehicle name is repeated
         (b) all locations are integer pairs (x,y) where 0<=x<=n-1 and 0<=y<=m-1
         (c) vehicle lengths are positive integers
    '''
    #rushhour.board_size = board_size
    #rushhour.goal_entrance = goal_entrance
    #rushhour.goal_direction = goal_direction
    
    rushhour.board_properties = (board_size, goal_entrance, goal_orientation)
    rushhour.vehicle_list = vehicle_list

########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################


def get_board(vehicle_statuses, board_properties):
    #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
    #and in generating sample trace output.
    #Note that if you implement the "get" routines
    #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
    #properly, this function should work irrespective of how you represent
    #your state.
    (m, n) = board_properties[0]
    board = [list(['.'] * n) for i in range(m)]
    for vs in vehicle_statuses:
        for i in range(vs[2]):  # vehicle length
            if vs[3]:
                # vehicle is horizontal
                board[vs[1][1]][(vs[1][0] + i) % n] = vs[0][0]
                # represent vehicle as first character of its name
            else:
                # vehicle is vertical
                board[(vs[1][1] + i) % m][vs[1][0]] = vs[0][0]
                # represent vehicle as first character of its name
    # print goal
    board[board_properties[1][1]][board_properties[1][0]] = board_properties[2]
    return board


def make_rand_init_state(nvehicles, board_size):
    '''Generate a random initial state containing
       nvehicles = number of vehicles
       board_size = (m,n) size of board
       Warning: may take a long time if the vehicles nearly
       fill the entire board. May run forever if finding
       a configuration is infeasible. Also will not work any
       vehicle name starts with a period.

       You may want to expand this function to create test cases.
    '''

    (m, n) = board_size
    vehicle_list = []
    board_properties = [board_size, None, None]
    for i in range(nvehicles):
        if i == 0:
            # make the goal vehicle and goal
            x = randint(0, n - 1)
            y = randint(0, m - 1)
            is_horizontal = True if randint(0, 1) else False
            vehicle_list.append(['gv', (x, y), 2, is_horizontal, True])
            if is_horizontal:
                board_properties[1] = ((x + n // 2 + 1) % n, y)
                board_properties[2] = 'W' if randint(0, 1) else 'E'
            else:
                board_properties[1] = (x, (y + m // 2 + 1) % m)
                board_properties[2] = 'N' if randint(0, 1) else 'S'
        else:
            board = get_board(vehicle_list, board_properties)
            conflict = True
            while conflict:
                x = randint(0, n - 1)
                y = randint(0, m - 1)
                is_horizontal = True if randint(0, 1) else False
                length = randint(2, 3)
                conflict = False
                for j in range(length):  # vehicle length
                    if is_horizontal:
                        if board[y][(x + j) % n] != '.':
                            conflict = True
                            break
                    else:
                        if board[(y + j) % m][x] != '.':
                            conflict = True
                            break
            vehicle_list.append([str(i), (x, y), length, is_horizontal, False])

    return make_init_state(board_size, vehicle_list, board_properties[1], board_properties[2])


def test(nvehicles, board_size):
    s0 = make_rand_init_state(nvehicles, board_size)
    se = SearchEngine('astar', 'full')
    #se.trace_on(2)
    final = se.search(s0, rushhour_goal_fn, heur_min_moves)
