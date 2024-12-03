from typing import List
from copy import deepcopy
from random import choice

class Board():
    def __init__(self, matrix: List[List[int]]):
        self._board = matrix
        self.n = len(matrix)
        self._goal_board = self._generate_goal_board()

    def dimension(self):
        return self.n
    
    def hamming(self):
        hamming = 0

        for i in range(self.n):
            for j in range(self.n):
                if self._board[i][j] != 0 and self._board[i][j] != self._goal_board[i][j]:
                    hamming += 1

        return hamming
    
    def manhattan(self):
        manhattan = 0

        for i in range(self.n):
            for j in range(self.n):
                value = self._board[i][j]
                expected_value = self._goal_board[i][j]

                if value != 0 and value != expected_value:
                    if expected_value != 0:
                        diff = abs(value - expected_value)
                    else:
                        diff = abs(value - self.n**2)
                    manhattan += diff//self.n + diff%self.n

        return manhattan

    def is_goal(self):
        return self._board == self._goal_board

    def neighbors(self):
        neighbors = []
        i, j = self._get_zero_position()

        if i != 0:
            neighbor_matrix = deepcopy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i-1][j] = neighbor_matrix[i-1][j], neighbor_matrix[i][j]

            neighbors.append(Board(neighbor_matrix))

        if i != (self.n - 1):
            neighbor_matrix = deepcopy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i+1][j] = neighbor_matrix[i+1][j], neighbor_matrix[i][j]

            neighbors.append(Board(neighbor_matrix))
        
        if j != 0:
            neighbor_matrix = deepcopy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i][j-1] = neighbor_matrix[i][j-1], neighbor_matrix[i][j]

            neighbors.append(Board(neighbor_matrix))

        if j != (self.n - 1):
            neighbor_matrix = deepcopy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i][j+1] = neighbor_matrix[i][j + 1], neighbor_matrix[i][j]

            neighbors.append(Board(neighbor_matrix))
        
        return neighbors

    def twin(self):
        non_zero_positions = [
            (i, j) for i in range(self.n) for j in range(self.n) if self._board[i][j] != 0
        ]

        (i1, j1), (i2, j2) = choice(non_zero_positions), choice(non_zero_positions)
        while (i1, j1) == (i2, j2):
            (i2, j2) = choice(non_zero_positions)

        twin_board = deepcopy(self._board)
        twin_board[i1][j1], twin_board[i2][j2] = twin_board[i2][j2], twin_board[i1][j1]

        return Board(twin_board)

    def _get_zero_position(self):
        for i in range(self.n):
            for j in range(self.n):
                if self._board[i][j] == 0:
                    return i, j        
        
    def _generate_goal_board(self):
        nums = [0] + list(range(self.n**2 - 1, 0, -1))
        
        return [[nums.pop() for _ in range(self.n)] for _ in range(self.n)]

    def __eq__(self, other: 'Board'):
        if not isinstance(other, Board):
            return False
        return self._board == other._board
    
    def __str__(self):
        result = f"{self.n}\n"
        result += "\n".join(" ".join(map(str, row)) for row in self._board)
        return result