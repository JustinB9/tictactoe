import random

def basic_AI(board_array):
    #options to be randomly selected from are initialized empty
    board_options = []

    #trawls through board adding options
    for x in board_array:
        for y in x:
            if board_array[x][y] == " ":
                board_options.append((x,y))

    #choose a random option
    choice = random.randint(0, len(board_options) - 1)
    x_select = board_options[choice[0]]
    y_select = board_options[choice[1]]
    board_array[x_select][y_select] = "O"
    return

def moderate_AI(board_array):
    return board_array
    #blocks twos

def impossible_AI(board_array):
    return board_array
    #forces a tie at worst