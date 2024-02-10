import random
import sys

def generateRandomNumber():
    return random.randint(0, 9)

def placeStart(graph,row,col):
    graph[row][col][0] = 'S'

def placeGoal(graph,row,col):
    graph[row][col][0] = 'G'

def placeObstacles(graph):
    density = (generateRandomNumber()+1)/20
    # print("Density: " + str(density))
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col][0] == '.' and random.random() < density:
                graph[row][col][0] = 'X'

def generateMaze():
    blankMaze = [
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]],
    [['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0],['.',0]]
]
    startRow = generateRandomNumber()
    startCol = generateRandomNumber()
    goalRow = generateRandomNumber()
    goalCol = generateRandomNumber()
    while ((abs((startRow + startCol) - (goalRow + goalCol)) < 6 )):
        goalRow = generateRandomNumber()
        goalCol = generateRandomNumber() 
    # print(f"Start Row and Column: {startRow} , {startCol}")
    # print(f"Goal Row and Column: {goalRow} , {goalRow}")
    # print(((startRow + startCol) - (goalRow + goalRow)))
    placeStart(blankMaze,startRow,startCol)
    placeGoal(blankMaze,goalRow,goalCol)
    placeObstacles(blankMaze)
    return blankMaze,startRow,startCol,goalRow,goalCol