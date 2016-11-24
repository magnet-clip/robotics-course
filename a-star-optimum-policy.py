# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    from heapq import heappush, heappop
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    value = [[99 if grid[row][col] == 1 else -1 for col in range(len(grid[0]))] for row in range(len(grid))]
    max_row = len(grid)
    max_col = len(grid[0])
    
    adjacents = []
    
    def make(row, col, d):
        if value[row][col] == -1:
            value[row][col] = d
            heappush(adjacents, (d, [row, col]))            

    def make2(row, col, drow, dcol, d):
        new_row = row + drow
        new_col = col + dcol
        if value[new_row][new_col] == -1:
            value[new_row][new_col] = d
            heappush(adjacents, (d, [new_row, new_col])) 
            
            shift = [-drow, -dcol]
            name = delta_name[delta.index(shift)]
            policy[new_row][new_col] = name
            

    make(goal[0], goal[1], 0)
    policy[goal[0]][goal[1]] = '*'
    while len(adjacents) > 0:
        (distance, pivot) = heappop(adjacents)
        [row, col] = pivot
        #if row-1 >= 0: make(row-1, col, distance+1)
        #if row+1 < max_row: make(row+1, col, distance+1)
        #if col+1 < max_col: make(row, col+1, distance+1)
        #if col-1 >= 0: make(row, col-1, distance+1)
        if row-1 >= 0: make2(row, col, -1, 0, distance+1)
        if row+1 < max_row: make2(row, col, 1, 0, distance+1)
        if col+1 < max_col:  make2(row, col, 0, 1, distance+1)
        if col-1 >= 0: make2(row, col, 0, -1, distance+1)
        
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    for row in range(max_row):
        for col in range(max_col):
            if value[row][col] == -1:
                value[row][col] = 99
                
    return policy 

res = optimum_policy(grid, goal, cost)
#print res
for row in res:
    print row