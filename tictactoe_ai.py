import random
from basic_ttt_functions import *


def basic_ai(board_array):
    # if board is full, immediately stop
    if not check_for_spaces:
        return board_array

    # options to be randomly selected from are initialized empty
    board_options = []

    # trawls through board adding options
    for x in range(3):
        for y in range(3):
            if board_array[x][y] == " ":
                board_options.append((x,y))

    # choose a random option
    choice = random.randint(0, len(board_options) - 1)
    choice_pair = board_options[choice]
    x_select = choice_pair[0]
    y_select = choice_pair[1]
    board_array[x_select][y_select] = "O"
    return board_array


def moderate_ai(board_array):
    # if there are two of a kind in any diagonal, row, or column
    # then the AI will add a letter to the third
    # note that having two is an edge case, and that there are no
    # first, columns
    for x in range(WIDTH):
        if board_array[x][0] == board_array[x][1]:
            if board_array[x][2] == ' ':
                board_array[x][2] = 'O'
                return board_array
        elif board_array[x][1] == board_array[x][2]:
            if board_array[x][0] == ' ':
                board_array[x][0] = 'O'
                return board_array
        elif board_array[x][0] == board_array[x][2]:
            if board_array[x][1] == ' ':
                board_array[x][1] = 'O'
                return board_array

    # second, rows
    for y in range(HEIGHT):
        if board_array[0][y] == board_array[1][y]:
            if board_array[2][y] == ' ':
                board_array[2][y] = 'O'
                return board_array
        elif board_array[1][y] == board_array[2][y]:
            if board_array[0][y] == ' ':
                board_array[0][y] = 'O'
                return board_array
        elif board_array[0][y] == board_array[2][y]:
            if board_array[1][y] == ' ':
                board_array[1][y] = 'O'
                return board_array

    # third, diagonals
    if board_array[0][0] == board_array[2][2]:
        if board_array[1][1] == ' ':
            board_array[1][1] = 'O'
            return board_array
    elif board_array[0][0] == board_array[1][1]:
        if board_array[2][2] == ' ':
            board_array[2][2] = 'O'
            return board_array
    elif board_array[1][1] == board_array[2][2]:
        if board_array[0][0] == ' ':
            board_array[0][0] = 'O'
            return board_array
    elif board_array[0][2] == board_array[2][0]:
        if board_array[1][1] == ' ':
            board_array[1][1] = 'O'
            return board_array
    elif board_array[0][2] == board_array[1][1]:
        if board_array[2][0] == ' ':
            board_array[2][0] = 'O'
            return board_array
    elif board_array[1][1] == board_array[2][0]:
        if board_array[0][2] == ' ':
            board_array[0][2] = 'O'
            return board_array

    # if none are found, it will take the center if available
    if board_array[1][1] == ' ':
        board_array[1][1] = "O"
        return board_array

    # if that is not available, it will default to basic_AI
    board_array = basic_ai(board_array)
    return board_array


def impossible_ai(board_array):
    return board_array
    # forces a tie at worst


def player_turn(board_array):

    return board_array