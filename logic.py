# logic.py
import csv
import datetime

board = []
winner = None
current_player = "X"

def initialize_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

def display_board():
    return "\n".join([" | ".join(row) for row in board])

def make_move(row, col):
    global current_player
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = current_player
        current_player = "O" if current_player == "X" else "X"
        return True
    return False

def turn():
    return current_player

def check_winner():
    global winner
    # Check rows, columns and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            winner = board[i][0]
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            winner = board[0][i]
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        winner = board[0][2]
        return True
    return False

def get_winner():
    return winner

def game_over():
    return check_winner() or all(cell != " " for row in board for cell in row)

def record_game_result():
    with open('game_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), get_winner() or "Draw"])
