#!/usr/bin/python3
import random


def is_prime(num: int, k: int = 5) -> bool:
    """
    Check if a given number is prime using the miller rabin primality test.

    :param num: The number to be checked for primality.
    :param k: The number of iterations or witnesses for the test.
    :return: True if the number is likely prime, False if it is composite.
    """
    # Base cases
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    # Express num - 1 as 2^s * d, where d is odd
    s, d = 0, num - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True


def main() -> None:
    if is_prime(num=512):
        return print("Num is prime")

    return print("Num is composite")


if __name__ == "__main__":
    main()
