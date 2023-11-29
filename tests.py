# tests.py
import unittest
import logic

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        logic.initialize_game()

    def test_initial_board_empty(self):
        self.assertEqual(logic.display_board(), "   |   |   \n   |   |   \n   |   |   ")

    def test_make_move(self):
        self.assertTrue(logic.make_move(0, 0))
        self.assertEqual(logic.display_board(), "X  |   |   \n   |   |   \n   |   |   ")
        self.assertTrue(logic.make_move(1, 1))
        self.assertEqual(logic.display_board(), "X  |   |   \n   | O |   \n   |   |   ")

    def test_invalid_move(self):
        logic.make_move(0, 0)
        self.assertFalse(logic.make_move(0, 0))  # Same spot

    def test_winner_row(self):
        logic.make_move(0, 0)  # X
        logic.make_move(1, 1)  # O
        logic.make_move(0, 1)  # X
        logic.make_move(1, 2)  # O
        logic.make_move(0, 2)  # X wins
        self.assertTrue(logic.check_winner())
        self.assertEqual(logic.get_winner(), "X")

    def test_winner_column(self):
        logic.make_move(0, 0)  # X
        logic.make_move(0, 1)  # O
        logic.make_move(1, 0)  # X
        logic.make_move(1, 1)  # O
        logic.make_move(2, 2)  # X
        logic.make_move(2, 1)  # O wins
        self.assertTrue(logic.check_winner())
        self.assertEqual(logic.get_winner(), "O")

    def test_winner_diagonal(self):
        logic.make_move(0, 0)  # X
        logic.make_move(0, 1)  # O
        logic.make_move(1, 1)  # X
        logic.make_move(1, 0)  # O
        logic.make_move(2, 2)  # X wins
        self.assertTrue(logic.check_winner())
        self.assertEqual(logic.get_winner(), "X")

    def test_draw(self):
        moves = [(0, 0), (0, 1), (0, 2),
                 (1, 1), (1, 0), (1, 2),
                 (2, 2), (2, 0), (2, 1)]
        for move in moves:
            logic.make_move(*move)
        self.assertTrue(logic.game_over())
        self.assertIsNone(logic.get_winner())

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
