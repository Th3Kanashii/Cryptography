import random


class MillerRabin:
    """
    This class implementing the Miller-Rabin primality test for checking and generating prime numbers.
    """

    @staticmethod
    def _is_prime(num: int, k: int = 5) -> bool:
        """
        Check if a given number is prime using the Miller-Rabin primality test.

        :param num: The number to be checked for primality.
        :param k: The number of iterations or witnesses for the test.
        :return: True if the number is likely prime, False if it is composite.
        """
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False

        s, d = 0, num - 1
        while d % 2 == 0:
            s += 1
            d //= 2

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

    def _generate_prime(self, bits: int) -> int:
        """
        Generate a random prime number with the specified number of bits.

        :param bits: Number of bits for generating the prime number.
        :return: A random prime number.
        """
        while True:
            num: int = random.getrandbits(bits)
            if self._is_prime(num):
                return num
