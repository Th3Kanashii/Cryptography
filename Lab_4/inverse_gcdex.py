#!/usr/bin/python3
from typing import Optional, Union

from gcdex import gcdex


def inverse_gcdex(a: int, n: int) -> Optional[int]:
    """
    Find the multiplicative inverse of a modulo n using the extended Euclidean algorithm.

    :param a: The integer for which the inverse is to be found.
    :param n: The modulus.
    :return: The multiplicative inverse of a modulo n, or None if it does not exist.
    """
    gcd, x, _ = gcdex(a=a, b=n)

    # Check for mutual simplicity
    if gcd != 1:
        # Inverse doesnt exist if gcd(a, n) is not 1
        return None

    # Ensure the result is positive and within the range [0, n)
    return (x % n + n) % n


def main() -> None:
    a, n = 5, 18
    inverse: Union[int, None] = inverse_gcdex(a=a, n=n)

    if inverse:
        return print(f"The multiplicative inverse of {a} mod {n} is {inverse}.")

    return print(f"The multiplicative inverse of {a} mod {n} does not exist.")


if __name__ == "__main__":
    main()
