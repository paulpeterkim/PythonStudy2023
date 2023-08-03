import numpy as np


def foo1(x: np.ndarray) -> np.ndarray:
    return 2 * x - 1


def foo2(x: np.ndarray) -> np.ndarray:
    return x ** 2


x = np.linspace(-2, 2, 10001)
y1 = foo1(x)
y2 = foo2(x)
difference_ori = list(y2 - y1)

difference = list()
for i, j in zip(y1, y2):
    difference.append(j - i)

print(difference == difference_ori)

