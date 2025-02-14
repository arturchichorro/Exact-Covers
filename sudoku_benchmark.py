import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sudoku_alg_x import translate_solution_to_sudoku, solve_sudoku_string_exact_cover, solve_sudoku_string_exact_cover_w_counts, solve_sudoku_matrix_exact_cover, solve_sudoku_string_exact_cover_w_counts_one_sol, translate_partial_sol_to_sudoku
from sudoku_backtracking import solve_sudoku_backtracking, solve_sudoku_backtracking_counting_nodes
from sudoku_helper import sudoku_string_to_sudoku_grid, print_sudoku_string, print_sudoku_grid, count_nums_sudoku_strings, is_valid_solved_grid


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

def benchmark_alg_x(sudoku_strings):
    alg_x_times = np.zeros(len(sudoku_strings))

    print("Benchmarking Alg X...")
    for i, sudoku_string in enumerate(sudoku_strings):
        start_time = time.perf_counter()
        translate_solution_to_sudoku(solve_sudoku_string_exact_cover(sudoku_string))
        end_time = time.perf_counter()
        alg_x_times[i] = end_time - start_time
        print("Solved: ", i+1, "/", len(sudoku_strings))

    mean = np.mean(alg_x_times)  
    median = np.median(alg_x_times) 
    std_dev = np.std(alg_x_times)
    variance = np.var(alg_x_times)
    minimum = np.min(alg_x_times)  
    maximum = np.max(alg_x_times)  
    sum_all = np.sum(alg_x_times)  

    print(f"Mean: {mean}, Median: {median}, Std Dev: {std_dev}, Variance: {variance}")
    print(f"Min: {minimum}, Max: {maximum}, Sum: {sum_all}")
    
    return alg_x_times

def verify_alg_x(sudoku_strings):
    invalid = []

    for i, sudoku_string in enumerate(sudoku_strings):

        sols = translate_solution_to_sudoku(solve_sudoku_string_exact_cover(sudoku_string))
        for s in sols:
            grid = sudoku_string_to_sudoku_grid(s)
            if is_valid_solved_grid(grid):
                invalid.append(i)
                print_sudoku_grid(grid)

        print("Solved: ", i+1, "/", len(sudoku_strings))
    
    return invalid

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

def benchmark_sudokus_w_count(sudoku_strings):
    results = []

    for i, sudoku_string in enumerate(sudoku_strings):
        grid = sudoku_string_to_sudoku_grid(sudoku_string)
        start_time = time.perf_counter()
        nodes_bt = solve_sudoku_backtracking_counting_nodes(grid)
        end_time = time.perf_counter()
        backtrack_time = end_time - start_time
        
        print(f"Solved {i+1}/{len(sudoku_strings)} with Backtracking in {backtrack_time:.6f}s using {nodes_bt} nodes.")
        start_time = time.perf_counter()
        solution, nodes_alg_x = solve_sudoku_string_exact_cover_w_counts(sudoku_string)
        translate_solution_to_sudoku(solution)
        end_time = time.perf_counter()
        alg_x_time = end_time - start_time

        print(f"Solved {i+1}/{len(sudoku_strings)} with Algorithm X in {alg_x_time:.6f}s using {nodes_alg_x} nodes.")

        speedup = backtrack_time / alg_x_time if alg_x_time > 0 else float('inf')
        node_efficiency = nodes_bt / nodes_alg_x if nodes_alg_x > 0 else float('inf')

        results.append({
            "Sudoku #": i + 1,
            "Backtracking Time (s)": backtrack_time,
            "Backtracking Nodes": nodes_bt,
            "Algorithm X Time (s)": alg_x_time,
            "Algorithm X Nodes": nodes_alg_x,
            "Speedup (Backtracking / Alg X)": speedup,
            "Node Efficiency (Backtracking / Alg X)": node_efficiency
        })

    df = pd.DataFrame(results)

    df.to_csv("sudoku_benchmark_results.csv", index=False)

    print(df.head())

    return df

