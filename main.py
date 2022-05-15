import numpy as np

from ex_1 import ex_numpy
from ex_2 import ex_numpy_second
from ex_3 import ex_numpy_third
from ex_4 import ex_numpy_forth
from ex_5 import ex_numpy_fifth
from ex_6 import ex_numpy_six
from ex_7 import ex_numpy_seven
from ex_8 import ex_numpy_eight

if __name__ == '__main__':
    # ex1
    number = np.arange(10, 20)
    ex_numpy(number)

    # ex2
    ex_numpy_second()

    # ex3
    ex_numpy_third()

    # ex4
    x = np.ones(10, 10)
    print(ex_numpy_forth(x))

    # ex5
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 1, 0])
    ex_numpy_fifth(m, v)

    # ex6

    x = np.arange(0, 7 * np.pi, 0.01)
    y = np.sin(x)

    ex_numpy_six(x, y)

    # ex7

    ex_numpy_seven()

    # ex8

    nums = np.array([[2.54, 6.38, 7.56],
                     [3.54, 9.32, 6.99],
                     [0.54, 7.39, 10.39]])

    ex_numpy_eight(nums, 9.14, 20.45)
