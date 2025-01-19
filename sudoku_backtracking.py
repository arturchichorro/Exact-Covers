import time
import numpy as np
from sudoku_helper import sudoku_string_to_sudoku_grid, print_sudoku_grid

def solve_sudoku(sudoku_grid):
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

hard_sudoku = ".16.8..4....5.3...3...2......3...96.7.......8.49...3..........1...9.5....3..4265."
counter_backtracking_sudoku = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

grid = sudoku_string_to_sudoku_grid(hard_sudoku)

start_time = time.time()
solve_sudoku(grid)
end_time = time.time()

print_sudoku_grid(grid)
print("Elapsed time: ", end_time - start_time)
