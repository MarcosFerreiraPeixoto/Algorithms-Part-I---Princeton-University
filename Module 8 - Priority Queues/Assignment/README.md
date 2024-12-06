# 8 Puzzle Solver

This project implements an AI solver for the **8-Puzzle problem** using the A* search algorithm. The 8-puzzle is a sliding puzzle consisting of a 3x3 grid with tiles numbered 1-8 and one empty space. The goal is to rearrange the tiles to reach the solved state.

## Features
- **Board Representation:** Encodes the puzzle board with efficient operations for tile sliding and neighbor generation.
- **A* Search Algorithm:** Finds the shortest solution path using Manhattan distance as a heuristic.
- **Solver API:** Determines solvability and outputs the sequence of moves to solve the puzzle.

## How to Run
1. Input a puzzle in text format.
2. Run the solver to get the solution steps or check if the puzzle is unsolvable.

For detailed implementation, see the [Coursera assignment](https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php).