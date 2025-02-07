import numpy as np

def print_cycle(matrix):
    print(matrix)
    print(matrix.shape)
    print("")

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print_cycle(matrix)

matrix = np.delete(matrix, 1, axis=0)

print_cycle(matrix)

matrix = np.delete(matrix, [0,1,2,3], axis=1)

print_cycle(matrix)