from Board import Board
from Solver import Solver

def test_solver_solvable():
    board = Board([[1, 0], [3, 2]])
    goal_board = Board([[1, 2], [3, 0]])
    solver = Solver(board)
    
    assert solver.is_solvable(), "Solver should detect that the board is solvable."
    assert solver.moves() == 1, "Solver should find the solution in 1 move."
    solution = solver.solution()
    assert len(solution) == 2, "Solution should have 2 boards: initial and goal."
    assert solution[-1] == goal_board, "Solution should end with the goal board."

def test_solver_unsolvable():
    board = Board([
        [0, 2, 3],
        [1, 7, 5],
        [4, 8, 6]
    ])
    solver = Solver(board)
    
    assert not solver.is_solvable(), "Solver should detect that the board is unsolvable."
    assert solver.moves() == -1, "Solver should return -1 moves for unsolvable boards."
    assert solver.solution() is None, "Solver should return None for unsolvable boards."

def test_solver_with_goal_board():
    board = Board([[1, 2], [3, 0]])
    solver = Solver(board)
    
    assert solver.is_solvable(), "Goal board should be solvable."
    assert solver.moves() == 0, "No moves should be required for the goal board."
    assert solver.solution() == [board], "Solution should contain only the goal board."

def test_solver_invalid_input():
    try:
        Solver(None)
    except TypeError as e:
        assert str(e) == "The input must be an instance of Board!", "Solver should raise a TypeError for None input."

    try:
        Solver("Invalid")
    except TypeError as e:
        assert str(e) == "The input must be an instance of Board!", "Solver should raise a TypeError for non-Board input."
