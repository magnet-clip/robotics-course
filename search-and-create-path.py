# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

path = []

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------

    max_row = len(grid)
    max_col = len(grid[0])

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    expand =  [[-1 for col in range(max_col)] for row in range(max_row)]
    action =  [[-1 for col in range(max_col)] for row in range(max_row)]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    wander = [[' ' for col in range(max_col)] for row in range(max_row)]    

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    step = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = step
            step += 1
            path.append([g,x,y])
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            
    if not found:
        return wander
    
    path.reverse()
    [lg, lx, ly] = path[0]
    wander[lx][ly] = '*'
    
    #for [g, x, y] in path:
    #    #print [g,x,y]
    #    if g != lg:
    #        diff = [lx-x, ly-y]
    #        if diff in delta:
    #            pos = delta.index(diff)
    #            symbol = delta_name[pos]
    #            #print symbol
    #            wander[x][y] = symbol
    #            [lg, lx, ly] = [g, x, y]        
    
    policy = [[' ' for col in range(max_col)] for row in range(max_row)]   
    x = goal[0]
    y = goal[1]
    policy[x][y]= '*'
    
    while x!=init[0] or y != init[1]:
        x2 = x -  delta[action[x][y]][0]
        y2 = y -  delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x= x2
        y=y2
    #return wander
    return policy

expand = search(grid,init,goal,cost)
for e in expand:
    print e