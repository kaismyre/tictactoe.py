import random


def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])


test_board = ["X"] * 10

# display_board(test_board)


def player_input():
    marker = ''

    while marker != "X" or marker != "O":
        marker = input("Enter X or O to start: ").upper()

        if marker == "X":
            return ("X", "O")
        elif marker == "O":
            return ("O", "X")
        else:
            print('You must enter X or O only')


# print(player_input())


def place_marker(board, marker, position):
    board[position] = marker


#place_marker(test_board, '$', 5)
# print(display_board(test_board))


def win_ckeck(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark))


#print(win_ckeck(test_board, 'X'))


def random_player():

    if random.randint(0, 1) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please enter your position from 1 to 9: "))
    return position


def play_again():
    return input("Do you want to play again? Enter y or n ").lower().startswith('y')

    # Game
    print('Welcome to Tic Tac Toe!')


while True:

    game_board = [' '] * 10
    player1_mark, player2_mark = player_input()
    turn = random_player()
    print(turn + " You go first")

    play = turn
    if play:
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_mark, position)

            if win_ckeck(game_board, player1_mark):
                display_board(game_board)
                print("Congratulation Player1 You have Won!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("oooh it's a draw! Play again")
                    break
                else:
                    turn = "Player 2"

        else:

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_mark, position)

            if win_ckeck(game_board, player2_mark):
                display_board(game_board)
                print("Congratulation Player2 You have Won!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("oooh it's a draw! Play again")
                    break
                else:
                    turn = "Player 1"

    if not play_again():
        break
