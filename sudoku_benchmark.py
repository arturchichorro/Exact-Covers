import numpy as np
import time
import matplotlib.pyplot as plt
from sudoku_alg_x import translate_solution_to_sudoku, solve_sudoku_string_exact_cover
from sudoku_backtracking import solve_sudoku_backtracking
from sudoku_helper import sudoku_string_to_sudoku_grid, print_sudoku_string, print_sudoku_grid, count_nums_sudoku_strings


def benchmark_sudokus(sudoku_strings):
    backtrack_times = []
    alg_x_times = []
    
    print("Benchmarking Backtracking...")
    for i, sudoku_string in enumerate(sudoku_strings):
        start_time = time.perf_counter()
        grid = sudoku_string_to_sudoku_grid(sudoku_string)
        solve_sudoku_backtracking(grid)
        end_time = time.perf_counter()
        backtrack_times.append(end_time - start_time)
        print("Solved: ", i+1, "/", len(sudoku_strings))

    print("Benchmarking Alg X...")
    for i, sudoku_string in enumerate(sudoku_strings):
        start_time = time.perf_counter()
        translate_solution_to_sudoku(solve_sudoku_string_exact_cover(sudoku_string))
        end_time = time.perf_counter()
        alg_x_times.append(end_time - start_time)
        print("Solved: ", i+1, "/", len(sudoku_strings))
    
    return backtrack_times, alg_x_times

def plot_benchmark_results(sudoku_strings, backtrack_times, alg_x_times):
    """Plot benchmark results for Sudoku solving methods."""
    num_sudokus = len(sudoku_strings)
    x_positions = range(num_sudokus)
    bar_width = 0.4

    if num_sudokus > 20:
        print("Aggregating results for visualization...")
        batch_size = max(num_sudokus // 20, 1)
        x_labels = [f"{i * batch_size + 1}-{(i + 1) * batch_size}" for i in range(len(backtrack_times) // batch_size)]
        backtrack_times = [sum(backtrack_times[i:i+batch_size]) / batch_size for i in range(0, num_sudokus, batch_size)]
        alg_x_times = [sum(alg_x_times[i:i+batch_size]) / batch_size for i in range(0, num_sudokus, batch_size)]
        x_positions = range(len(backtrack_times))
    else:
        x_labels = [f"Sudoku {i + 1}" for i in range(num_sudokus)]

    plt.figure(figsize=(10, 6))
    plt.bar([x - bar_width / 2 for x in x_positions], backtrack_times, width=bar_width, label="Backtracking", color="blue")
    plt.bar([x + bar_width / 2 for x in x_positions], alg_x_times, width=bar_width, label="Algorithm X", color="orange")
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
hard_sudoku1 = ".7.1.........8.4....3.6.....1...6......5...984...21.5.......7.9...3.4.1..69.....3"
invalid_sudoku = "11.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"

sudoku_strings = [
    # sudoku_string,
    sudoku_string2,
    # diabolical_sudoku,
    # extreme_sudoku,
    # hardest_sudoku,
    # very_hard_sudoku,
    # counter_backtracking_sudoku,
]

filename = "50.txt"

lengths = count_nums_sudoku_strings(filename)
print("Filled cells per sudoku:")
for i in range(len(lengths)):
    print(i+1, ": ", lengths[i])

with open(filename, "r") as file:
    sudoku_strings = [line.strip() for line in file if line.strip()]

backtrack_times, alg_x_times = benchmark_sudokus(sudoku_strings)
print(backtrack_times, alg_x_times)
plot_benchmark_results(sudoku_strings, backtrack_times, alg_x_times)

# print(sudoku_strings)

# for sol in translate_solution_to_sudoku(solve_sudoku_string_exact_cover(invalid_sudoku)):
#     print_sudoku_string(sol)

# print(translate_solution_to_sudoku(solve_sudoku_string_exact_cover(".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2")))