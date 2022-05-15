import numpy as np


def ex_numpy():
    """
    Function creates a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
    """
    x = np.arange(10, 20)
    print(x)
    x[9:16] *= -1
    print(x)
