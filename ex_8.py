import numpy as np


def ex_numpy_eight(nums, n, replace):
    """
    Function to program to multiply two given arrays of same size element-by-element.
    """
    if replace == "<":
        print(np.where(nums < n, replace, nums))
    elif replace == "=":
        print(np.where(nums == n, replace, nums))
    elif replace == ">":
        print(np.where(nums > n, replace, nums))
