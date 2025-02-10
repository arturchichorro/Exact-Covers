import numpy as np
from sudoku_helper import is_valid_placement

def solve_sudoku_backtracking(sudoku_grid):
    def backtrack(sudoku_grid):
        for row in range(9):
            for col in range(9):
                if sudoku_grid[row, col] == 0:
                    for num in range(1, 10):
                        if is_valid_placement(sudoku_grid, row, col, num):
                            sudoku_grid[row, col] = num
                            if backtrack(sudoku_grid):
                                return True
                            sudoku_grid[row, col] = 0
                    return False
        return True
    backtrack(sudoku_grid)

def solve_sudoku_backtracking_counting_nodes(sudoku_grid):
    node_counter = [0]

    def backtrack(sudoku_grid):
        node_counter[0] += 1
        for row in range(9):
            for col in range(9):
                if sudoku_grid[row, col] == 0:
                    for num in range(1, 10):
                        if is_valid_placement(sudoku_grid, row, col, num):
                            sudoku_grid[row, col] = num
                            if backtrack(sudoku_grid):
                                return True
                            sudoku_grid[row, col] = 0
                    return False
        return True

    backtrack(sudoku_grid)
    
    return node_counter[0]
