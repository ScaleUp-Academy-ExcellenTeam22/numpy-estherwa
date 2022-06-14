import numpy as np


def ex_numpy_fifteen():
    """
     A NumPy program to create a three-dimension array with a specific shape .
    """
    np.random.seed(32)
    array = np.random.randint(0, 256, size=(300, 400, 5), dtype=np.uint8)
    return array
