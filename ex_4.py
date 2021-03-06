import numpy as np


def ex_numpy_forth(x):
    """
    A function that creates a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
    """
    x = np.ones((10, 10))
    x[1:-1, 1:-1] = 0
    return x
