from math import sqrt
import numpy as np

def solve_exact_cover(matrix):
    """Exact Cover Solver
    Inputs: numpy matrix of 1s and 0s
    Outputs: List of sets with rows that are part of solution (1 indexed)
    
    Example input:
    np.array([
                     [0, 0, 1, 0, 1, 1, 0],
                     [1, 0, 0, 1, 0, 0, 1],
                     [0, 1, 1, 0, 0, 1, 0],
                     [1, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1],
                     [0, 0, 0, 1, 1, 0, 1],
                    ])
    Output: [{1, 4, 5}]
    """

    # Add identifier label to each row 
    row_identifiers = np.arange(1, matrix.shape[0] + 1).reshape(-1, 1)
    matrix_with_ids = np.hstack((row_identifiers, matrix))

    solutions = []
    _solve(matrix_with_ids, set(), solutions)
    return solutions

def _solve(matrix, partial_solution, solutions):
    rows, columns = matrix.shape
    # Base case: if only column with row identifiers remains, found solution
    if columns == 1:
        solutions.append(partial_solution)
        return
    # Choose column with least 1s
    column_sums = np.sum(matrix[:, 1:], axis=0)
    min_col_idx = np.argmin(column_sums) + 1
    candidate_rows = [r for r in range(rows) if matrix[r, min_col_idx] == 1]
    
    # If there aren't any valid rows, there's no solution here
    if not candidate_rows:
        return
    for row_idx in candidate_rows:
        new_partial_solution = partial_solution.copy()
        new_partial_solution.add(matrix[row_idx, 0])
        reduced_matrix = choose_row(matrix, row_idx, rows, columns)
        _solve(reduced_matrix, new_partial_solution, solutions)

def choose_row(matrix, row_idx, n_rows, n_columns):
    rows_to_delete = set()
    columns_to_delete = set()

    for j in range(1, n_columns):
        if matrix[row_idx, j] == 1:
            columns_to_delete.add(j)
            for i in range(n_rows):
                if matrix[i, j] == 1:
                    rows_to_delete.add(i)

    reduced_matrix = np.delete(matrix, list(rows_to_delete), axis=0)
    return np.delete(reduced_matrix, list(columns_to_delete), axis=1)

def sudoku_grid_to_sudoku_string(sudoku_grid):
    return ''.join(str(cell) if cell != 0 else '.' for row in sudoku_grid for cell in row)

def sudoku_string_to_sudoku_grid(sudoku_string):
    return np.array([int(char) if char != '.' else 0 for char in sudoku_string]).reshape(9,9)

def print_sudoku_board(sudoku_string):
    # invalid sudoku string
    if len(sudoku_string) != 81 or not all(c in '123456789.' for c in sudoku_string):
        return
    
    for i in range(9):
        row = sudoku_string[i * 9:(i + 1) * 9]
        formatted_row = " | ".join(row[j:j + 3] for j in range(0, 9, 3))
        print(formatted_row)
        if i % 3 == 2 and i < 8:
            print("-" * 15)

def _one_constraint(row: int, size:int) -> int:
    return row//size
def _row_constraint(row:int, size:int) -> int:
    return size**2 + size*(row//(size**2)) + row % size
def _col_constraint(row:int, size:int) -> int:
    return 2*(size**2) + (row % (size**2))
def _box_constraint(row:int, size:int) -> int:
    return (int(3*(size**2)
            + (row//(sqrt(size)*size**2))*(size*sqrt(size))
            + ((row//(sqrt(size)*size)) % sqrt(size))*size
            + (row % size)))

def empty_sudoku_exact_cover_matrix(size = 9):
    constraints, rows = 4 * (size ** 2), size ** 3
    matrix = [] 
    for r in range(rows):
        row = np.zeros(constraints)
        positions = [_one_constraint(r, size), _row_constraint(r, size), _col_constraint(r, size), _box_constraint(r, size), ]
        row[positions] = 1
        matrix.append(row)

    return np.array(matrix, dtype=int)

def sudoku_grid_to_exact_cover(sudoku_string):
    """Translates a sudoku board into a matrix of 1s and 0s to be solved as an Exact Cover problem
    Inputs: 81 character long string
    Outputs: numpy matrix of 1s and 0s 
    
    Example Input:
    ".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"
    """
    for c in sudoku_string:
        pass

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

# sudoku_string = ".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"
# print_sudoku_board(sudoku_string)

print(len(solve_exact_cover(empty_sudoku_exact_cover_matrix(4))))
