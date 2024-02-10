import matplotlib 
import matplotlib.pyplot as plt
import copy
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation

def createFoundPathGraph(maze,foundPath):
    newMaze = []
    for sizeOfFoundPath in range(len(foundPath)):
        newMaze.append(copy.deepcopy(maze))
    for index in range(len(foundPath)):
        for distanceFromStart in range(index,len(foundPath)):
            if newMaze[distanceFromStart][foundPath[index][0]][foundPath[index][1]] == 'G':
                continue
            newMaze[distanceFromStart][foundPath[index][0]][foundPath[index][1]] = 'H'
    return newMaze

def displayMazeAnimation(searchAlg, foundPath, mazeName,solvable):
    if solvable:
        solutionMaze = createFoundPathGraph(searchAlg[0],foundPath)
        for i in range(len(solutionMaze)):
            searchAlg.append(solutionMaze[i])

    symbolMapping = {'H': 0.4, 'X': 1, 'S': 0.2, 'G': 0.6, '.': 0, 'O': 0.8}
    colorMapping = {0: 'purple', 0.2: 'cyan', 0.4: 'yellow', 0.6: 'green', 0.8: 'blue', 1: 'black'}

    norm = mcolors.Normalize(vmin=0, vmax=1)
    cmap = mcolors.ListedColormap([colorMapping[0], colorMapping[0.2], colorMapping[0.4], colorMapping[0.6], colorMapping[0.8], colorMapping[1]])
    fig, ax = plt.subplots()
    fig.suptitle(mazeName)
    fig.set_size_inches((7, 7))

    def updateSearchAlg(frame):
        ax.clear()
        maze = searchAlg[frame]
        numericArray = np.array([[symbolMapping[item[0]] for item in row] for row in maze])
        ax.imshow(numericArray, cmap=cmap, norm=norm, extent=[0, len(maze[0]), 0, len(maze)])
        ax.set_xticks([])
        ax.set_yticks([])
        #ax.set_title(f'Frame {frame + 1}/{len(searchAlg)}')

    showSearch = FuncAnimation(fig, updateSearchAlg, frames=len(searchAlg), interval=50,repeat=False)
    plt.show()


def getArray():
    while True:
        try:
            userInput = int(input("Enter which Maze to Observe 1 and 10: "))
            if 1 <= userInput <= 10:
                return userInput
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input.")

def getAlg():
    while True:
        try:
            userChoice = int(input("Choose an option:\n1. Depth First Search\n2. Breadth First Search\n3. A*\n4. Exit\n"))
            match userChoice:
                case 1:
                    print("Depth First Search selected.")
                    return "dfs"
                case 2:
                    print("Breadth First Search selected.")
                    return "bfs"
                case 3:
                    print("A* selected.")
                    return "a"
                case 4:
                    print("Exiting the program.")
                    return "exit"
                case _:
                    print("Please enter a valid choice (1, 2, 3, or 4).")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            

def displayMaze(allMazes):
    while True:
        arrayNumber = getArray()
        algorithm = getAlg()
        if algorithm == "exit":
            break
        print(f"Displaying Array #{arrayNumber}, Algorithm:", end=' ')
        match algorithm:
            case "dfs":
                print(f"Depth First Search\n")
                displayMazeAnimation(allMazes[arrayNumber-1]._visualDFS,allMazes[arrayNumber-1]._solutionDFS,"Array #" + str(arrayNumber) + ": Depth First Search",allMazes[arrayNumber-1]._solvable)       
            case "bfs":
                print(f"Breadth First Search\n")
                displayMazeAnimation(allMazes[arrayNumber-1]._visualBFS,allMazes[arrayNumber-1]._solutionBFS,"Array #" + str(arrayNumber) + ": Breadth First Search",allMazes[arrayNumber-1]._solvable)       
            case "a":
                print(f"A*\n")
                displayMazeAnimation(allMazes[arrayNumber-1]._visualA,allMazes[arrayNumber-1]._solutionA,"Array #" + str(arrayNumber) + ": A*",allMazes[arrayNumber-1]._solvable)       

            

        
