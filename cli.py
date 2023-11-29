# cli.py
import logic

def main():
    logic.initialize_game()
    while not logic.game_over():
        print(logic.display_board())
        print(f"Current turn: {logic.turn()}")
        row, col = map(int, input("Enter your move (row col): ").split())
        if not logic.make_move(row, col):
            print("Invalid move. Try again.")
        else:
            print("Move registered.")
            if logic.check_winner():
                print(f"Game Over. {logic.get_winner()} wins!")
                break
    else:
        print("Game is a draw.")
    logic.record_game_result()

if __name__ == "__main__":
    main()
