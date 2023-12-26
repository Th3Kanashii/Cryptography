#!/usr/bin/python3
import hashlib
import random
from typing import Tuple


class DSA:
    """
    A class implementation of the DSA.
    """

    def __init__(self, q_length: int = 160) -> None:
        """
        Initialize a Digital Signature Algorithm (DSA) instance.

        :param q_length: The length (in bits) of the prime number q. Default is 160 bits.
        """
        self.q: int = q_length
        self.p: int = self.generate_prime_p
        self.g: int = self.generate_generator
        self.x: int = random.randint(1, self.q - 1)
        self.y: int = pow(self.g, self.x, self.p)

    @property
    def generate_prime_p(self) -> int:
        """
        Generate a prime number p using the specified length q.
        """
        p_candidate: int = 2 * self.q + 1
        while not self._is_prime(p_candidate):
            p_candidate += 2 * self.q
        return p_candidate

    @property
    def generate_generator(self) -> int:
        """
        Generate a generator g for the group Zp*.
        """
        g_candidate: int = 2
        while pow(g_candidate, self.q, self.p) != 1:
            g_candidate += 1
        return g_candidate

    def _is_prime(self, n: int, k: int = 5) -> bool:
        """
        Check primality using the Miller-Rabin test.
        :param n: Number to check for primality.
        :param k: Number of iterations for the Miller-Rabin test.
        """
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def mod_inverse(self, a: int, m: int) -> int:
        """
        Compute the modular multiplicative inverse of a modulo m.
        :param a: Base value.
        :param m: Modulus.
        :return: Modular multiplicative inverse of a modulo m.
        """
        g, x, _ = self.extended_gcd(a, m)
        if g != 1:
            raise ValueError("The modular inverse does not exist.")
        else:
            return x % m

    def extended_gcd(self, a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = self.extended_gcd(b % a, a)
            return g, y - (b // a) * x, x

    def sign(self, message: str) -> Tuple[int, int]:
        """
        Generate a digital signature for the given message.
        :param message: Message to sign.
        :return: Digital signature (r, s).
        """
        k: int = random.randint(1, self.q - 1)
        r: int = pow(self.g, k, self.p) % self.q
        h: int = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        s: int = (self.mod_inverse(k, self.q) * (h + self.x * r)) % self.q
        return r, s

    def verify(self, message: str, signature: Tuple[int, int]) -> bool:
        """
        Verify the digital signature for the given message.
        :param message: Original message.
        :param signature: Digital signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
        r, s = signature
        if not (0 < r < self.q) or not (0 < s < self.q):
            return False

        w: int = self.mod_inverse(s, self.q)
        h: int = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        u1: int = (h * w) % self.q
        u2: int = (r * w) % self.q
        v: int = (pow(self.g, u1, self.p) * pow(self.y, u2, self.p) % self.p) % self.q
        return v == r


def main() -> None:
    dsa_key_generator: DSA = DSA()

    message: str = "Hello, world!"

    signature: Tuple[int, int] = dsa_key_generator.sign(message)
    is_valid: bool = dsa_key_generator.verify(message, signature)

    return print(
        f"Message: {message}\n"
        f"Signature: {signature}\n"
        f"Signature is valid: {is_valid}"
    )


if __name__ == "__main__":
    main()
