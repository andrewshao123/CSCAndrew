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
from copy import deepcopy
##################################################
# The search space class 'rushhour'             #
# This class is a sub-class of 'StateSpace'      #
##################################################

	
class rushhour(StateSpace):
    def __init__(self, action, gval, vehicle_statuses, board_properties, parent = None):
	#IMPLEMENT
        """Initialize a rushhour search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.vehicle_statuses = vehicle_statuses
        self.board_properties = board_properties

    def successors(self):
#IMPLEMENT
        '''Return list of rushhour objects that are the successors of the current object'''
        States = list()
        board_xedge = self.board_properties[0][0]
        board_yedge = self.board_properties[0][1]

        board = [[' ' for x in range(board_xedge)] for x in range(board_yedge)]

        for v in self.get_vehicle_statuses():
            v_x = v[1][0]
            v_y = v[1][1]
            if v[3] == True:#is_horizontal = True
                for i in range(v[2]):#v_length
                    board[v_y][(v_x+i)%board_xedge] = v[0]
            else: #is_horizontal = False
                for i in range(v[2]):#v_length
                    board[(v_y+i)%board_yedge][v_x] = v[0]
        #print(board)
        index = 0
        for i in range(len(self.get_vehicle_statuses())):
            v_name = self.vehicle_statuses[i][0]
            v_x = self.vehicle_statuses[i][1][0]
            v_y = self.vehicle_statuses[i][1][1]
            v_len = self.vehicle_statuses[i][2]
            v_hor = self.vehicle_statuses[i][3]
            v_goal = self.vehicle_statuses[i][4]
            if v_hor == True: #if the vehicle is horizontal
                if board[v_y][(v_x - 1)%(board_xedge)] == ' ':
                    new_vehicle_statuses = deepcopy(self.vehicle_statuses)
                    #print(new_vehicle_statuses)
                    new_vehicle_statuses[i][1] = ((v_x-1)%(board_xedge),v_y)
                    #print((new_vehicle_statuses))
                    States.append(rushhour('move_vehicle('+v_name+', W)', self.gval +1, new_vehicle_statuses, list(self.get_board_properties()), self))


                if board[v_y][(v_x+v_len)%(board_xedge)] == ' ':
                    new_vehicle_statuses = deepcopy(self.vehicle_statuses)
                    new_vehicle_statuses[i][1] = ((v_x+1)%(board_xedge),v_y)
                    #print((new_vehicle_statuses))
                    States.append(rushhour('move_vehicle('+v_name+', E)', self.gval +1, new_vehicle_statuses, list(self.get_board_properties()), self))

            else: #if the vehicle is vertical
                if board[(v_y - 1)%(board_yedge)][v_x] == ' ':
                    new_vehicle_statuses = deepcopy(self.vehicle_statuses)
                    new_vehicle_statuses[i][1] = (v_x,(v_y - 1)%(board_yedge))
                    #print((new_vehicle_statuses))
                    States.append(rushhour('move_vehicle('+v_name+', N)', self.gval +1, new_vehicle_statuses, list(self.get_board_properties()), self))

                if board[(v_y + v_len)%(board_yedge)][v_x] == ' ':
                    new_vehicle_statuses = deepcopy(self.vehicle_statuses)
                    new_vehicle_statuses[i][1] = (v_x,(v_y + 1)%(board_yedge))
                    #print((new_vehicle_statuses))
                    States.append(rushhour('move_vehicle('+v_name+', S)', self.gval +1, new_vehicle_statuses, list(self.get_board_properties()), self))
            index = index +1
        #print('before')
        #student_vehicles = sorted(s.successors()[i].get_vehicle_statuses())
        #for vs in sorted(self.vehicle_statuses):
        #    print('**************')
        print('after*****************')
        print(len(States))
        i = 0
        for x in States:
            print((x.get_vehicle_statuses()))
            print((x.get_board_properties()))
            #x.print_state()
            #i += 1
        return States

    def hashable_state(self):
#IMPLEMENT
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.''' 
        vehicle_statuses = []
        board_properties = []
        index = 0
        for i in range(len(self.vehicle_statuses)):
            vehicle_statuses.append(tuple(list(self.vehicle_statuses[i])))
        for i in range(len(self.board_properties)):
            board_properties.append(tuple(list(self.board_properties[i])))
        return (tuple(vehicle_statuses), tuple(board_properties))

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
        return self.vehicle_statuses

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

    vehicle_statuses = state.get_vehicle_statuses()
    board_properties = state.get_board_properties()
    goal_entrance = board_properties[1]
    goal_orientation = board_properties[2]
    board_xedge = board_properties[0][0]
    board_yedge = board_properties[0][1]
    MOVES1 = 0
    MOVES2 = 0
    MIN = max(board_xedge, board_yedge)
    for v in vehicle_statuses:
        #is_horizontal = v[3]
        if v[4] == True:#is_goal
            if v[3]:
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
    return (heur_min_moves(state) == 0)

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
    #self, action, gval, vehicle_statuses, board_properties, parent = None):
    #(board_size, vehicle_list, goal_entrance, goal_direction):
    board_properties = (board_size, goal_entrance, goal_direction)
    vehicle_list = vehicle_list
    return rushhour("START",0 ,vehicle_list, board_properties, None)
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

#test(3,(7,7))
