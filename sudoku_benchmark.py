import numpy as np
import time
import matplotlib.pyplot as plt
from sudoku_alg_x import translate_solution_to_sudoku, solve_sudoku_exact_cover
from sudoku_backtracking import sudoku_string_to_sudoku_grid, solve_sudoku_backtracking
from sudoku_helper import print_sudoku_string, print_sudoku_grid


def benchmark_sudokus(sudoku_strings):

    backtrack_times = []
    alg_x_times = []

    for method in ["Backtracking", "Algorithm X"]:
        print("Method: ", method)
        for i, sudoku_string in enumerate(sudoku_strings):
            if method == "Backtracking":
                start_time = time.time()
                grid = sudoku_string_to_sudoku_grid(sudoku_string)
                solve_sudoku_backtracking(grid)
                end_time = time.time()
                backtrack_times.append(end_time - start_time)
            else:
                start_time = time.time()
                translate_solution_to_sudoku(solve_sudoku_exact_cover(sudoku_string))
                end_time = time.time()
                alg_x_times.append(end_time - start_time)
            print("Solved: ", i+1, "/", len(sudoku_strings))

    return backtrack_times, alg_x_times

def plot_benchmark_results(sudoku_strings, backtrack_times, alg_x_times):
    x_labels = [f"Sudoku {i + 1}" for i in range(len(sudoku_strings))]
    x_positions = range(len(sudoku_strings))
    
    plt.figure(figsize=(10, 6))
    plt.bar([x - 0.2 for x in x_positions], backtrack_times, width=0.4, label="Backtracking", color="blue")
    plt.bar([x + 0.2 for x in x_positions], alg_x_times, width=0.4, label="Algorithm X", color="orange")
    plt.xticks(x_positions, x_labels, rotation=45, ha="right")
    plt.xlabel("Sudoku Strings")
    plt.ylabel("Time (seconds)")
    plt.title("Sudoku Solver Benchmark: Backtracking vs Algorithm X")
    plt.legend()
    plt.tight_layout()
    plt.show()

sudoku_string = ".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"
sudoku_string2 = "2.6.51.7.5.87.6..94.......1.49..58..375.481..82.3.97.51..6..9....48.32..7.2.....3"
diabolical_sudoku = "..43......5...91.4...1....6......8..61..9...5..8.23......2.753.5.....6.7...4.5..."
extreme_sudoku = "7..1....9.2.3..7..4.9.......6.8..2............7...1.5......49...46..5..2.1...68.."
hardest_sudoku = "...1.2....6.....7...8...9..4.......3.5...7...2...8...1..9...8.5.7.....6....3.4..."
very_hard_sudoku = ".16.8..4....5.3...3...2......3...96.7.......8.49...3..........1...9.5....3..4265."
counter_backtracking_sudoku = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

sudoku_string_arr = [
    sudoku_string,
    sudoku_string2,
    diabolical_sudoku,
    extreme_sudoku,
    # hardest_sudoku,
    very_hard_sudoku,
    # counter_backtracking_sudoku,
]

backtrack_times, alg_x_times = benchmark_sudokus(sudoku_string_arr)
plot_benchmark_results(sudoku_string_arr, backtrack_times, alg_x_times)