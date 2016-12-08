# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    from heapq import heappush, heappop

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    value = [[999 if grid[row][col] == 1 else {} for col in range(len(grid[0]))] for row in range(len(grid))]
    max_row = len(grid)
    max_col = len(grid[0])
    
    def get_move(row, col, direction, action):
        [up, left, down, right] = forward
        if action == -1: # right turn
            if direction == 0: # up
                return right
            elif direction == 1: # left
                return up
            elif direction == 2: # down
                return left
            # right
            return down
        elif action == 0: # forward
            if direction == 0: # up
                return up
            elif direction == 1: # left
                return left
            elif direction == 2: # down
                return down
            # right
            return right
            
        # left turn
        if direction == 0: # up
            return left
        elif direction == 1: # left
            return down
        elif direction == 2: # down
            return right
        # right
        return up

    adjacents = []
    heappush(adjacents, (0, [init[0], init[1], init[2]])) # cost, position, direction
    #value[init[0]][init[1]][cost[]]
    
    while len(adjacents) > 0:
        (distance, state) = heappop(adjacents)
        [row, col, direction] = state
        
        for i, a in enumerate(action):
            move = get_move(row, col, direction, a)
            [d_row, d_col] = move
            new_row = row + d_row
            new_col = col + d_col
            new_dir = forward.index(move)
            price = cost[i]
            if new_row >= 0 and new_row < max_row and new_col >= 0 and new_col < max_col:
                vals = value[new_row][new_col]
                if vals == 999: continue

                add = False                    
                if new_dir not in vals:
                    add = True
                elif vals[new_dir] > distance + price: 
                    add = True

                if add:                        
                    value[new_row][new_col][new_dir] = distance + price
                    heappush(adjacents, (distance + price, [new_row, new_col, new_dir]))

                                

    policy2D = value
    return policy2D
    
res = optimum_policy2D(grid,init,goal,cost)
for row in res:
    #for item in row:
    print row