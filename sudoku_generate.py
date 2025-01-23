from sudoku_alg_x import sudoku_matrix_to_exact_cover, solve_sudoku_exact_cover, translate_solution_to_sudoku
from sudoku_helper import generate_filled_sudoku, sudoku_grid_to_sudoku_string

# 1. Generate filled sudoku
# 2. Remove numbers
# 3. Check if len(solutions) == 1

def generate_sudoku_puzzle():

    filled_grid = generate_filled_sudoku()

    print(translate_solution_to_sudoku(solve_sudoku_exact_cover(sudoku_matrix_to_exact_cover(filled_grid))))
    
    print(filled_grid)



generate_sudoku_puzzle()