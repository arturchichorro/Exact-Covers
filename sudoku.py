import numpy as np
from math import sqrt
from alg_x import solve_exact_cover, solve, choose_row

def sudoku_grid_to_sudoku_string(sudoku_grid):
    return ''.join(str(cell) if cell != 0 else '.' for row in sudoku_grid for cell in row)

def sudoku_string_to_sudoku_grid(sudoku_string):
    return np.array([int(char) if char != '.' else 0 for char in sudoku_string]).reshape(9, 9)

def print_sudoku_board(sudoku_string):
    if len(sudoku_string) != 81 or not all(c in '123456789.' for c in sudoku_string):
        return
    
    for i in range(9):
        row = sudoku_string[i * 9:(i + 1) * 9]
        formatted_row = " | ".join(row[j:j + 3] for j in range(0, 9, 3))
        print(formatted_row)
        if i % 3 == 2 and i < 8:
            print("-" * 15)

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

def sudoku_to_exact_cover(sudoku_string):
    size = int(sqrt(len(sudoku_string)))
    if size != 9:
        return

    empty_sudoku = empty_sudoku_exact_cover()
    partial_solution = set()
    for i, char in enumerate(sudoku_string):
        if char == ".":
            continue

        row_id = (i // 9) * 81 + (i % 9) * 9 + int(char)
        partial_solution.add(row_id)

    sudoku_matrix = empty_sudoku.copy()
    for row_id in partial_solution:
        sudoku_matrix = choose_row(sudoku_matrix, np.where(sudoku_matrix[:, 0] == row_id)[0][0])

    return sudoku_matrix, partial_solution

def solve_sudoku_exact_cover(sudoku_string):
    sudoku_matrix, partial_solution = sudoku_to_exact_cover(sudoku_string)
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

t_matrix = np.array([
                     [0, 0, 1, 0, 1, 1, 0],
                     [1, 0, 0, 1, 0, 0, 1],
                     [0, 1, 1, 0, 0, 1, 0],
                     [1, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1],
                     [0, 0, 0, 1, 1, 0, 1],
                    ])

sudoku_grid_example = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

sudoku_string = ".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"
sudoku_string2 = "2.6.51.7.5.87.6..94.......1.49..58..375.481..82.3.97.51..6..9....48.32..7.2.....3"
diabolical_sudoku = "..43......5...91.4...1....6......8..61..9...5..8.23......2.753.5.....6.7...4.5..."

# start_time = time.time()
# print(solve_sudoku_exact_cover(sudoku_string))
# end_time = time.time()

# print(end_time - start_time, "seconds")
sudoku_sols = [i for input_data in [diabolical_sudoku] for i in translate_solution_to_sudoku(solve_sudoku_exact_cover(input_data))]

for sol in sudoku_sols:
    print_sudoku_board(sol)