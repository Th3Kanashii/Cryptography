#!/usr/bin/python3
from typing import Optional

from extended_euclidean_algorithm import gcdex


def inverse_element(a: int,
                    n: int) -> Optional[int]:
    """
    Find the multiplicative inverse of a modulo n using the extended Euclidean algorithm.

    :param a: The integer for which the inverse is to be found.
    :param n: The modulus.
    :return: The multiplicative inverse of a modulo n, or None if it does not exist.
    """
    gcd, x, y = gcdex(a=a, b=n)

    # Check for mutual simplicity
    if gcd != 1:
        # Inverse doesnt exist if gcd(a, n) is not 1
        return None

    # Ensure the result is positive and within the range [0, n)
    return (x % n + n) % n


if __name__ == "__main__":
    _a, _n = 5, 18
    inverse = inverse_element(a=_a, n=_n)
    if inverse is not None:
        print(f"The multiplicative inverse of {_a} mod {_n} is {inverse}")
    else:
        print(f"The multiplicative inverse of {_a} mod {_n} does not exist.")
