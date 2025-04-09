# TicTacToe

from time import sleep
from string import Template
import os


def welcome():
    # welcome

    def display(game):
        for index, char in enumerate(game):
            n = 6 * index
            if char == 'T':
                display_T(n)
                sleep(0.5)
            elif char == 'I':
                display_I(n)
                sleep(0.5)
            elif char == 'C':
                display_C(n)
                sleep(0.5)
            elif char == 'A':
                display_A(n)
                sleep(0.5)
            elif char == 'O':
                display_O(n)
                sleep(0.5)
            elif char == 'E':
                display_E(n)
                sleep(0.5)

    def display_T(n):
        for i in range(5):
            for j in range(n + 5):
                if i == 0 and j in range(n):
                    print(" ", end="")

                elif i == 0 or j == n + 2:
                    print("T", end="")

                else:
                    print(" ", end="")  # here you have to put end = '' or else it moves cursor to next line
            # To move to next line
            print()

    def display_I(n):
        for i in range(5):
            for j in range(n + 5):
                if i == 0 and j in range(n) or i == 4 and j in range(n):
                    print(" ", end="")
                elif i == 0 or j == n + 2 or i == 4:
                    print("I", end="")
                else:
                    print(" ", end="")
            print()

    def display_C(n):
        for i in range(5):
            for j in range(n + 5):
                if i == 0 and j in range(n) or i == 4 and j in range(n):
                    print(" ", end="")
                elif j == n or i == 0 or i == 4:
                    print("C", end="")
                else:
                    print(" ", end="")
            print()

    def display_A(n):
        for i in range(5):
            for j in range(n + 5):
                if i in range(2, 5) and j in range(n):
                    print(" ", end="")
                elif i == 2 or j == n and i in range(2, 5) or j == n + 4 and i in range(2,5) or i == 0 and j == n + 2 or i == 1 and j == n + 1 or i == 1 and j == n + 3:
                    print("A", end="")
                else:
                    print(" ", end="")
            print()

    def display_O(n):
        for i in range(5):
            for j in range(n + 5):
                if i in range(5) and j in range(n):
                    print(" ", end="")
                elif i == 0 or i == 4 or j == n or j == n + 4:
                    print("O", end="")
                else:
                    print(" ", end="")
            print()

    def display_E(n):
        for i in range(5):
            for j in range(n + 5):
                if i in range(5) and j in range(n):
                    print(" ", end="")
                elif i % 2 == 0 or j == n:
                    print("E", end="")
                else:
                    print(" ", end="")
            print()

    print(f'Welcome to..')

    game = 'TicTacToe'.upper()

    display(game)

def wanna_play():
    choice = '-1'
    toggle = ['Yes', 'No']

    while choice not in toggle:
        choice = input("Wanna play (Yes or No) ? ").capitalize()
        if choice not in toggle:
            print("I don't understand!! Enter Yes or No")

    return choice == 'Yes'

def instructions():
     # function to display board
    def display(board):
        for row in board:
            for block in board[row]:
                print(block, end="")
            print(" ")

    row1 = [' ---', ' ---', ' ---']
    row2 = ['|   |', '   ', '|   |']
    row3 = [' ---', ' ---', ' ---']
    row4 = ['|   |', '   ', '|   |']
    row5 = [' ---', ' ---', ' ---']
    row6 = ['|   |', '   ', '|   |']
    row7 = [' ---', ' ---', ' ---']

    board = {
        'row1': [' ---', ' ---', ' ---'],

        1: ['|   |', '   ', '|   |'],

        'row3': [' ---', ' ---', ' ---'],

        2: ['|   |', '   ', '|   |'],

        'row5': [' ---', ' ---', ' ---'],

        3: ['|   |', '   ', '|   |'],

        'row7': [' ---', ' ---', ' ---'],
    }
    # To display
    for i in range(1, 4):
        for j in range(3):
            print(f"Enter {i + 2 * (i - 1) + j} to insert 'X' or 'O' here")
            if j % 2 == 0:
                board[i][j] = '| O |'
                display(board)
                sleep(1.25)
                board[i][j] = '| X |'
                display(board)
                sleep(1.25)
                if i == 1:
                    board[i][j] = row2[j]
                elif i == 2:
                    board[i][j] = row4[j]
                else:
                    board[i][j] = row6[j]
            else:
                board[i][j] = ' O '
                display(board)
                sleep(1.25)
                board[i][j] = ' X '
                display(board)
                sleep(1.25)
                if i == 1:
                    board[i][j] = row2[j]
                elif i == 2:
                    board[i][j] = row4[j]
                else:
                    board[i][j] = row6[j]

def numpad():
    def display(*rows):
        for row in rows:
            for i in range(len(row)):
                print(row[i], end="")
            print(" ")

    row1 = [' ---', ' ---', ' ---']
    row2 = ['| 1 |', ' 2 ', '| 3 |']
    row3 = [' ---', ' ---', ' ---']
    row4 = ['| 4 |', ' 5 ', '| 6 |']
    row5 = [' ---', ' ---', ' ---']
    row6 = ['| 7 |', ' 8 ', '| 9 |']
    row7 = [' ---', ' ---', ' ---']

    display(row1, row2, row3, row4, row5, row6, row7)

