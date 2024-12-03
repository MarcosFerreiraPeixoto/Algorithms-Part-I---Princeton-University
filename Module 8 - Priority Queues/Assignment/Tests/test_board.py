import unittest
from Board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        # Initial configurations for tests
        self.board_2x2 = Board([[1, 0], [3, 2]])
        self.goal_board_2x2 = Board([[1, 2], [3, 0]])
        self.board_3x3 = Board([[8, 1, 3], [4, 0, 2], [7, 6, 5]])

    def test_dimension(self):
        self.assertEqual(self.board_2x2.dimension(), 2)
        self.assertEqual(self.board_3x3.dimension(), 3)

    def test_hamming(self):
        self.assertEqual(self.board_2x2.hamming(), 1)  # Two tiles out of place
        self.assertEqual(self.goal_board_2x2.hamming(), 0)

    def test_manhattan(self):
        self.assertEqual(self.board_2x2.manhattan(), 1)
        self.assertEqual(self.goal_board_2x2.manhattan(), 0)

    def test_is_goal(self):
        self.assertFalse(self.board_2x2.is_goal())
        self.assertTrue(self.goal_board_2x2.is_goal())

    def test_neighbors(self):
        neighbors = list(self.board_2x2.neighbors())
        self.assertEqual(len(neighbors), 2)  # Two neighbors in a corner for 2x2 board
        neighbor_boards = [neighbor._board for neighbor in neighbors]
        self.assertIn([[0, 1], [3, 2]], neighbor_boards)
        self.assertIn([[1, 2], [3, 0]], neighbor_boards)

    def test_twin(self):
        twin_board = self.board_2x2.twin()
        self.assertNotEqual(twin_board._board, self.board_2x2._board)
        self.assertIn(twin_board._board, [
            [[1, 0], [2, 3]], 
            [[3, 0], [1, 2]]
        ])  # Valid twins for 2x2 board

    def test_equality(self):
        self.assertEqual(self.board_2x2, Board([[1, 0], [3, 2]]))
        self.assertNotEqual(self.board_2x2, self.goal_board_2x2)

    def test_string_representation(self):
        expected_string = "2\n1 0\n3 2"
        self.assertEqual(str(self.board_2x2), expected_string)

    def test_large_board(self):
        large_board = Board([[i * 4 + j + 1 for j in range(4)] for i in range(4)])
        self.assertEqual(large_board.dimension(), 4)

if __name__ == "__main__":
    unittest.main()
