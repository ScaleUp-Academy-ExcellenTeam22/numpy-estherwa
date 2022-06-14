import numpy as np


def ex_numpy_fourteen(m1, m2):
    """
    A NumPy program to combine a one and a two-dimensional array together and display their elements.
    """
    for first_matrix_number, second_matrix_number in np.nditer([m1, m2]):
        print(first_matrix_number, ":", second_matrix_number)
