import time
import numpy as np
from sudoku_helper import sudoku_string_to_sudoku_grid, print_sudoku_grid

def solve_sudoku_backtracking(sudoku_grid):
    def is_valid_placement(sudoku_grid, row, col, num):
        if num in sudoku_grid[row, :]:
            return False
        if num in sudoku_grid[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in sudoku_grid[start_row:start_row+3, start_col:start_col+3]:
            return False
        return True
    
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
