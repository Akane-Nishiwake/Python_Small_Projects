# Conway's Game of Life
# The 4 Rules of a cell
# Any live cell with 0 or 1 live neighbors becomes dead,
#    #because of underpopulation
# Any live cell with 2 or 3 live neighbors stays alive,
#    #because its neighborhood is just right
# Any live cell with more than 3 live neighbors becomes dead,
#    #because of overpopulation
# Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
# # <- living cell
# ' ' <- dead cell
import random
import time
import copy

# board width and height
WIDTH = 40
HEIGHT = 20

# Create a 2D list for the cells
nextCells = []
for x in range(WIDTH):  # x and width are related
    column = []  # Create new column
    for y in range(HEIGHT):  # y and height are related
        if random.randint(0, 1) == 0:
            column.append("#")  # add living cell
        else:
            column.append(" ")  # add dead cell
    nextCells.append(column)  # nextCells is a list of the column list

while True:
    print("\n\n\n\n\n")  # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    # Printing cells to screen space
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or ''
        print()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            top = (y - 1) % HEIGHT
            bottom = (y + 1) % HEIGHT
            # Count the number of living neighbors
