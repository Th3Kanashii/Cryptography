#!/usr/bin/python3
from typing import Tuple


def gcdex(a: int,
          b: int) -> Tuple[int, int, int]:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b using the extended Euclidean algorithm.

    :param a: The first integer.
    :param b: The second integer.
    :return: A tuple (d, x, y) where d is the GCD of a and b, and x, y satisfy the equation a*x + b*y = d.
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


if __name__ == "__main__":
    _a, _b = 612, 342
    d, x, y = gcdex(a=_a, b=_b)
    print(f"НСД({_a}, {_b}) = {d}\n"
          f"x = {x}, y = {y}\n"
          f"{_a}*{x} + {_b}*{y} = {d}")
