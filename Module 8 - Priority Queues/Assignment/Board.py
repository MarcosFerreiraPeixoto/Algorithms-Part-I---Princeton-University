from typing import List
from copy import copy

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
                if self._board[i][j] != self._goal_board[i][j]:
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
            neighbor_matrix = copy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i-1][j] = neighbor_matrix[i][j], neighbor_matrix[i-1][j]

            neighbors.append(Board(neighbor_matrix))

        if i != self.n:
            neighbor_matrix = copy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i+1][j] = neighbor_matrix[i][j], neighbor_matrix[i+1][j]

            neighbors.append(Board(neighbor_matrix))
        
        if j != 0:
            neighbor_matrix = copy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i][j-1] = neighbor_matrix[i][j-1], neighbor_matrix[i][j]

            neighbors.append(Board(neighbor_matrix))

        if i != self.n:
            neighbor_matrix = copy(self._board)
            neighbor_matrix[i][j], neighbor_matrix[i+1][j] = neighbor_matrix[i][j], neighbor_matrix[i+1][j]

            neighbors.append(Board(neighbor_matrix))
        


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
            raise TypeError("Must compare boards!!")
        return self._board == other._board
    
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._board)