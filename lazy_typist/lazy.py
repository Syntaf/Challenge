from parse import board_parse, distance

board = board_parse("board.dat")

sentence = input("Enter a sentence(lower case / upper case no punctuation):\n")

prev = (0,0)
left_hand_pos = (3,5)
right_hand_pos = (3,5)
for letter in sentence:
    for row in range(0,len(board)):
        if letter in board[row]:
            index = board[row].index(letter)

    if distance((row,index),left_hand_pos) < distance((row,index),right_hand_pos):
        print("left")
        left_hand_pos = (row,index)
    else:
        print("right")
        right_hand_pos = (row, index)
