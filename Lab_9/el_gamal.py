#!/usr/bin/python3
import random
from typing import Tuple

from diffie_helman import DiffieHellman


class ElGamal(DiffieHellman):
    def __init__(self, p: int, g: int) -> None:
        """
        Initialize ElGamal object.

        :param p: The prime modulus.
        :param g: The primitive root modulo p.
        """
        self.p = p
        self.g = g

    def generate_keypair(self, private_key: int) -> int:
        """
        Generate ElGamal key pair.

        :param private_key: The private key for the key pair.
        :return: The public key generated during the key pair generation.
        """
        return pow(self.g, private_key, self.p)

    def encrypt(self, message: int, public_key: int, k: int) -> Tuple[int, int]:
        """
        Encrypt a message using ElGamal.

        :param message: The message to be encrypted.
        :param public_key: The public key for encryption.
        :param k: A random value for encryption.
        :return: A tuple (alpha, beta) representing the ciphertext.
        """
        alpha: int = pow(self.g, k, self.p)
        beta: int = (pow(public_key, k, self.p) * message) % self.p
        return alpha, beta

    def decrypt(self, ciphertext: Tuple[int, int], private_key: int) -> int:
        """
        Decrypt ElGamal ciphertext.

        :param ciphertext: A tuple (alpha, beta) representing the ciphertext.
        :param private_key: The private key for decryption.
        :return: The decrypted message.
        """
        alpha, beta = ciphertext
        s: int = pow(alpha, private_key, self.p)
        plaintext: int = (beta * pow(s, -1, self.p)) % self.p
        return plaintext


def main() -> None:
    diffie_hellman: DiffieHellman = DiffieHellman()

    p: int = diffie_hellman.p
    g: int = diffie_hellman.g

    elgamal: ElGamal = ElGamal(p=p, g=g)

    # Generate key pair ElGamal
    private_key = random.randint(2, p - 2)
    public_key = elgamal.generate_keypair(private_key)

    k: int = random.randint(2, p - 2)
    message = 42
    ciphertext: Tuple[int, int] = elgamal.encrypt(message, public_key, k)
    decrypted_message: int = elgamal.decrypt(ciphertext, private_key)

    return print(
        f"Original message: {message}\n"
        f"Encrypted message: {ciphertext}\n"
        f"Decrypted message: {decrypted_message}"
    )


if __name__ == "__main__":
    main()
