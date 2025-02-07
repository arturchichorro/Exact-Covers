import numpy as np

def solve_exact_cover(matrix):
    row_identifiers = np.arange(1, matrix.shape[0] + 1).reshape(-1, 1)
    matrix_with_ids = np.hstack((row_identifiers, matrix))

    solutions = []
    solve(matrix_with_ids, set(), solutions)
    return solutions

def solve(matrix, partial_solution, solutions):
    print(matrix)
    print(partial_solution)
    print(matrix.shape)
    print("")
    
    
    rows, columns = matrix.shape
    if columns == 1:
        solutions.append(partial_solution)
        return

    column_sums = np.sum(matrix[:, 1:], axis=0)
    min_col_idx = np.argmin(column_sums) + 1
    candidate_rows = [r for r in range(rows) if matrix[r, min_col_idx] == 1]

    if not candidate_rows:
        return

    for row_idx in candidate_rows:
        new_partial_solution = partial_solution.copy()
        new_partial_solution.add(matrix[row_idx, 0])
        reduced_matrix = choose_row(matrix, row_idx)
        solve(reduced_matrix, new_partial_solution, solutions)

def choose_row(matrix, row_idx):
    n_rows, n_columns = matrix.shape

    rows_to_delete = set()
    columns_to_delete = set()
    for j in range(1, n_columns):
        if matrix[row_idx, j] == 1:
            columns_to_delete.add(j)
            for i in range(n_rows):
                if matrix[i, j] == 1:
                    rows_to_delete.add(i)

    print("RC ", rows_to_delete, columns_to_delete)

    reduced_matrix = np.delete(matrix, list(rows_to_delete), axis=0)
    return np.delete(reduced_matrix, list(columns_to_delete), axis=1)


matrix = np.array([
    [0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1]
])

print(solve_exact_cover(matrix))