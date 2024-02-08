import time
import copy
import heapq
from collections import deque
from maze import *
from depthFirstSearch import *
from breadthFirstSearch import *
from aStar import *

#from displayMaze import *
def loadMazeList(allMazes):
    for i in range(10):
        mazeInstance = Maze(*generateMaze())
        allMazes.append(mazeInstance)

def getAvg(allMazes, methodName):
    addAllNumbers = 0
    for theMazes in allMazes:  # Iterate through allMazes
        result = getattr(theMazes,methodName, None)
        addAllNumbers += result
    
    if len(allMazes) > 0:
        average = addAllNumbers / len(allMazes)
        return average
    else:
        return None


def printHeader():
    header = f"{'Run':^7} {'Algorithm':^15} {'Solution Path Length':^20} {'Nodes Expanded':^20} {'Execution Time (ms)':^20} {'Status':^20}"
    print(header)

def printDFSAvg(allMazes):
    avg = f"{'Average':^7} {'DFS':^15}"
    avg += f"{str(getAvg(allMazes,'solPatLenDFS')):^20}"
    avg += f"{str(getAvg(allMazes,'nodeExpandDFS')):^24}"
    avg += f"{str(getAvg(allMazes,'executionTimeDFS')):^19}"
    #{'Solution Path Length':^20} {'Nodes Expanded':^20} {'Execution Time (ms)':^20} {'Status':^20}"
    print(avg)

def printBFSAvg(allMazes):
    avg = f"{'Average':^7} {'BFS':^15}"
    avg += f"{str(getAvg(allMazes,'solPatLenBFS')):^20}"
    avg += f"{str(getAvg(allMazes,'nodeExpandBFS')):^24}"
    avg += f"{str(getAvg(allMazes,'executionTimeBFS')):^19}"
    #{'Solution Path Length':^20} {'Nodes Expanded':^20} {'Execution Time (ms)':^20} {'Status':^20}"
    print(avg)


def gatherDFSData(allMazes):
    for i in range(10):
        passFail = depthFirstSearch(allMazes[i])
        print(f"{str(i+1):^7} {'DFS':^15} {str(allMazes[i].solPatLenDFS):^20} {str(allMazes[i].nodeExpandDFS):^20} {str(round(allMazes[i].executionTimeDFS)):^20}" ,end=" ")
        if passFail == True:
            print(f"{'Pass':^20}")
        else:
            print(f"{'Fail':^20}")
    printDFSAvg(allMazes)

def gatherBFSData(allMazes):
    for i in range(10):
        passFail = breadthFirstSearch(allMazes[i])
        print(f"{str(i+1):^7} {'BFS':^15} {str(allMazes[i].solPatLenBFS):^20} {str(allMazes[i].nodeExpandBFS):^20} {str(round(allMazes[i].executionTimeBFS)):^20}" ,end=" ")
        if passFail == True:
            print(f"{'Pass':^20}")
        else:
            print(f"{'Fail':^20}")
    printBFSAvg(allMazes)

def main():
    nodeExpandDFS, solPatLenDFS, nodeExpandBFS, solPatLenBFS, nodeExpandA, solPatLenA = 0, 0, 0, 0, 0, 0
    allMazes = [] 
    loadMazeList(allMazes)
    printHeader()
    gatherDFSData(allMazes)
    gatherBFSData(allMazes)

    aStar(allMazes[0])
    #solPatLenDFS, nodeExpandBFS, solPatLenBFS, nodeExpandA, and solPatLenA
         
main()