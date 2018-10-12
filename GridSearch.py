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

def search(grid,init,goal,delta):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    
    
    TempNeighbours = []
    
    g=0
    init.append(g)
    NewOpen = [init]
    NewClosed = []
    New
    CurrentCell = NewOpen[0]
#     print(goal)
#     print(NewOpen)
#     print(init)
#     print(NewOpen[0])
#     print(CurrentCell)
#     print([CurrentCell[0], CurrentCell[1]])
    

    #while loop begins here
    while [CurrentCell[0], CurrentCell[1]]!=goal:
        g+=1
        OldOpen = NewOpen
        OldClosed = NewClosed
        try:
            TempOpen, NewClosed, CurrentCell = FindCurrentCell(OldOpen, OldClosed)
        except IndexError:
            return 'fail'

        for i in range(len(delta)):
            temp = [CurrentCell[0]+delta[i][0], CurrentCell[1]+delta[i][1], CurrentCell[2]+1]
            TempNeighbours.append(temp)
        Neighbours = InGrid(TempNeighbours, grid)
        
        NewOpen = UpdateOpen(NewClosed, TempOpen, Neighbours)
    
    path = [CurrentCell[2], CurrentCell[0], CurrentCell[1]]

    return path

def FindCurrentCell(Open, Closed):
    if len(Open)==1:
        CurrentCell = Open.pop()
        Closed.append(CurrentCell)
    else:
        tempCell = Open[0]
        for i in range(len(Open)):
            if Open[i][2]<tempCell[2]:
                tempCell = Open[i]
        CurrentCell = tempCell
        Open.remove(CurrentCell)
        Closed.append(CurrentCell)
        
    return Open, Closed, CurrentCell

def InGrid(TempNeighbours, grid):
    Neighbours = []
    FreeNeighbours = []
    for i in range(len(TempNeighbours)):
            if (TempNeighbours[i][0]>=0) and (TempNeighbours[i][0]<=(len(grid)-1)):
                if (TempNeighbours[i][1]>=0) and (TempNeighbours[i][1]<=(len(grid[0])-1)):
                    Neighbours.append(TempNeighbours[i])
    for i in range(len(Neighbours)):
        row = Neighbours[i][0]
        col = Neighbours[i][1]
        if grid[row][col]==0:
            FreeNeighbours.append(Neighbours[i])
    return FreeNeighbours

def UpdateOpen(Closed, Open, Neighbours):
    
    OpenWithoutG = []
    for i in range(len(Open)):
        Cell = [Open[i][0], Open[i][1]]
        OpenWithoutG.append(Cell)
    
    ClosedWithoutG = []
    for i in range(len(Closed)):
        Cell = [Closed[i][0], Closed[i][1]]
        ClosedWithoutG.append(Cell)
        
    NeighboursWithoutG =[]
    for i in range(len(Neighbours)):
        Cell = [Neighbours[i][0], Neighbours[i][1]]
        NeighboursWithoutG.append(Cell)
        
        if NeighboursWithoutG[i] not in OpenWithoutG:
            if NeighboursWithoutG[i] not in ClosedWithoutG:
                Open.append(Neighbours[i])
                
    return Open

# search(grid,init,goal,delta)
    
