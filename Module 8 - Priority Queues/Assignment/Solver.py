from MinPQNoDuplicates import MinPQNoDuplicates
from Board import Board, BoardComparator
from typing import List

class Solver():
    def __init__(self, board: Board):
        if board is None or not isinstance(board, Board):
            raise TypeError("The input must be a Board type!")

        # Main solution
        self.is_main_board_solvable = True
        self.board_solution: List[Board] = []
        pq: MinPQNoDuplicates = MinPQNoDuplicates(BoardComparator())
        pq.insert(board)

        # Twin solution to check if board is solvable
        twin_board = board.twin()
        twin_pq: MinPQNoDuplicates = MinPQNoDuplicates(BoardComparator())
        twin_pq.insert(twin_board)
        print(twin_board)

        min_board_pq: Board = pq.del_min()
        min_twin_board_pq: Board = twin_pq.del_min()
        while not min_board_pq.is_goal() and not min_twin_board_pq.is_goal():
            self.board_solution.append(min_board_pq)

            neighbors: List[Board] = min_board_pq.neighbors()
            neighbors_twin: List[Board] = min_twin_board_pq.neighbors()

            for n in neighbors:
                pq.insert(n)

            for n in neighbors_twin:
                twin_pq.insert(n)

            min_board_pq: Board = pq.del_min()
            min_twin_board_pq: Board = twin_pq.del_min()

        if min_twin_board_pq.is_goal():
            self.is_main_board_solvable = False
            self.board_solution = None
            return

        self.board_solution.append(min_board_pq)

    def is_solvable(self):
        return self.is_main_board_solvable

    def moves(self):
        if self.board_solution is None:
            return -1
        return self.board_solution[-1].moves

    def solution(self):
        return self.board_solution