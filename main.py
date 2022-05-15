import numpy as np

from ex_1 import ex_numpy
from ex_10 import ex_numpy_ten
from ex_11 import ex_numpy_eleven
from ex_12 import ex_numpy_twelve
from ex_13 import ex_numpy_thirteen
from ex_14 import ex_numpy_fourteen
from ex_15 import ex_numpy_fifteen
from ex_16 import ex_numpy_sixteen
from ex_17 import ex_numpy_seventeen
from ex_18 import ex_numpy_eightteen
from ex_2 import ex_numpy_second
from ex_3 import ex_numpy_third
from ex_4 import ex_numpy_forth
from ex_5 import ex_numpy_fifth
from ex_6 import ex_numpy_six
from ex_7 import ex_numpy_seven
from ex_8 import ex_numpy_eight
from ex_9 import ex_numpy_nine

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

    # ex 9

    nums1 = np.array([[2, 5, 2],
                      [1, 5, 5]])
    nums2 = np.array([[5, 3, 4],
                      [3, 2, 5]])

    ex_numpy_nine(nums1, nums2)

    # ex 10

    ex_numpy_ten(np.random.randint(100, size=16).reshape(-1, 4))

    # ex 11

    ex_numpy_eleven()

    # ex 12

    x = np.zeros((3, 1, 4))
    print(ex_numpy_twelve(x))

    # ex 13

    a = np.array([[10], [20], [30]])
    b = np.array([[40], [50], [60]])

    print(ex_numpy_thirteen(a, b))

    # ex 14
    x = np.array([0, 1, 2, 3])
    y = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    ex_numpy_fourteen(x, y)

    # ex 15

    ex_numpy_fifteen()

    # ex 16

    ex_numpy_sixteen()

    # ex 17

    m = np.random.randint(100, 16).reshape(4, 4)

    ex_numpy_seventeen(m)

    # ex 18

    ex_numpy_eightteen()
