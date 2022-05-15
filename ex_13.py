import numpy as np


def ex_numpy_thirteen(a, b):
    """
     A NumPy program to convert (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
    """
    return np.dstack((a, b))
