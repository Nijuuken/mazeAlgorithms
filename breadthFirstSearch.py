import copy
import time
from collections import deque

def breadthFirstSearch(myMaze):
    startTime = time.time()
    mazeBFS = copy.deepcopy(myMaze.maze)
    visited = set()
    queue = deque([(myMaze.startRow, myMaze.startCol, 0, [])])

    while queue:
        currentRow, currentCol, pathLength, pathTaken = queue.popleft()
        currentPosition = (currentRow, currentCol)

        # Check if the current position is within bounds
        if not (0 <= currentRow < 10) or not (0 <= currentCol < 10):
            continue

        # Check if the current position has been visited
        if currentPosition in visited:
            continue

        # Mark the current position as visited  
        visited.add(currentPosition)

        mazeBFS[currentRow][currentCol][1] = pathLength

        # Check if the current position is a wall
        if mazeBFS[currentRow][currentCol][0] == 'X':
            continue

        # Check if the goal is reached
        if mazeBFS[currentRow][currentCol][0] == 'G':
            myMaze._solutionBFS = pathTaken
            myMaze.solPatLenBFS = pathLength
            myMaze.executionTimeBFS = time.time() - startTime
            myMaze.solvable = True
            return True

        # Update maze visualization and expand the queue
        mazeBFS[currentRow][currentCol][0] = 'H'
        myMaze.getVisualizationBFS(mazeBFS)  
        mazeBFS[currentRow][currentCol][0] = 'O'
        #myMaze.displayIteration("visualBFS", myMaze.nodeExpandBFS)

        # Append adjacent positions to the queue
        queue.append((currentRow, currentCol + 1, pathLength + 1, pathTaken + [(currentRow, currentCol)]))
        queue.append((currentRow + 1, currentCol, pathLength + 1, pathTaken + [(currentRow, currentCol)]))
        queue.append((currentRow, currentCol - 1, pathLength + 1, pathTaken + [(currentRow, currentCol)]))
        queue.append((currentRow - 1, currentCol, pathLength + 1, pathTaken + [(currentRow, currentCol)]))

        myMaze._nodeExpandBFS += 1

    # If the queue becomes empty and no solution is found
    myMaze.executionTimeBFS = time.time() - startTime
    myMaze.solvable = False
    return False
