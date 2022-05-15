import numpy as np


def ex_numpy_seven():
    """
    Function to compute the x and y coordinates for points on a sine curve.
    """
    nums = np.arange(1000, size=16).reshape(-1, 4)

    new_nums = nums[::-1]
    print(new_nums)
