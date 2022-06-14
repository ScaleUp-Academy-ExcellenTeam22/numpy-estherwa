import numpy as np


def ex_numpy_seven():
    """
    A function that creates an array with some values,
    and the function must create a new array and swap the first and the last rows.
  
    """
    nums = np.arange(1000, size=16).reshape(-1, 4)

    new_nums = nums[::-1]
    print(new_nums)
