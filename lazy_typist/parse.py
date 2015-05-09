def board_parse(filename):
    with open(filename) as f:
        board = f.read().splitlines()   # split file into lines

    return [list(x) for x in board]     # turn each line into a list of chars
