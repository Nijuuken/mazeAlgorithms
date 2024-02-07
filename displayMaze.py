import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def displayMaze(maze):
    # Create a mapping of symbols to numeric values and corresponding colors
    symbolMapping = {'H': 0.4, 'X': 1, 'S': 0.2, 'G': 0.6, '.': 0, 'O': 0.8}
    colorMapping = {0: 'purple', 0.2: 'blue', 0.4: 'red', 0.6: 'yellow', 0.8: 'green',1: 'black'}

    # Convert the symbols to a 2D array of numeric values
    numericArray = np.array([[symbolMapping[item[0]] for item in row] for row in maze])

    # Create a custom colormap with explicit normalization
    norm = mcolors.Normalize(vmin=0, vmax=1)
    # Specify the colors explicitly in the ListedColormap constructor
    cmap = mcolors.ListedColormap([colorMapping[0], colorMapping[0.2], colorMapping[0.4], colorMapping[0.6], colorMapping[0.8], colorMapping[1]])

    # Display the 2D array with custom symbols and colors using plt.imshow()
    plt.imshow(numericArray, cmap=cmap, norm=norm, extent=[0, len(maze[0]), 0, len(maze)])
    plt.colorbar()

    plt.xticks([]) # remove the tick marks by setting to an empty list
    plt.yticks([]) # remove the tick marks by setting to an empty list
    plt.show()