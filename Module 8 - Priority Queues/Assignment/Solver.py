import sys
from MinPQNoDuplicates import MinPQNoDuplicates
from Board import Board, BoardComparator
from typing import List, Optional

class Solver:
    def __init__(self, initial_board: Board):
        if not isinstance(initial_board, Board):
            raise TypeError("The input must be an instance of Board!")

        self.is_main_board_solvable: bool = True
        self.solution_path: Optional[List[Board]] = []
        self._solve(initial_board)

    def _solve(self, initial_board: Board):
        main_pq = MinPQNoDuplicates(BoardComparator())
        twin_pq = MinPQNoDuplicates(BoardComparator())
        main_pq.insert(initial_board)
        twin_pq.insert(initial_board.twin())

        while True:
            min_main_board = main_pq.del_min()
            min_twin_board = twin_pq.del_min()

            if min_main_board.is_goal():
                self._get_solution(min_main_board)
                break
            if min_twin_board.is_goal():
                self.is_main_board_solvable = False
                self.solution_path = None
                return

            self._add_neighbors_to_pq(main_pq, min_main_board)
            self._add_neighbors_to_pq(twin_pq, min_twin_board)

    def _add_neighbors_to_pq(self, pq: MinPQNoDuplicates, board: Board):
        for neighbor in board.neighbors():
            pq.insert(neighbor)

    def _get_solution(self, solution_board: Board):
        current_board = solution_board
    
        while current_board != None:
            self.solution_path.append(current_board)
            current_board = current_board.previous_board
        
        self.solution_path.reverse()
            
    def is_solvable(self) -> bool:
        return self.is_main_board_solvable

    def moves(self) -> int:
        if not self.is_main_board_solvable or self.solution_path is None:
            return -1
        return self.solution_path[-1].moves

    def solution(self) -> Optional[List[Board]]:
        return self.solution_path

def main():
    with open(sys.argv[1], 'r') as file:
        n = int(file.readline().strip())
        tiles = []
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            tiles.append(row)

    initial = Board(tiles)
    solver = Solver(initial)

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print(f"Minimum number of moves = {solver.moves()}")
        for board in solver.solution():
            print(board)

if __name__ == "__main__":
    main()
