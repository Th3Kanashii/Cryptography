#!/usr/bin/python3
def phi(m: int) -> int:
    """
    Calculates the Euler function (function Phi) for a given number m.

    :param m: An integer for which the function Phi is calculated.
    :return: The value of the function Phi for the number m.
    """
    # The initial value is m
    result = m

    # For every prime number p that is a divisor of m
    p = 2
    while p * p <= m:
        if m % p == 0:
            # If p is a simple divisor of m, we take it into account in eulers formula
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1

    # Consider the case when other prime factors remain
    if m > 1:
        result -= result // m

    return result


def main() -> None:
    n = 12
    return print(f"Euler function for {n} = {phi(m=n)}")


if __name__ == "__main__":
    main()
