from sudoku_alg_x import solve_sudoku_matrix_exact_cover, translate_solution_to_sudoku
from sudoku_helper import generate_filled_sudoku, print_sudoku_grid, sudoku_grid_to_sudoku_string
import random

def count_non_zero_elements(grid):
    count = 0
    for row in grid:
        for value in row:
            if value != 0:
                count += 1
    return count

def generate_sudoku_puzzle(threshold=40):
    while True:
        sudoku_grid = generate_filled_sudoku()
        previous = (-1, -1, -1)
        filled_coords = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(filled_coords)

        while len(solve_sudoku_matrix_exact_cover(sudoku_grid)) == 1:
            row, col = filled_coords.pop()
            num = sudoku_grid[row, col]
            sudoku_grid[row, col] = 0
            previous = (row, col, num)
        
        row, col, num = previous
        sudoku_grid[row, col] = num

        if count_non_zero_elements(sudoku_grid) < threshold:
            break

    return sudoku_grid

def generate_sudoku_to_txt(n, filename):
    with open(filename, 'w') as f:
        for i in range(n):
            print("Generating puzzle " + str(i + 1) + "...")
            puzzle = sudoku_grid_to_sudoku_string(generate_sudoku_puzzle())
            f.write(puzzle + '\n')

generate_sudoku_to_txt(5, "t_output.txt")