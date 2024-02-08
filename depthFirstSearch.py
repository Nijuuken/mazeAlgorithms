import copy
import time

from maze import *

def depthFirstSearch(myMaze):
    startTime = round(time.time()*1000)
    mazeDFS = copy.deepcopy(myMaze.maze)
    visited = set()
    stack = [(myMaze.startRow, myMaze.startCol, 0,[])]

    while stack:
        currentRow, currentCol, pathLength, pathTaken = stack.pop()
        currentPosition = (currentRow,currentCol)
        #print(f"At Row {currentRow}, column {currentCol}")
        if not (0 <= currentRow < 10) or not (0 <= currentCol < 10):
            #print("Out of bounds")
            continue
        if currentPosition in visited:
            continue
        visited.add(currentPosition)
        mazeDFS[currentRow][currentCol][1] = pathLength
        if mazeDFS[currentRow][currentCol][0] == 'X': 
            #print("It's a wall")
            continue
        if mazeDFS[currentRow][currentCol][0] == 'G':
            myMaze._solutionDFS = pathTaken
            myMaze.solPatLenDFS = pathLength
            #print("Goal was found")
            myMaze.executionTimeDFS = round(time.time()*1000) - startTime
            myMaze.solvable = True
            return True
        mazeDFS[currentRow][currentCol][0] = 'H'
        myMaze.getVisualizationDFS(mazeDFS)
        mazeDFS[currentRow][currentCol][0] = 'O'
        #myMaze.displayIteration("visualDFS",myMaze.nodeExpandDFS)
        #print(f"Adding ({currentCol},{currentRow-1}),({currentCol-1},{currentRow}),({currentCol},{currentRow+1}), and ({currentCol+1},{currentRow}) to the stack")
        stack.append((currentRow,currentCol+1, pathLength + 1, pathTaken + [(currentRow-1,currentCol,)]))
        stack.append((currentRow+1,currentCol, pathLength + 1, pathTaken + [(currentRow-1,currentCol,)]))
        stack.append((currentRow,currentCol-1, pathLength + 1, pathTaken + [(currentRow-1,currentCol,)]))
        stack.append((currentRow-1,currentCol, pathLength + 1, pathTaken + [(currentRow-1,currentCol,)]))

        myMaze._nodeExpandDFS += 1
    #print("Goal was not found")
    myMaze.executionTimeDFS = round(time.time()*1000) - startTime
    # If the stack becomes empty and no solution is found
    myMaze.solvable = False
    return False
