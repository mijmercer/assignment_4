def new_board():
    empty_board = [
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
        ['8', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '8'],
        ['7', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '7'],
        ['6', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '6'],
        ['5', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '5'],
        ['4', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '4'],
        ['3', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '3'],
        ['2', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '2'],
        ['1', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '1'],
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' ']
        ]
    return empty_board

#Colour of pieces
def colour(board, square):
    #need to invert rows
    #convert letters to numbers
    row_m, column_v = (i for i in square)
    row = (ord(row_m) - 96)
    column = (9 - int(column_v))
    return board[column][row][1]
#note 1 represents colour in new board ['chess_piece', 'colour']

#number of pieces on board
def count_pieces(board, colour):
    count = 0  
    for i in board:
        for n in i:
            #Found function showing how to account for an error and dont want code to crash. Thanks google
            try:
                if i[1] == colour:
                    count += 1
            except:
                None
    return count

#Returns letter in square
#Note same as colour however want 0 instead of 1 'chess_piece'
def piece(board, square):
    row_m, column_f = (i for i in square)
    row = (ord(row_m) - 96)
    column = (9 - int(column_f))
    thingymabob = board[column][row][0]
    if thingymabob == '□':
        return None
    else:
        return thingymabob
        

#puts piece in specific square
def place_piece(board, square, colour, piece):
    row_m, column_f = (i for i in square)
    row = (ord(row_m) - 96)
    column = (9 - int(column_f))
    board[column][row] = [piece, colour]
    
def pretty(board):
    nice_board = []
    for i in board:
        s = []
        for n in i:
            try:
            #add n to list
                s.append(n[0])
            except:
                s.append(n)
        nice_board.append(s)
    for i in nice_board:
        print(' '.join(i))
        
                