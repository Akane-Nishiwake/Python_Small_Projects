# Conway's Game of Life

import random
import time
import copy

# board width and height
WIDTH = 60
HEIGHT = 8

# Create a 2D list for the cells
nextCells = []

# Setting the initial cells with random alive and dead cells
for x in range(WIDTH):  # x and width are related
    column = []  # Create new column
    for y in range(HEIGHT):  # y and height are related
        if random.randint(0, 1) == 0:
            column.append("#")  # add living cell
        else:
            column.append(" ")  # add dead cell

    nextCells.append(column)  # nextCells is a list of the column list
# Main program Loop
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
            livingNeighbors = 0
            if currentCells[left][top] == "#":
                livingNeighbors += 1  # Top left is alive
            if currentCells[x][top] == "#":
                livingNeighbors += 1  # top neighbor is alive
            if currentCells[right][top] == "#":
                livingNeighbors += 1  # top right neighbor is alive
            if currentCells[left][y] == "#":
                livingNeighbors += 1  # left neighbor is alive
            if currentCells[right][y] == "#":
                livingNeighbors += 1  # right neighbor is alive
            if currentCells[left][bottom] == "#":
                livingNeighbors += 1  # bottom left neighbor is alive
            if currentCells[x][bottom] == "#":
                livingNeighbors += 1  # bottom neighbor is alive
            if currentCells[right][bottom] == "#":
                livingNeighbors += 1  # bottom right neighbor is alive

            # Set cell based on CGOL Rules
            if currentCells[x][y] == "#" and (
                livingNeighbors == 2 or livingNeighbors == 3
            ):
                # Living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and livingNeighbors == 3:
                # Dead cells with 3 neighbors become alive
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays dead
                nextCells[x][y] = " "

        # Add a pause to reduce flickering
        time.sleep(0.1)
