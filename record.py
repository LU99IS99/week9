import random

class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def make_move(self, position, symbol):
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == symbol for i in line) for line in lines)

    def is_full(self):
        return " " not in self.board


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        try:
            position = int(input(f"Player {self.symbol}, enter your move (0-8): "))
            return board.make_move(position, self.symbol)
        except ValueError:
            return False


class BotPlayer(Player):
    def make_move(self, board):
        position = random.choice([i for i, spot in enumerate(board.board) if spot == " "])
        return board.make_move(position, self.symbol)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        while True:
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            if not current_player.make_move(self.board):
                print("Invalid move, try again.")
                continue

            if self.board.check_winner(current_player.symbol):
                self.board.print_board()
                print(f"Player {current_player.symbol} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break

            self.switch_player()


if __name__ == "__main__":
    player1 = HumanPlayer("X")
    player2 = BotPlayer("O") if input("How many human players? (1/2): ") == "1" else HumanPlayer("O")
    game = Game(player1, player2)
    game.play()
