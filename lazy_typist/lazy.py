from parse import board_parse, distance, find_shift
board = board_parse("board.dat")
shifts = find_shift(board)
lshift = shifts[0]
rshift = shifts[1]


sentence = input("Enter a sentence(lower case / upper case no punctuation):\n")

prev = (0,0)
left_hand_pos = (3,5)
right_hand_pos = (3,5)
for letter in sentence:
    for row in range(0,len(board)):
        if letter.lower() in board[row]:
            index = board[row].index(letter.lower())
    # if letter is uppercase
    if letter == letter.upper():
        if distance(right_hand_pos, rshift) < distance(left_hand_pos, lshift):
            left_hand_pos = lshift
            right_hand_pos = (row, index)
            print("shift : left hand")
            print(letter, ":     right hand")
        else:
            right_hand_pos = rshift
            left_hand_pos = (row, index)
            print("shift: right hand")
            print(letter, ":     left hand")
    else:
        if distance((row,index),left_hand_pos) < distance((row,index),right_hand_pos):
            print(letter, ":     left hand")
            left_hand_pos = (row,index)
        else:
            print(letter, ":     right hand")
            right_hand_pos = (row, index)
