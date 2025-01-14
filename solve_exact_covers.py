import numpy as np

t_matrix = np.array([[0, 0, 1, 0, 1, 1, 0],
                     [1, 0, 0, 1, 0, 0, 1],
                     [0, 1, 1, 0, 0, 1, 0],
                     [1, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1],
                     [0, 0, 0, 1, 1, 0, 1],
                     [0, 1, 0, 0, 0, 0, 1] 
                    ])

def solve_exact_cover(matrix):
    row_identifiers = np.arange(1, matrix.shape[0] + 1).reshape(-1, 1)
    matrix_with_ids = np.hstack((row_identifiers, matrix))

    solutions = []
    recursive_solver(matrix_with_ids, set(), solutions)
    return solutions

def recursive_solver(matrix, partial_solution, solutions):
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

        rows_to_delete = set()
        columns_to_delete = set()

        for j in range(1, columns):
            if matrix[row_idx, j] == 1:
                columns_to_delete.add(j)
                for i in range(rows):
                    if matrix[i, j] == 1:
                        rows_to_delete.add(i)

        reduced_matrix = np.delete(matrix, list(rows_to_delete), axis=0)
        reduced_matrix = np.delete(reduced_matrix, list(columns_to_delete), axis=1)

        recursive_solver(reduced_matrix, new_partial_solution, solutions)


print(solve_exact_cover(t_matrix))
