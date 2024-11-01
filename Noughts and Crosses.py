
## Create empty board
def new_board():
    return [[None,None,None],[None,None,None],[None,None,None]]

## Display current board state
def render(board):
    i=0
    print('   0   1   2')
    for row in board:
        print(f'{i} ', ' | '.join([item if item is not None else ' ' for item in row]))
        if i<2:
            print('  ', '-' * 9)
        i+=1

def input_coord(coord):
    while True:
        x = int(input(f'What is your move\'s {coord} coordinate? '))
        if x in [0,1,2]:
            return x
        else:
            print('Invalid coordinate given')

## Receive coordinates for next move
def get_move(board, player):
    while True:
        x = input_coord('X')
        y = input_coord('Y')

        if board[x][y] is not None:
            print('invalid move')
        else:
            return (x, y)

## Update board state after move has been made
def make_move(board, coords, player):
    new_board = board
    new_board[coords[0]][coords[1]] = player
    return new_board
    
## Check if a player has won
def get_winner(board):
    lines = board + [[row[i] for row in board] for i in range(3)] + [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    for line in lines:
        if line in [['O', 'O', 'O'], ['X', 'X', 'X']]:
            return line[0]
    return None


## Check if there is a draw
def is_board_full(board):
    full = True
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                full = False
    return full
    

board = new_board()
turn = 0
while True:
    turn += 1
    player = ['O','X'][turn%2]

    render(board)
    print(f'{player}\'s turn:')
    move_coords = get_move(board, player)
    make_move(board, move_coords, player)
    winner = get_winner(board)

    if winner is not None:
        render(board)
        print(f'{winner} wins')
        break
    
    if is_board_full(board):
        render(board)
        print('It\'s a draw')
        break
