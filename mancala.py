"""
File:    mancala.py
Author:  Timothy Rauck
Date:    11/3/2023
Section: 52
E-mail:  trauck1@umbc.edu
Description: This program is the game mancala, the user can pick the two names and play the game
"""
from typing import List, Union, Any

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
# six spaces
SPSIX = '      '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


# This function takes the player names and puts them into a list
def get_player(names):
    name_question1 = input("Player 1 please tell me your name: ")
    names.append(name_question1)
    name_question2 = input("Player 2 please tell me your name: ")
    names.append(name_question2)

    return names


# This function creates the list needed for the draw_board function
def board_detail(names):
    player_1 = names[0]
    player_2 = names[1]

    details = [
        [
            ["cup", "1", "Stones", "4", ""],
            ["cup", "2", "Stones", "4", ""],
            ["cup", "3", "Stones", "4", ""],
            ["cup", "4", "Stones", "4", ""],
            ["cup", "5", "Stones", "4", ""],
            ["cup", "6", "Stones", "4", ""],
        ],
        [
            ["cup", "13", "Stones", "4", ""],
            ["cup", "12", "Stones", "4", ""],
            ["cup", "11", "Stones", "4", ""],
            ["cup", "10", "Stones", "4", ""],
            ["cup", "9", "Stones", "4", ""],
            ["cup", "8", "Stones", "4", ""]
        ],
        [SPSIX, SPSIX, SPSIX, player_1[0: BLOCK_WIDTH].rjust(BLOCK_WIDTH), SPSIX, SPSIX, SPSIX, 'Stone', '0', SPSIX,
         SPSIX],
        [SPSIX, SPSIX, SPSIX, player_2[0: BLOCK_WIDTH].rjust(BLOCK_WIDTH), SPSIX, SPSIX, SPSIX, 'Stone', '0', SPSIX,
         SPSIX]
    ]

    draw_board(details[0], details[1], details[2], details[3])
    return details


# Run game uses all the functions needed to run the game
def run_game():
    names = []
    get_player(names)
    board_detail(names)
    take_turns(board_detail(names), names)


# Take turns allows the players to take turns picking stones and see how the board changes after each move
def take_turns(board, name):
    counter = 1
    game_over = False
    user_turn = input(f"{name[0]}, What cup do you want to move? ")
    while not game_over:
        if int(user_turn) >= 14 or int(user_turn) == 7 or int(user_turn) <= 0:
            print("That isn't a valid move.")
            counter -= 1
        for i in range(len(board[1])) and range(len(board[0])):
            if board[1][i][1] == user_turn:
                if board[1][i][3] != "0":
                    num = i - 1
                    row = 1
                    for cups in range(int(board[1][i][3])):
                        if num < 0:
                            board[2][8] = int(board[2][8])
                            board[2][8] += 1
                            board[2][8] = str(board[2][8])
                            num = 0
                            row = 0
                            if cups + 1 == (int(board[1][i][3])):
                                counter -= 1
                                print("You landed on a mancala, go again")
                        elif num > 5:
                            board[3][8] = int(board[3][8])
                            board[3][8] += 1
                            board[3][8] = str(board[3][8])
                            num = 5
                            row = 1
                            if cups + 1 == (int(board[1][i][3])):
                                counter -= 1
                                print("You landed on a mancala, go again")
                        else:
                            if row == 1:
                                board[row][num][3] = int(board[row][num][3])
                                board[row][num][3] += 1
                                board[row][num][3] = str(board[row][num][3])
                                num -= 1
                            elif row == 0:
                                board[row][num][3] = int(board[row][num][3])
                                board[row][num][3] += 1
                                board[row][num][3] = str(board[row][num][3])
                                num += 1
                    board[1][i][3] = "0"
                    row = 1
                elif board[1][i][3] == "0":
                    print("This isn't a valid move.")
                    counter -= 1
            elif board[0][i][1] == user_turn:
                if board[0][i][3] != "0":
                    num = i + 1
                    row = 0
                    for cups in range(int(board[0][i][3])):
                        if num > 5:
                            board[3][8] = int(board[3][8])
                            board[3][8] += 1
                            board[3][8] = str(board[3][8])
                            num = 5
                            row = 1
                            if cups + 1 == (int(board[0][i][3])):
                                counter -= 1
                                print("You landed on a mancala, go again")
                        elif num < 0:
                            board[2][8] = int(board[2][8])
                            board[2][8] += 1
                            board[2][8] = str(board[2][8])
                            num = 0
                            row = 0
                            if cups + 1 == (board[0][i][3]):
                                counter -= 1
                                print("You landed on a mancala, go again")
                        else:
                            if row == 0:
                                board[row][num][3] = int(board[row][num][3])
                                board[row][num][3] += 1
                                board[row][num][3] = str(board[row][num][3])
                                num += 1
                            elif row == 1:
                                board[row][num][3] = int(board[row][num][3])
                                board[row][num][3] += 1
                                board[row][num][3] = str(board[row][num][3])
                                num -= 1
                    board[0][i][3] = "0"
                    row = 0
                elif board[0][i][3] == "0":
                    print("This isn't a valid move.")
                    counter -= 1
        draw_board(board[0], board[1], board[2], board[3])
        game_over = end_game(board, name)
        counter += 1
        if game_over == False:
            if counter % 2 == 1:
                user_turn = input(f"{name[0]}, What cup do you want to move? ")
            elif counter % 2 == 0:
                user_turn = input(f"{name[1]}, What cup do you want to move? ")


# This function is a helper function for the take_turns function,
# checking to see if the game has ended after each turn
def end_game(board, name):
    top_row = 0
    bottom_row = 0
    for i in range(6):
        board[0][i][3] = int(board[0][i][3])
        board[1][i][3] = int(board[1][i][3])
        top_row += board[0][i][3]
        bottom_row += board[1][i][3]
        board[0][i][3] = str(board[0][i][3])
        board[1][i][3] = str(board[1][i][3])
    if top_row == 0 or bottom_row == 0:
        board[2][8] = int(board[2][8])
        board[3][8] = int(board[3][8])
        if board[2][8] > board[3][8]:
            print(f"{name[0]} is the winner")
        elif board[3][8] > board[2][8]:
            print(f"{name[1]} is the winner")
        elif board[3][8] == board[2][8]:
            print("The game has ended in a tie")
        board[2][8] = str(board[2][8])
        board[3][8] = str(board[3][8])
        return True
    else:
        return False


if __name__ == '__main__':
    run_game()
