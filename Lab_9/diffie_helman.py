import random

from miller_rabin import MillerRabin


class DiffieHellman(MillerRabin):
    """
    This class represents an instance of the Diffie-Hellman key exchange protocol.
    """

    def __init__(self, p_bits: int = 128) -> None:
        """
        Initialize DiffieHellman object.

        :param p_bits: Number of bits for generating a prime number.
        """
        self.p = self._generate_prime(p_bits)
        self.g = self._generate_primitive_root(self.p)

    def _generate_primitive_root(self, p: int) -> int:
        """
        Generate a primitive root modulo p.

        :param p: The prime modulus.
        :return: A primitive root modulo p.
        """
        phi = p - 1
        while True:
            g = random.randint(2, phi - 1)
            if pow(g, phi, p) == 1:
                return g
