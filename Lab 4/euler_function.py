#!/usr/bin/python3
def phi(m: int) -> int:
    """
    Calculates the Euler function (function Phi) for a given number m.

    :param m: An integer for which the function Phi is calculated.
    :return: The value of the function Phi for the number m.
    """
    result = m

    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1

    if m > 1:
        result -= result // m

    return result


if __name__ == "__main__":
    n = 12
    print(f"Euler's function for {n} = {phi(m=n)}")