def clear_out():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def display(board):
    for row in board:
        for block in board[row]:
            print(block, end="")
        print(" ")

def update_pl(player):
    if player == player1:
        return player2
    else:
        return player1

def update_us(choice):
    if choice == 'X':
        return 'O'
    else:
        return 'X'

def validate_cell(cell, available_cells):
    """
    Validates the choosen cell
    - valid range
    - cell available
    """
    if cell in available_cells:
        return True
    else:
        print('Invalid cell! Please choose an available cell.')
        return False

def validate_choice(choice, options):
    if choice in options:
        return True
    else:
        print(f'Invalid choice! Please select from {options}')
        return False

def update(board, cell, user_choice):
    positions = {
        1: ('row2', 0),
        2: ('row2', 1),
        3: ('row2', 2),
        4: ('row4', 0),
        5: ('row4', 1),
        6: ('row4', 2),
        7: ('row6', 0),
        8: ('row6', 1),
        9: ('row6', 2),
    }

    row, col = positions[cell]

    if col == 1:
        board[row][col] = f' {user_choice} '
    else:
        board[row][col] = f'| {user_choice} |'

def WinTie(board, player_choice, user_choice):

    winning_chance = [
        ['row2', 0, 'row2', 1, 'row2', 2],  # Top row
        ['row4', 0, 'row4', 1, 'row4', 2],  # Middle row
        ['row6', 0, 'row6', 1, 'row6', 2],  # Bottom row
        ['row2', 0, 'row4', 0, 'row6', 0],  # Left column
        ['row2', 1, 'row4', 1, 'row6', 1],  # Middle column
        ['row2', 2, 'row4', 2, 'row6', 2],  # Right column
        ['row2', 0, 'row4', 1, 'row6', 2],  # Diagonal \
        ['row2', 2, 'row4', 1, 'row6', 0],  # Diagonal /
    ]

    for choice in ['X', 'O']:
        for chance in winning_chance:
            if all(board[chance[i]][chance[i+1]] == (f' {choice} ' if chance[i+1] == 1 else f'| {choice} |') for i in range(0, len(chance), 2)):
                winner = player_choice if choice == user_choice else update_pl(player_choice)
                return True, winner

    return False, None

def gameon_choice():
    choice = '-1'
    while choice not in ['Y', 'N']:
        choice = input("Keep playing ? (Y or N)  ").upper()
        if choice == 'Y':
            return True
        else:
            print(f'Thank you for playing so far...')
            return False
    #gameon

    #game_on




welcome()

wanna_play = wanna_play()

if wanna_play:

    game_on = True

    while game_on:
        print("Let's drive into the world of TicTacToe")

        player1 = input("Enter your good name : ").capitalize()
        player2 = input("Your companion : ").capitalize()

        t = Template("Great!! $companion1 and $companion2 stick to your seats and lock in for a wonderful gaming experience.")
        ready = t.safe_substitute(companion1 = player1, companion2 = player2)
        print(ready)
        sleep(5)

        print("Here are few instructions: ")
        sleep(2)
        instructions()

        print("Here is a quick go through of instructions again, if you didn't get it..")
        numpad()
        print("To select a block, enter corresponding number")
        sleep(6)

        print("Game starts in ")
        for i in range(5):
            print(f"{5 - i}.. ", end = "")
            sleep(1)
        print()
        sleep(2)

        clear_out()

        board = {
            'row1': [' ---', ' ---', ' ---'],
            'row2': ['|   |', '   ', '|   |'],
            'row3': [' ---', ' ---', ' ---'],
            'row4': ['|   |', '   ', '|   |'],
            'row5': [' ---', ' ---', ' ---'],
            'row6': ['|   |', '   ', '|   |'],
            'row7': [' ---', ' ---', ' ---'],
        }

        display(board)

        player_choice = "-1"
        while player_choice not in [player1, player2]:
            player_choice = input(f"Who is playing first ?{player1} or {player2} ")
            if player_choice not in [player1, player2]:
                print(f'Enter valid name..')

        while True:
            user_choice = input("Do you wanna be X or O ? ").title()
            if validate_choice(user_choice, ['X', 'O']):
                break

        wintie = False
        cell_list = list(range(1, 10))

        while not wintie:
            while True:
                try:
                    cell = int(input(f"Choose a cell from {cell_list} : "))
                    if validate_cell(cell, cell_list):
                        cell_list.remove(cell)
                        break
                except ValueError:
                    print(f'Invalid input! Plases choose a valid cell..')

            update(board, cell, user_choice)
            display(board)
            wintie, player = WinTie(board, player_choice, user_choice)
        #    clear_out()

            if wintie:
                print(f'Congo!!! {player} has won')
                break

            player_choice = update_pl(player_choice)
            user_choice = update_us(user_choice)

            if len(cell_list) == 0:
                print("Oops!! Game has come to end.\nIt's a tie")
                break

        game_on = gameon_choice()


else:
    print("No worries!! You can always comeback if you feel like playing")







