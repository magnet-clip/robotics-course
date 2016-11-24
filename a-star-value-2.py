# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
        
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

from heapq import heappush, heappop

def compute_value(grid, goal, cost):
    value = [[99 if grid[row][col] == 1 else -1 for col in range(len(grid[0]))] for row in range(len(grid))]
    max_row = len(grid)
    max_col = len(grid[0])
    
    adjacents = []
    
    def make(row, col, d):
        if value[row][col] == -1:
            value[row][col] = d
            heappush(adjacents, (d, [row, col]))            

    make(goal[0], goal[1], 0)
    while len(adjacents) > 0:
        (distance, pivot) = heappop(adjacents)
        [row, col] = pivot
        if row-1 >= 0: make(row-1, col, distance+1)
        if row+1 < max_row: make(row+1, col, distance+1)
        if col+1 < max_col: make(row, col+1, distance+1)
        if col-1 >= 0: make(row, col-1, distance+1)
        
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    for row in range(max_row):
        for col in range(max_col):
            if value[row][col] == -1:
                value[row][col] = 99
                
    return value 

res = compute_value(grid, goal, cost)
#print res
for row in res:
    print row