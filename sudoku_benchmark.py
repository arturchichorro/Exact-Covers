import numpy as np
import time
from sudoku_alg_x import translate_solution_to_sudoku, solve_sudoku_exact_cover
from sudoku_backtracking import sudoku_string_to_sudoku_grid, solve_sudoku_backtracking
from sudoku_helper import print_sudoku_string, print_sudoku_grid

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
extreme_sudoku = "7..1....9.2.3..7..4.9.......6.8..2............7...1.5......49...46..5..2.1...68.."
hardest_sudoku = "...1.2....6.....7...8...9..4.......3.5...7...2...8...1..9...8.5.7.....6....3.4..."
very_hard_sudoku = ".16.8..4....5.3...3...2......3...96.7.......8.49...3..........1...9.5....3..4265."
counter_backtracking_sudoku = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

grid = sudoku_string_to_sudoku_grid(very_hard_sudoku)

start_time = time.time()
solve_sudoku_backtracking(grid)
end_time = time.time()

print_sudoku_grid(grid)
print("Method: Backtracking; Elapsed time: ", end_time - start_time)

start_time = time.time()
sudoku_sols = [i for input_data in [counter_backtracking_sudoku] for i in translate_solution_to_sudoku(solve_sudoku_exact_cover(input_data))]
end_time = time.time()

for sol in sudoku_sols:
    print_sudoku_string(sol)

print("Method: Algorithm X; Elapsed time: ", end_time - start_time)