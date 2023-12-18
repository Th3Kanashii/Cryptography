#!/usr/bin/python3
from typing import Optional, Union

from gcdex import gcdex
from phi import phi


def inverse_phi(a: int, n: int) -> Optional[int]:
    """
    Find the multiplicative inverse of a modulo n using the extended Euler theorem.

    :param a: The integer for which the inverse is to be found.
    :param n: The modulus.
    :return: The multiplicative inverse of a modulo n, or None if it does not exist.
    """
    phi_n: int = phi(m=n)
    gcd, _, _ = gcdex(a=a, b=n)

    # Check for mutual simplicity
    if gcd != 1:
        # Inverse doesnt exist if gcd(a, n) is not 1
        return None

    # Calculate the inverse using Euler theorem
    return pow(a, phi_n - 1, n)


def main() -> None:
    a, n = 5, 18
    inverse: Union[int, None] = inverse_phi(a=a, n=n)

    if inverse:
        return print(f"The multiplicative inverse of {a} modulo {n} is {inverse}.")

    return print(f"The multiplicative inverse of {a} modulo {n} does not exist.")


if __name__ == "__main__":
    main()
