#!/usr/bin/python3
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
        self.g = self.generate_primitive_root(self.p)

    def generate_primitive_root(self, p: int) -> int:
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

    def key_exchange(self, private_key: int) -> int:
        """
        Perform the Diffie-Hellman key exchange to generate the public key.

        :param private_key: The private key for the key exchange.
        :return: The public key generated during the key exchange.
        """
        return pow(self.g, private_key, self.p)


def main() -> None:
    diffie_hellman: DiffieHellman = DiffieHellman()

    # Generates private keys
    alice_private_key: int = random.randint(2, diffie_hellman.p - 2)
    bob_private_key: int = random.randint(2, diffie_hellman.p - 2)

    # Generates public keys
    alice_public_key: int = diffie_hellman.key_exchange(private_key=alice_private_key)
    bob_public_key: int = diffie_hellman.key_exchange(private_key=bob_private_key)

    # Calculate shared key
    alice_shared_secret: int = pow(bob_public_key, alice_private_key, diffie_hellman.p)
    bob_shared_secret: int = pow(alice_public_key, bob_private_key, diffie_hellman.p)

    return print(
        f"Public key for Alice: {alice_public_key}\n"
        f"Public key for Bob: {bob_public_key}\n"
        f"Shared key for Alice: {alice_shared_secret}\n"
        f"Shared key for Bob: {bob_shared_secret}"
    )


if __name__ == "__main__":
    main()
