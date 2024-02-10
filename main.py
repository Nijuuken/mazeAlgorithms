from printResults import *
from displayMaze import *

def main():
    allMazes = [] 
    loadMazeList(allMazes)
    gatherDFSData(allMazes)
    gatherBFSData(allMazes)
    gatherA(allMazes)    
main()