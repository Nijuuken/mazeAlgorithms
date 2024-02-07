import copy
from generateMaze import *

class Maze:
    def __init__(self, grid, startRow, startCol, goalRow, goalCol):
        self._maze, self._startRow, self._startCol, self._goalRow, self._goalCol = generateMaze()
        self._nodeExpandDFS = 0
        self._solPatLenDFS = 0
        self._nodeExpandBFS = 0
        self._solPatLenBFS = 0
        self._nodeExpandA = 0
        self._solPatLenA = 0
        self._executionTimeDFS = 0 
        self._executionTimeBFS = 0 
        self._executionTimeAFS = 0 
        self._solvable = True
        self._visualDFS = []
        self._visualBFS = []
        self._visualA = []
        self._solutionDFS = []
        self._solutionBFS = []
        self._solutionA = []

    @property
    def maze(self):
        return self._maze

    @property
    def startRow(self):
        return self._startRow

    @property
    def startCol(self):
        return self._startCol

    @property
    def goalRow(self):
        return self._goalRow

    @property
    def goalCol(self):
        return self._goalCol

    @property
    def nodeExpandDFS(self):
        return self._nodeExpandDFS

    @nodeExpandDFS.setter
    def nodeExpandDFS(self, newNodeExpandDFS):

        self._nodeExpandDFS = newNodeExpandDFS

    @property
    def solPatLenDFS(self):
        return self._solPatLenDFS

    @solPatLenDFS.setter
    def solPatLenDFS(self, newSolPatLenDFS):

        self._solPatLenDFS = newSolPatLenDFS

    @property
    def nodeExpandBFS(self):
        return self._nodeExpandBFS

    @nodeExpandBFS.setter
    def nodeExpandBFS(self, newNodeExpandBFS):
        self._nodeExpandBFS = newNodeExpandBFS

    @property
    def solPatLenBFS(self):
        return self._solPatLenBFS

    @solPatLenBFS.setter
    def solPatLenBFS(self, newSolPatLenBFS):
        self._solPatLenBFS = newSolPatLenBFS

    @property
    def nodeExpandA(self):
        return self._nodeExpandA

    @nodeExpandA.setter
    def nodeExpandA(self, newNodeExpandA):
        self._nodeExpandA = newNodeExpandA

    @property
    def solPatLenA(self):
        return self._solPatLenA

    @solPatLenA.setter
    def solPatLenA(self, newSolPatLenA):
        self._solPatLenA = newSolPatLenA

    @property
    def executionTimeDFS(self):
        return self._executionTimeDFS

    @executionTimeDFS.setter
    def executionTimeDFS(self, newExecutionTimeDFS):
        self._executionTimeDFS = newExecutionTimeDFS

    @property
    def executionTimeBFS(self):
        return self._executionTimeBFS

    @executionTimeBFS.setter
    def executionTimeBFS(self, newExecutionTimeBFS):
        self._executionTimeBFS = newExecutionTimeBFS

    @property
    def executionTimeAFS(self):
        return self._executionTimeAFS

    @executionTimeAFS.setter
    def executionTimeAFS(self, newExecutionTimeAFS):
        self._executionTimeAFS = newExecutionTimeAFS

    @property
    def solvable(self):
        return self._solvable

    @solvable.setter
    def solvable(self, newSolvable):
        self._solvable = newSolvable

    def getVisualizationDFS(self, mazeArray):
        newIteration = copy.deepcopy(mazeArray)
        self._visualDFS.append(newIteration)

    def getVisualizationBFS(self, mazeArray):
        newIteration = copy.deepcopy(mazeArray)
        self._visualBFS.append(newIteration)
    def getVisualizationA(self, mazeArray):
        newIteration = copy.deepcopy(mazeArray)
        self._visualA.append(newIteration)
    def displayMaze(self):
        for row in self._maze:
            for element in row:
                print(str(element[0]).center(2), end=" ")
            print() 
        print("============================")

    def displayIteration(self,sortAlg,number):
        data = getattr(self, f'_{sortAlg}', None)
        result = data[number]
        for row in result:
            for element in row:
                print(str(element[0]).center(2), end=" ")
            print() 
        print("============================")
