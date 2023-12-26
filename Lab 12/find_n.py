#!/usr/bin/python3
from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b using the extended Euclidean algorithm.

    :param a: Integer
    :param b: Integer
    :return: Tuple (gcd, x, y)
    """
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)


def inverse_modulo(a: int, m: int) -> int:
    """
    Find the modular multiplicative inverse of 'a' modulo 'm' using the extended gcd.

    :param a: Integer
    :param m: Modulus
    :return: Integer (Inverse of a modulo m)
    """
    _, inv, _ = extended_gcd(a, m)
    return inv % m


def elliptic_curve_addition(
    P: Tuple[int, int], Q: Tuple[int, int], a: int, p: int
) -> Tuple[int, int]:
    """
    Perform elliptic curve point addition operation.

    :param P: Tuple representing the coordinates of point P (x, y)
    :param Q: Tuple representing the coordinates of point Q (x, y)
    :param a: Coefficient in the elliptic curve equation
    :param p: Prime modulus
    :return: Tuple representing the result of the addition operation (x, y)
    """
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P

    x_p, y_p = P
    x_q, y_q = Q

    if P != Q:
        m = (y_q - y_p) * inverse_modulo(x_q - x_p, p) % p
    else:
        m = (3 * x_p**2 + a) * inverse_modulo(2 * y_p, p) % p

    x_r = (m**2 - x_p - x_q) % p
    y_r = (m * (x_p - x_r) - y_p) % p

    return x_r, y_r


def elliptic_curve_multiplication(
    G: Tuple[int, int], n: int, a: int, p: int
) -> Tuple[int, int]:
    """
    Perform elliptic curve point multiplication using the double and add algorithm.

    :param G: Tuple representing the coordinates of the base point G (x, y)
    :param n: Integer, the scalar multiplier
    :param a: Coefficient in the elliptic curve equation
    :param p: Prime modulus
    :return: Tuple representing the result of the multiplication (x, y)
    """
    result = (0, 0)
    current = G

    while n > 0:
        if n % 2 == 1:
            result = elliptic_curve_addition(result, current, a, p)
        current = elliptic_curve_addition(current, current, a, p)
        n //= 2

    return result


def find_order(G: Tuple[int, int], a: int, p: int) -> int:
    """
    Find the order of the base point G on the elliptic curve.

    :param G: Tuple representing the coordinates of the base point G (x, y)
    :param a: Coefficient in the elliptic curve equation
    :param p: Prime modulus
    :return: Integer representing the order of the point G
    """
    order = 1
    current = G

    while current != (0, 0):
        order += 1
        current = elliptic_curve_multiplication(G, order, a, p)

    return order


def main() -> None:
    # Given parameters of the elliptic curve
    a = 1
    p = 23
    G = (17, 25)

    # Find the order of the base point G
    order = find_order(G, a, p)

    return print(f"The order of the base point G is: {order}")


if __name__ == "__main__":
    main()
