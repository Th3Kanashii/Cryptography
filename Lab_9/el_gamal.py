#!/usr/bin/python3
import random
from typing import Tuple


class ElGamal:
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
        public_key: int = pow(self.g, private_key, self.p)
        return public_key

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


class DiffieHellman:
    def __init__(self, p_bits: int = 128) -> None:
        """
        Initialize DiffieHellman object.

        :param p_bits: Number of bits for generating a prime number.
        """
        self.p = self.generate_prime(p_bits)
        self.g = self.generate_primitive_root(self.p)

    @staticmethod
    def is_prime(num: int, k: int = 5) -> bool:
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

    @staticmethod
    def generate_prime(bits: int) -> int:
        """
        Generate a random prime number with the specified number of bits.

        :param bits: Number of bits for generating the prime number.
        :return: A random prime number.
        """
        while True:
            num: int = random.getrandbits(bits)
            if DiffieHellman.is_prime(num):
                return num

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


def main():
    diffie_hellman = DiffieHellman()
    p = diffie_hellman.p
    g = diffie_hellman.g

    elgamal = ElGamal(p, g)

    # generate key pair el gamal
    private_key = random.randint(2, p - 2)
    public_key = elgamal.generate_keypair(private_key)

    message = 42

    # encrypt
    k = random.randint(2, p - 2)
    ciphertext = elgamal.encrypt(message, public_key, k)

    # decrypt
    decrypted_message = elgamal.decrypt(ciphertext, private_key)

    print("Original message:", message)
    print("Encrypted message:", ciphertext)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
