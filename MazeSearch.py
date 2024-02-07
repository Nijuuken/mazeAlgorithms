import time
import copy
import heapq
from collections import deque
from maze import *
from depthFirstSearch import *
from breadthFirstSearch import *
from aStar import *

#from displayMaze import *

# def breadthFirstSearch(row, col, graph):
#     graphBFS = copy.deepcopy(graph)
#     count = 0

#     def countIt(row, col, graph, visited=set(), solutionPathLen=0, length=0):
#         nonlocal count
#         queue = deque([(row, col, solutionPathLen, length)])
        
#         while queue:
#             row, col, solutionPathLen, length = queue.popleft()
#             pos = (row, col)

#             if pos in visited:
#                 continue

#             if (row < 0 or row >= len(graph) or col < 0 or col >= len(graph[row])):
#                 continue

#             if graph[row][col][0] == 'X':
#                 continue

#             count += 1
#             visited.add(pos)
#             graph[row][col][1] = length

#             if graph[row][col][0] == 'G':
#                 graph[row][col][0] = 'H'
#                 #time.sleep(0.5)
#                 displayMaze(graph)
#                 return graph[row][col][1], True

#             if graph[row][col][0] != 'S':
#                 graph[row][col][0] = 'H'

#             #time.sleep(0.5)
#             displayMaze(graph)

#             if graph[row][col][0] != 'S':
#                 graph[row][col][0] = 'O'

#             # Enqueue neighbors
#             queue.append((row, col - 1, solutionPathLen, length + 1))
#             queue.append((row - 1, col, solutionPathLen, length + 1))
#             queue.append((row, col + 1, solutionPathLen, length + 1))
#             queue.append((row + 1, col, solutionPathLen, length + 1))

#         return solutionPathLen, False

#     solutionPathLen, found = countIt(row, col, graphBFS)
#     print("Number of Nodes Expanded: ", count)
#     print("Solution Path Length: ", solutionPathLen)
    
#     if found:
#         print("Breadth-First Search found the Goal!")
#     else:
#         print("Breadth-First Search did not find the Goal!")

#     return count, solutionPathLen  


# def aStar(startRow, startCol, endRow, endCol, graph):
#     graphAStar = copy.deepcopy(graph)
#     count = 0

#     def distanceToGoal(row, col):
#         return abs(row - endRow) + abs(col - endCol)

#     def countIt(row, col, graph, visited=set(), solutionPathLen=0, length=0):
#         nonlocal count, startRow, startCol, endRow, endCol
#         priorityQueue = [(distanceToGoal(row, col), row, col, solutionPathLen, length)]

#         while priorityQueue:
#             _, row, col, solutionPathLen, length = heapq.heappop(priorityQueue)
#             pos = (row, col)

#             if pos in visited:
#                 continue

#             if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[row]):
#                 continue

#             if graph[row][col][0] == 'X':
#                 continue

#             count += 1
#             visited.add(pos)
#             graph[row][col][1] = length
#             #print(f"Distance from end: ({distanceToGoal(row, col)})")
#             if row == endRow and col == endCol:
#                 graph[row][col][0] = 'H'
#                 #time.sleep(0.5)
#                 displayMaze(graph)
#                 return graph[row][col][1], True

#             if graph[row][col][0] != 'S':
#                 graph[row][col][0] = 'H'
#                 #time.sleep(0.5)
#                 displayMaze(graph)

#             if graph[row][col][0] != 'S':
#                 graph[row][col][0] = 'O'

#             # Enqueue neighbors with priority based on A* formula (f = g + h)
#             heapq.heappush(priorityQueue, (distanceToGoal(row, col - 1), row, col - 1, solutionPathLen + 1, length + 1))
#             heapq.heappush(priorityQueue, (distanceToGoal(row - 1, col), row - 1, col, solutionPathLen + 1, length + 1))
#             heapq.heappush(priorityQueue, (distanceToGoal(row, col + 1), row, col + 1, solutionPathLen + 1, length + 1))
#             heapq.heappush(priorityQueue, (distanceToGoal(row + 1, col), row + 1, col, solutionPathLen + 1, length + 1))
#             #print(priorityQueue)

#         return solutionPathLen, False

#     solutionPathLen, found = countIt(startRow, startCol, graphAStar)
#     print("Number of Nodes Expanded: ", count)
#     print("Solution Path Length: ", solutionPathLen)

#     if found:
#         print("A* Search found the Goal!")
#     else:
#         print("A* Search did not find the Goal!")

#     return count, solutionPathLen


def main():
    nodeExpandDFS, solPatLenDFS, nodeExpandBFS, solPatLenBFS, nodeExpandA, solPatLenA = 0, 0, 0, 0, 0, 0
    allMazes = [] 
    
    for i in range(10):
        mazeInstance = Maze(*generateMaze())
        allMazes.append(mazeInstance)
    for i in range(10):
        passFail = depthFirstSearch(allMazes[i])
    breadthFirstSearch(allMazes[0])
    aStar(allMazes[0])
    #solPatLenDFS, nodeExpandBFS, solPatLenBFS, nodeExpandA, and solPatLenA
        
    #time.sleep(5)
    #nodeExpandBFS, solPatLenBFS = breadthFirstSearch(startRow, startCol, newMaze)
    #nodeExpandAStar, solPatLenAStar = aStar(startRow, startCol,goalRow,goalCol, newMaze)

     
main()