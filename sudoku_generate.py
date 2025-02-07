from sudoku_alg_x import solve_sudoku_matrix_exact_cover, translate_solution_to_sudoku
from sudoku_helper import generate_filled_sudoku, print_sudoku_grid, sudoku_grid_to_sudoku_string
import random
from copy import deepcopy

def count_non_zero_elements(grid):
    count = 0
    for row in grid:
        for value in row:
            if value != 0:
                count += 1
    return count

def generate_sudoku_puzzle():
    sudoku_grid = generate_filled_sudoku()
    
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    while positions:
        r, c = positions.pop()
        temp = sudoku_grid[r][c]
        sudoku_grid[r][c] = 0

        test_grid = deepcopy(sudoku_grid)
        if len(solve_sudoku_matrix_exact_cover(test_grid)) > 1:
            sudoku_grid[r][c] = temp
    
    return sudoku_grid

def generate_sudoku_to_txt(n, filename):
    with open(filename, 'w') as f:
        for i in range(n):
            print("Generating puzzle " + str(i + 1) + "...")
            puzzle = sudoku_grid_to_sudoku_string(generate_sudoku_puzzle())
            f.write(puzzle + '\n')

generate_sudoku_to_txt(50, "50.txt")