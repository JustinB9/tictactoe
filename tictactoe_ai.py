import random
#import basic_ttt_functions

def basic_AI(board_array):
    #options to be randomly selected from are initialized empty
    board_options = []

    #trawls through board adding options
    for x in range(3):
        for y in range(3):
            if board_array[x][y] == " ":
                board_options.append((x,y))

    #choose a random option
    choice = random.randint(0, len(board_options) - 1)
    choice_pair = board_options[choice]
    x_select = choice_pair[0]
    y_select = choice_pair[1]
    board_array[x_select][y_select] = "O"
    return board_array

def moderate_AI(board_array):
    return board_array
    #blocks twos

def impossible_AI(board_array):
    return board_array
    #forces a tie at worst

def player_turn(board_array):

    return board_array