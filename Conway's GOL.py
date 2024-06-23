
#This is for later still dont have the skills yet

# Conway's Game of Life
# The 4 Rules of a cell
# Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
# Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
import random

# This is the base Board state of a 10 x 10
board_state = [
    [1, 1, 1, 1, 1, 1, 1],#[0][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[1][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[2][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[3][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[4][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[6][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[7][0-6]
    [1, 1, 1, 1, 1, 1, 1],#[8][0-6]
    [1, 1, 1, 1, 1, 1, 1] #[9][0-6]
]

#board dead state where all values are 0
def deadState(_width, _height):



#board
width = 10
height = 10
