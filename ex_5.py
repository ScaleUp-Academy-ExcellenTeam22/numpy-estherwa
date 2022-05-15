import numpy as np


def ex_numpy_fifth(matrix, vector):
    """
    Function to add a vector to each row of a given matrix.
    """
    result = np.empty_like(matrix)
    for row in range(4):
        result[row, :] = matrix[row, :] + vector

    print(result)
