# Time to play tic tac toe


board = [' ' for x in range(10)]


def insert_letter(letter, position):
    board[position] = letter


def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)


def computer_move():
    possible_moves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if is_winner(board_copy, letter):
                move = i
                return move

    if 5 in possible_moves:
        move = 5
        return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(list):
    import random
    length = len(list)
    rand_range = random.randrange(0, length)
    return list[rand_range]


def is_board_full(board):
    if board.count(' ') <= 1:
        print_board(board)
        print('Tie game. Play again!')
        quit()


def main():

    print('\nTime to play Tic Tac Toe :)')
    while not is_board_full(board):
        print_board(board)

        if is_winner(board, 'X') == True:
            print_board(board)
            print('You won! Good job!')
            break
        elif is_winner(board, 'O') == True:
            print_board(board)
            print('Sorry, the computer won this time. Try again!')
            break

        spot_choice = int(input('Choose a space 1-9: '))

        if spot_choice in range(1, 10) and board[spot_choice] == ' ':
            board[spot_choice] = 'X'
            move = computer_move()
            if move != 0:
                insert_letter('O', move)
        else:
            print('Make sure that the number you inputted is 1-9 and the space you chose does not already have a letter in it.')
    quit()


main()