def benchmark_alg_x_df(sudoku_strings):
    results = []

    for i, sudoku_string in enumerate(sudoku_strings):
        start_time = time.perf_counter()
        solution, nodes_alg_x = solve_sudoku_string_exact_cover_w_counts(sudoku_string)
        translate_solution_to_sudoku(solution)
        end_time = time.perf_counter()
        alg_x_time = end_time - start_time

        print(f"Solved {i+1}/{len(sudoku_strings)} with Algorithm X in {alg_x_time:.6f}s using {nodes_alg_x} nodes.")
        
        results.append({
            "Sudoku #": i,
            "Algorithm X Time (s)": alg_x_time,
            "Algorithm X Nodes": nodes_alg_x,
        })

    df = pd.DataFrame(results)

    df.to_csv("sudoku_alg_x_benchmark_results.csv", index=False)

    print(df.head())

    return df

def benchmark_alg_x_df_one_sol(sudoku_strings):
    results = []

    for i, sudoku_string in enumerate(sudoku_strings):
        start_time = time.perf_counter()
        psol, nodes_alg_x = solve_sudoku_string_exact_cover_w_counts_one_sol(sudoku_string)
        translate_partial_sol_to_sudoku(psol)
        end_time = time.perf_counter()
        alg_x_time = end_time - start_time

        print(f"Solved {i+1}/{len(sudoku_strings)} with Algorithm X in {alg_x_time:.6f}s using {nodes_alg_x} nodes.")
        
        results.append({
            "Sudoku #": i,
            "Algorithm X Time (s)": alg_x_time,
            "Algorithm X Nodes": nodes_alg_x,
        })

    df = pd.DataFrame(results)

    df.to_csv("sudoku_alg_x_benchmark_results.csv", index=False)

    print(df.head())

    return df

# sudoku_string = ".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"
# sudoku_string2 = "2.6.51.7.5.87.6..94.......1.49..58..375.481..82.3.97.51..6..9....48.32..7.2.....3"
# diabolical_sudoku = "..43......5...91.4...1....6......8..61..9...5..8.23......2.753.5.....6.7...4.5..."
# extreme_sudoku = "7..1....9.2.3..7..4.9.......6.8..2............7...1.5......49...46..5..2.1...68.."
# hardest_sudoku = "...1.2....6.....7...8...9..4.......3.5...7...2...8...1..9...8.5.7.....6....3.4..."
# very_hard_sudoku = ".16.8..4....5.3...3...2......3...96.7.......8.49...3..........1...9.5....3..4265."
# counter_backtracking_sudoku = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
# hard_sudoku1 = ".7.1.........8.4....3.6.....1...6......5...984...21.5.......7.9...3.4.1..69.....3"
# invalid_sudoku = "11.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2"

# sudoku_strings = [
#     # sudoku_string,
#     sudoku_string2,
#     # diabolical_sudoku,
#     # extreme_sudoku,
#     # hardest_sudoku,
#     # very_hard_sudoku,
#     # counter_backtracking_sudoku,
# ]


# for sol in translate_solution_to_sudoku(solve_sudoku_string_exact_cover(invalid_sudoku)):
#     print_sudoku_string(sol)

# print(translate_solution_to_sudoku(solve_sudoku_string_exact_cover(".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2")))

# filename = "50.txt"
# lengths = count_nums_sudoku_strings(filename)
# print("Filled cells per sudoku:")
# for i in range(len(lengths)):
#     print(i+1, ": ", lengths[i])

# with open(filename, "r") as file:
#     sudoku_strings = [line.strip() for line in file if line.strip()]

# backtrack_times, alg_x_times = benchmark_sudokus(sudoku_strings)
# print(backtrack_times, alg_x_times)
# plot_benchmark_results(sudoku_strings, backtrack_times, alg_x_times)

# print(sudoku_strings)



filename = "puzzles.txt"
with open(filename, "r") as file:
    sudoku_strings = [line.strip() for line in file if line.strip()]

# top_50_slowest = [45750, 21851, 45751, 41812, 41816, 30172, 48883, 34232, 23326, 20693, 41813, 39601, 41815, 41814, 48611, 12963, 45876, 28384, 44758, 14656, 33646, 40179, 16081, 46771, 14657, 4236, 16082, 46770, 48145, 25231, 34229, 20154, 42298, 18676, 46850, 46671, 13505, 17259, 6647, 14795, 19038, 1775, 20645, 20317, 43076, 20369, 25930, 45327, 29751, 10758]

# filtered_sudoku = [sudoku_strings[i] for i in top_50_slowest]
benchmark_alg_x_df_one_sol(sudoku_strings)

# hardest = sudoku_string_to_sudoku_grid(sudoku_strings[top_50_slowest[0]])
# print(hardest)
# print_sudoku_grid(hardest)