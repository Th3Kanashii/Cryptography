#!/usr/bin/python3
from typing import Optional

from euler_function import phi
from extended_euclidean_algorithm import gcdex


def inverse_element_2(a: int, n: int) -> Optional[int]:
    """
    Find the multiplicative inverse of a modulo n using the extended Euler theorem.

    :param a: The integer for which the inverse is to be found.
    :param n: The modulus.
    :return: The multiplicative inverse of a modulo n, or None if it does not exist.
    """
    phi_n = phi(m=n)
    gcd, x, y = gcdex(a=a, b=n)

    # Check for mutual simplicity
    if gcd != 1:
        # Inverse doesnt exist if gcd(a, n) is not 1
        return None

    # Calculate the inverse using Euler theorem
    return pow(a, phi_n - 1, n)


if __name__ == "__main__":
    _a, _n = 5, 18
    inverse = inverse_element_2(a=_a, n=_n)
    if inverse is not None:
        print(f"The multiplicative inverse of {_a} modulo {_n} is {inverse}")
    else:
        print(f"The multiplicative inverse of {_a} modulo {_n} does not exist.")
