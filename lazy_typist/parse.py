import math

def board_parse(filename):
    with open(filename) as f:
        board = f.read().splitlines()   # split file into lines

    return [list(x) for x in board]     # turn each line into a list of chars

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def find_shift(board):
    shifts = []
    for row in range(0,len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == '^':
                shifts.append((row,col))
    if distance(shifts[1], (0,0)) < distance(shifts[0], (0,0)):
        a = shifts[0]
        shifts[0] = shifts[1]
        shifts[1] = a
    return shifts
