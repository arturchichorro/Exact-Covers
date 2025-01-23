import numpy as np
import random

def sudoku_grid_to_sudoku_string(sudoku_grid):
    return ''.join(str(cell) if cell != 0 else '.' for row in sudoku_grid for cell in row)

def sudoku_string_to_sudoku_grid(sudoku_string):
    return np.array([int(char) if char != '.' else 0 for char in sudoku_string]).reshape(9, 9)

def print_sudoku_string(sudoku_string):
    if len(sudoku_string) != 81 or not all(c in '123456789.' for c in sudoku_string):
        return
    
    for i in range(9):
        row = sudoku_string[i * 9:(i + 1) * 9]
        formatted_row = " | ".join(row[j:j + 3] for j in range(0, 9, 3))
        print(formatted_row)
        if i % 3 == 2 and i < 8:
            print("-" * 15)

def print_sudoku_grid(sudoku_grid):
    for i, row in enumerate(sudoku_grid):
        formatted_row = " | ".join(
            "".join(str(num) if num != 0 else '.' for num in row[j:j + 3])
            for j in range(0, 9, 3)
        )
        print(formatted_row)
        if i % 3 == 2 and i < 8:
            print("-" * 15)

def is_valid_placement(sudoku_grid, row, col, num):
        if num in sudoku_grid[row, :]:
            return False
        if num in sudoku_grid[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in sudoku_grid[start_row:start_row+3, start_col:start_col+3]:
            return False
        return True

def generate_filled_sudoku():
    """Generate a fully filled Sudoku board."""
    def fill_grid(grid):
        """Fill the grid recursively using backtracking."""
        for row in range(9):
            for col in range(9):
                if grid[row, col] == 0:
                    random_numbers = random.sample(range(1, 10), 9)
                    for num in random_numbers:
                        if is_valid_placement(grid, row, col, num):
                            grid[row, col] = num
                            if fill_grid(grid):
                                return True
                            grid[row, col] = 0
                    return False
        return True

    grid = np.zeros((9, 9), dtype=int)
    fill_grid(grid)
    return grid