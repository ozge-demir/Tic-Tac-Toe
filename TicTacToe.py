# TIC TAC TOE

"""
What we need to do:
1. We need to print a board.
2. Take in player input.
3. Place their input on the board.
4. Check if the game is won,tied, lost, or ongoing.
5. Repeat 3 and 4 until the game has been won or tied.
6. Ask if players want to play again.

Game Play Steps:
1. Decide whose turn it is (choose_first())
2. Show the board
3. Choose the position to put mark on
4. Check if there is a win on the board
5. Check if there is a tie on the board
6. If no tie or no win, next player's turn
7. Do the same steps 1-6 (for the next player)
8. Ask if they wanna replay
"""
import random


# function to print the Tic Tac Toe Board
def display_board(board):
    # clear the board for the new game
    print('\n' * 100)

    print('{}  |  {}  |  {}'.format(board[7], board[8], board[9]))
    print('--------------')
    print('{}  |  {}  |  {}'.format(board[4], board[5], board[6]))
    print('--------------')
    print('{}  |  {}  |  {}'.format(board[1], board[2], board[3]))


# function to take player input to let them choose their marker as X or O
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# function to place the player input on the board
def put_choice_on_board(board, marker, position):
    board[position] = marker


# function to check if there is a win on the board
def win_check(board, mark):
    # check All Rows to see if they all share the same marker
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            # check ALL Columns, to see if marker matches
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            # 2 diagonals, check to see match
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


# function to decide which player goes first
def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# function to check if the position is empty
def is_cell_empty(board, position):
    return board[position] == ' '


# function that checks if the board is full and returns a boolean value
def is_board_full(board):
    for i in range(1, 10):
        if is_cell_empty(board, i):
            return False
    return True


# function to take the player position
def player_position_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_cell_empty(board, position):
        position = int(input('Choose a position (1-9): '))

    return position


# function to ask for replaying
def replay():
    choice = input('Do you want to replay the game? y or n: ')

    return choice == 'y'


# ************************ MAIN GAME PROGRAM ********************************
print('Welcome to Tic Tac Toe!')

# While loop for keep the game running

while True:
    # Play the game

    # set everything up (board, who plays first, choose X or O
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' is the first player')

    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(the_board)

            pos = player_position_choice(the_board)

            put_choice_on_board(the_board, player1_marker, pos)

            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                # or check of there is a tie
                if is_board_full(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)

            pos = player_position_choice(the_board)

            put_choice_on_board(the_board, player2_marker, pos)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                # or check of there is a tie
                if is_board_full(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 1'


    if not replay():
        break