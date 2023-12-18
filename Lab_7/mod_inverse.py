from typing import Optional, Tuple


class ModInverse:
    """
    A class for calculating modular inverses using the extended Euclidean algorithm.
    """

    @staticmethod
    def _gcdex(a: int, b: int) -> Tuple[int, int, int]:
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

    def _inverse_gcdex(self, a: int, n: int) -> Optional[int]:
        """
        Find the multiplicative inverse of a modulo n using the extended Euclidean algorithm.

        :param a: The integer for which the inverse is to be found.
        :param n: The modulus.
        :return: The multiplicative inverse of a modulo n, or None if it does not exist.
        """
        gcd, x, _ = self.gcdex(a=a, b=n)

        # Check for mutual simplicity
        if gcd != 1:
            # Inverse doesnt exist if gcd(a, n) is not 1
            return None

        # Ensure the result is positive and within the range [0, n)
        return (x % n + n) % n
