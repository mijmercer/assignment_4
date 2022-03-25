from board import *
def new_game():
    board = [
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
        ['8', ['R', 'B'], ['N', 'B'] , ['B', 'B'], ['Q', 'B'], ['K', 'B'], ['B', 'B'], ['N', 'B'], ['R', 'B'], '8'],
        ['7', ['P', 'B'], ['P', 'B'], ['P', 'B'], ['P', 'B'], ['P', 'B'], ['P', 'B'], ['P', 'B'], ['P', 'B'], '7'],
        ['6', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '6'],
        ['5', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '5'],
        ['4', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '4'],
        ['3', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '3'],
        ['2', ['P', 'W'], ['P', 'W'], ['P', 'W'], ['P', 'W'], ['P', 'W'], ['P', 'W'], ['P', 'W'], ['P', 'W'], '2'],
        ['1', ['R', 'W'], ['N', 'W'] , ['B', 'W'], ['K', 'W'], ['Q', 'W'], ['B', 'W'], ['N', 'W'], ['R', 'W'], '1'],
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' ']
        ]
    turn = "W"
    return board, turn
    
def print_game_state(b, turn):
    if turn == 'B':
        print("It is Black's turn")
    else:
        print("It is White's turn")
    pretty(b)
        
