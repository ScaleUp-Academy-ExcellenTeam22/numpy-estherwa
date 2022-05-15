import numpy as np


def ex_numpy_sixteen():
    """
     A NumPy program to create a three-dimension array with a specific shape .
    """
    student_id = np.array([1, 2, 3, 4, 5, 6, 7])
    student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
    indices = np.lexsort((student_id, student_height))

    for index in indices:
        print(student_id[index], student_height[index])
