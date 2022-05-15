import numpy as np


def ex_numpy_third():
    """
    Function that finds the number of rows and columns of a given matrix.
    """
    m = np.arange(10, 22).reshape((3, 4))

    print(m)
    print(m.shape)
