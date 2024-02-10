import copy
import time
import heapq

def aStar(myMaze):
    startTime = round(time.time()*1000)
    mazeAStar = copy.deepcopy(myMaze.maze)
    visited = set()
    count = 0

    def heuristic(row, col):
        # A simple heuristic function, you might want to adjust it
        return abs(row - myMaze.goalRow) + abs(col - myMaze.goalCol)

    priorityQueue = [(heuristic(myMaze.startRow, myMaze.startCol), myMaze.startRow, myMaze.startCol, 0, [])]

    while priorityQueue:
        _, currentRow, currentCol, pathLength, pathTaken = heapq.heappop(priorityQueue)
        currentPosition = (currentRow, currentCol)

        if currentPosition in visited:
            continue

        visited.add(currentPosition)

        if not (0 <= currentRow < 10) or not (0 <= currentCol < 10):
            continue

        if mazeAStar[currentRow][currentCol][0] == 'X':
            continue

        count += 1
        mazeAStar[currentRow][currentCol][1] = pathLength

        if currentRow == myMaze.goalRow and currentCol == myMaze.goalCol:
            myMaze._solutionA = pathTaken
            myMaze.solPatLenA = pathLength
            myMaze.executionTimeA = round(time.time()*1000) - startTime
            myMaze.solvable = True
            return True

        if mazeAStar[currentRow][currentCol][0] != 'S':
            mazeAStar[currentRow][currentCol][0] = 'H'

        myMaze.getVisualizationA(mazeAStar)
        mazeAStar[currentRow][currentCol][0] = 'O'
        #myMaze.displayIteration("visualA", myMaze.nodeExpandA)

        # Enqueue neighbors with priority based on A* formula (f = g + h)
        heapq.heappush(priorityQueue, (heuristic(currentRow, currentCol - 1), currentRow, currentCol - 1, pathLength + 1, pathTaken + [(currentRow, currentCol-1)]))
        heapq.heappush(priorityQueue, (heuristic(currentRow - 1, currentCol), currentRow - 1, currentCol, pathLength + 1, pathTaken + [(currentRow-1, currentCol)]))
        heapq.heappush(priorityQueue, (heuristic(currentRow, currentCol + 1), currentRow, currentCol + 1, pathLength + 1, pathTaken + [(currentRow, currentCol+1)]))
        heapq.heappush(priorityQueue, (heuristic(currentRow + 1, currentCol), currentRow + 1, currentCol, pathLength + 1, pathTaken + [(currentRow+1, currentCol)]))

        myMaze._nodeExpandA += 1

    myMaze.executionTimeA = round(time.time()*1000) - startTime
    myMaze._solutionA = pathTaken
    myMaze.solvable = False
    return False
