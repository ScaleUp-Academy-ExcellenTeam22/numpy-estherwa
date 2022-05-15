import numpy as np


def ex_numpy(x):
    """
    Function creates a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
    """

    x[9:16] *= -1
    print(x)
