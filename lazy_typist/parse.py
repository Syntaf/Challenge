import math

def board_parse(filename):
    with open(filename) as f:
        board = f.read().splitlines()   # split file into lines

    return [list(x) for x in board]     # turn each line into a list of chars

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
