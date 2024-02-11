# Maze-Solving Program

## Overview

This project was created for my 2024 Winter Semester of Introduction to AI course. The program is designed to solve mazes using three different search algorithms: Depth First Search (DFS), Breadth First Search (BFS), and A*. The program generates random mazes, applies the search algorithms, and provides visualizations and statistics about the solution paths.

## Files and Structure

The program is organized into several files, each serving a specific purpose:

1. **main.py**: The main script that orchestrates the execution of the program.

2. **maze.py**: Defines the `Maze` class representing the maze structure.

3. **aStar.py, breadthFirstSearch.py, depthFirstSearch.py**: Implementations of the A*, BFS, and DFS search algorithms, respectively.

4. **displayMaze.py**: Contains functions for visualizing the maze and the search process using matplotlib.

5. **generateMaze.py**: Generates random mazes with a start, goal, and obstacles.

6. **printResults.py**: Handles the execution of the search algorithms, prints results, and calculates averages.

# Useage

1. Run the main.py script.
2. Select a maze number to observe from 1 to 10 in the terminal.
3. Choose an algorithm (DFS, BFS, A*) in the terminal to visualize the solution paths and statistics.
4. View the maze animation and results for the chosen algorithm and maze.

## Dependencies

The program relies on the following Python libraries:

- `matplotlib`: Used for maze visualization and animatio[Uploading generateMaze.py…]()
ns.
- `numpy`: Used for array operations in the visualization process.

To install the required dependencies, use the following commands:

```bash
pip install matplotlib
pip install numpy
```
## Author

- Nijuuken
