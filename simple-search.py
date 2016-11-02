# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

        
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    max_row = len(grid)
    max_col = len(grid[0])

    import heapq
    open_list = []
    heapq.heappush(open_list, (0, init))
    
    marks = [[False for col in range(max_col)] for row in range(max_row)]
    marks[0][0] = True
    
    def find_available_moves(g, pos):
        [row, col] = pos
    
        for move in delta:
            [d_row, d_col] = move
            [new_col, new_row] = [col + d_col, row + d_row]
            
            if new_col < max_col and new_row < max_row and new_col >= 0 and new_row >= 0:
                if grid[new_row][new_col] != 1 and not marks[new_row][new_col]:
                    heapq.heappush(open_list, (g+cost, [new_row, new_col]))
                    marks[new_row][new_col] = True
                    
    (g_value, position) = heapq.heappop(open_list)
    last = [g_value] + position
    #print (g_value, position)
    if position != goal:
        find_available_moves(g_value, position)

    while position != goal and len(open_list) > 0:
        (g_value, position) = heapq.heappop(open_list)
        last = [g_value] + position
        #print last
        if position != goal:
            find_available_moves(g_value, position)
    
    if position != goal:
        return 'fail'
        
    return last

print search(grid, init, goal, cost)