"""
v = [[1,2,3],[4,5,6],[7,8,9]]
for i in v:
    if i[1] == 5:
        new_i = [9,9,9]
        new_vehicle = v.copy()
        new_vehicle.remove(i)
        new_vehicle.append(new_i)
        print(new_vehicle)
"""
"""
matrix = [[" " for x in range(3)] for x in range(7)]
print (matrix)
#for i in range(2):
#    print (i)
"""

"""122
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

"""188
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
"""
        for v in self.vehicle_statuses:
            v_x = v[1][0]
            v_y = v[1][1]
            cut_counter = 0
            if v[3] == True:#is_horizontal = True
                for i in range(v[2]):#v_length
                    if v_x+i <= self.board_properties[0][0]-1:#BE CAREFUL, ON BOARD DOUBLE LIST X AND Y ARE OPPOSITE
                        board[v_y][v_x+i] = v[0]
                    else:
                        board[v[1][1]][0+cut_counter] = v[0]
                        cut_counter = cut_counter + 1
            else: #is_horizontal = False
                for i in range(v[2]):#v_length
                    if v[1][1]+i <= self.board_properties[0][1]-1:
                        board[v[1][1]+i][v[1][0]] = v[0]
                    else:
                        board[0+cut_counter][v[1][0]] = v[0]
                        cut_counter = cut_counter + 1

"""
"""
a = ()
nested_lst = [['a',1,True],['b',2,False]]

nested_lst_of_tuples = []
for i in range(len(nested_lst)):
    print(tuple(nested_lst[i]))
    nested_lst_of_tuples.append(tuple(list(nested_lst[i])))
print(tuple(nested_lst_of_tuples))\
"""
"""
board_properties = ((7,7),(4,1),'E')
vehicle_statuses = [['gv', (1, 1), 2, True, True],
              ['1', (3, 1), 2, False, False],
              ['3', (4, 4), 2, False, False]]
board_xedge = board_properties[0][0]
board_yedge = board_properties[0][1]
board = [[' ' for x in range(board_xedge)] for x in range(board_yedge)]
for v in vehicle_statuses:
    v_x = v[1][0]
    v_y = v[1][1]
    if v[3] == True:#is_horizontal = True
        for i in range(v[2]):#v_length
            board[v_y][(v_x+i)%board_xedge] = v[0]
    else: #is_horizontal = False
        for i in range(v[2]):#v_length
            board[(v_y+i)%board_yedge][v_x] = v[0]
print(board)
"""
v=['1',(1,2)]
a = 'move_vehicle('+v[0]+',W)'
print(a)
