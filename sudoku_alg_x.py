import numpy as np
from math import sqrt
from alg_x import solve, choose_row, solve_and_count
from sudoku_helper import print_sudoku_grid, sudoku_string_to_sudoku_grid

def _one_constraint(row, size):
    return row // size

def _row_constraint(row, size):
    return size**2 + size * (row // (size**2)) + row % size

def _col_constraint(row, size):
    return 2 * (size**2) + (row % (size**2))

def _box_constraint(row, size):
    return (int(3 * (size**2)
                + (row // (sqrt(size) * size**2)) * (size * sqrt(size))
                + ((row // (sqrt(size) * size)) % sqrt(size)) * size
                + (row % size)))

def empty_sudoku_exact_cover(size=9):
    constraints, rows = 4 * (size**2), size**3
    matrix = []
    for r in range(rows):
        row = np.zeros(constraints, dtype=int)
        positions = [
            _one_constraint(r, size),
            _row_constraint(r, size), 
            _col_constraint(r, size), 
            _box_constraint(r, size)
        ]
        row[positions] = 1
        matrix.append(row)

    numbered_column = np.arange(1, rows + 1, dtype=int).reshape(-1, 1)
    return np.hstack((numbered_column, matrix))

def sudoku_string_to_exact_cover(sudoku_string):
    size = int(sqrt(len(sudoku_string)))
    if size != 9:
        return

    empty_sudoku = empty_sudoku_exact_cover()
    partial_solution = set()
    for i, char in enumerate(sudoku_string):
        if char == "." or char == "0":
            continue

        row_id = (i // 9) * 81 + (i % 9) * 9 + int(char)
        partial_solution.add(row_id)

    sudoku_matrix = empty_sudoku.copy()
    for row_id in partial_solution:
        sudoku_matrix = choose_row(sudoku_matrix, np.where(sudoku_matrix[:, 0] == row_id)[0][0])

    return sudoku_matrix, partial_solution

def sudoku_matrix_to_exact_cover(sudoku_matrix):
    size = sudoku_matrix.shape[0]
    if size != 9 or sudoku_matrix.shape[1] != 9:
        return
    empty_sudoku = empty_sudoku_exact_cover()
    partial_solution = set()

    for row in range(9):
        for col in range(9):
            num = sudoku_matrix[row, col]
            if num == 0:
                continue

            row_id = row * 81 + col * 9 + num
            partial_solution.add(row_id)

    sudoku_exact_cover = empty_sudoku.copy()
    for row_id in partial_solution:
        sudoku_exact_cover = choose_row(sudoku_exact_cover, np.where(sudoku_exact_cover[:, 0] == row_id)[0][0])

    return sudoku_exact_cover, partial_solution

def solve_sudoku_string_exact_cover(sudoku_string):
    sudoku_matrix, partial_solution = sudoku_string_to_exact_cover(sudoku_string)
    solutions = []
    solve(sudoku_matrix, partial_solution, solutions)
    return solutions

def solve_sudoku_matrix_exact_cover(sudoku_grid):
    sudoku_matrix, partial_solution = sudoku_matrix_to_exact_cover(sudoku_grid)
    solutions = []
    solve(sudoku_matrix, partial_solution, solutions)
    return solutions

def translate_solution_to_sudoku(solutions):
    result = []
    for sol in solutions:
        sudo_string = ""
        sorted_sol = sorted(sol)
        for i, e in enumerate(sorted_sol):
            if i == 0:
                sudo_string += str(e)
                continue
            sudo_string += str(e % (9 * i)) if e % (9 * i) != 0 else "9"
        result.append(sudo_string)
    
    return result

def solve_sudoku_string_exact_cover_w_counts(sudoku_string):
    sudoku_matrix, partial_solution = sudoku_string_to_exact_cover(sudoku_string)
    solutions = []
    node_counter = [0]

    solve_and_count(sudoku_matrix, partial_solution, solutions, node_counter)

    return solutions, node_counter[0]

