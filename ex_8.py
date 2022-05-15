import numpy as np


def ex_numpy_eight(nums, n, r):
    """
    Function to program to multiply two given arrays of same size element-by-element.
    """
    if r == "<":
        print(np.where(nums < n, r, nums))
    elif r == "=":
        print(np.where(nums == n, r, nums))
    elif r == ">":
        print(np.where(nums > n, r, nums))
