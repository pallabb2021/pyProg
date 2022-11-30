"""
Logic -
1. Print Game Borad print_board
    print_board(bo)
2. Find empty cell (so that player cannot insert into already filled cell)
    check_position_for_zero(bo,x,y)
3. Check win
    winner(bo)
        1. Any 3 cell row wise
        2. Any 3 cell column wise
        3. Diagonal 3 cell

4. Check data correctness
    input_data_check(x,y)

5. Find any empty cell for game run
    find_empty(bo)
6. Play Game
    play(bo):

7. To be enhanced.. put all data check in one place...
"""

import sys

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def print_board(bo):
    for i in range(len(bo)):
        print("_____________")
        for j in range(len(bo[0])):
            print("| " + str(bo[i][j]) + " ", end="")
        print()
    print("_____________")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return True  # cell is empty
    return None  # no cell is empty.


# print(find_empty(board))

def check_position_for_zero(bo, x, y):
    try:
        if bo[x][y] == 0:
            return True
    except IndexError:
        pass
    except ValueError:
        pass
        # print("Index is wrong.. try again!")


def fill_cell(bo, x, y, pl1_or_pl2):
    value = pl1_or_pl2
    if value == 1:
        bo[x][y] = 1
    else:
        bo[x][y] = 2


def input_data_check(x, y):
    try:
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
    except IndexError:
        return False
    return True


def input_data_check_enhanced(user_input):
    try:
        x = int(user_input.split(',')[0])
        y = int(user_input.split(',')[1])
        if not user_input:  # if the value is empty!
            return False
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
    except IndexError:
        return False
    except ValueError:
        return False
    return True


def play(bo):
    while find_empty(bo):
        if winner(board) != 0:
            print(f"We have a winner! Congratulations {winner(board)}")
            sys.exit(0)
        print_board(board)

        while True:
            if not find_empty(bo):
                print("No more moved possible, quitting game!")
                sys.exit(0)
            print(
                "PLAYER1 : Enter the position(x,y = 0,0 or 0,1 or 0,2 or 1,0 or 1,1 or 1,2 or or 2,0 or 2,1 or 2,"
                "2) to mark '1")
            user_position = input()
            result1 = input_data_check_enhanced(user_position)

            if result1:  # (data is correct, break the while True loop)
                break

            if not find_empty(bo):
                print("No more moved possible, quitting game!")
                sys.exit(0)
        print(f" PLAYER 1 RESULT CHEKC = {result1}")
        print(f" find_empty check in player 1 {find_empty(bo)}")
        if check_position_for_zero(bo, int(user_position.split(',')[0]), int(user_position.split(',')[1])):
            fill_cell(board, int(user_position.split(',')[0]), int(user_position.split(',')[1]), 1)
        else:
            while True:
                if not find_empty(bo):
                    print("No more moved possible, quitting game!")
                    sys.exit(0)
                print("This cell is not available.. enter another set of co-ordiate")
                print(
                    "PLAYER1 : Enter the position(x,y = 0,0 or 0,1 or 0,2 or 1,0 or 1,1 or 1,2 or or 2,0 or 2,1 or 2,"
                    "2) to mark '1")
                user_position = input()

                if check_position_for_zero(bo, int(user_position.split(',')[0]), int(user_position.split(',')[1])):
                    fill_cell(board, int(user_position.split(',')[0]), int(user_position.split(',')[1]), 1)
                    break

                if not find_empty(bo):
                    print("No more moved possible, quitting game!")
                    sys.exit(0)
        print_board(board)
        if winner(board) != 0:
            print(f"We have a winner! Congratulations {winner(board)}")
            sys.exit(0)
        while True:
            if not find_empty(bo):
                print("No more moved possible, quitting game!")
                sys.exit(0)
            print(
                "PLAYER2 : Enter the position(x,y = 0,0 or 0,1 or 0,2 or 1,0 or 1,1 or 1,2 or or 2,0 or 2,1 or 2,"
                "2) to mark '2")
            user_position = input()
            result2 = input_data_check_enhanced(user_position)

            if result2:  # (data is correct, break the while True loop)
                break
            if not find_empty(bo):
                print("No more moved possible, quitting game!")
                sys.exit(0)
        print(f" PLAYER 2 RESULT CHEKC = {result2}")
        if check_position_for_zero(bo, int(user_position.split(',')[0]), int(user_position.split(',')[1])):
            fill_cell(board, int(user_position.split(',')[0]), int(user_position.split(',')[1]), 2)
        else:
            while True:
                if not find_empty(bo):
                    print("No more moved possible, quitting game!")
                    sys.exit(0)
                print("This cell is not available.. enter another set of co-ordinate")
                print(
                    "PLAYER2 : Enter the position(x,y = 0,0 or 0,1 or 0,2 or 1,0 or 1,1 or 1,2 or or 2,0 or 2,1 or 2,"
                    "2) to mark '2")
                user_position = input()

                if check_position_for_zero(bo, int(user_position.split(',')[0]), int(user_position.split(',')[1])):
                    fill_cell(board, int(user_position.split(',')[0]), int(user_position.split(',')[1]), 2)
                    break

                if not find_empty(bo):
                    print("No more moved possible, quitting game!")
                    sys.exit(0)
        print_board(board)

        print(winner(board))


def winner(bo):
    # row check..
    for x in range(3):
        row = {bo[x][0], bo[x][1], bo[x][2]}
        if len(row) == 1 or len(row) == 1 and bo[x][0] != 0:
            return bo[x][0]

    # column check..
    for x in range(3):
        column = {bo[0][x], bo[1][x], bo[2][x]}
        if len(column) == 1 or len(column) == 1 and bo[0][x] != 0:
            return bo[0][x]

    # diagonal
    diag1 = {bo[0][0], bo[1][1], bo[2][2]}
    diag2 = {bo[0][2], bo[1][1], bo[2][0]}
    # if (len(diag1) == 1) and (bo[0][0] == 1):
    #     print("Player 1 wins")
    if len(diag1) == 1 or len(diag2) == 1 and bo[1][1] != 0:
        return bo[1][1]

    return 0


play(board)
winner(board)
