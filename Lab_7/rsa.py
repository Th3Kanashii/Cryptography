#!/usr/bin/python3
import math
import random

from Lab_7.miller_rabin import is_prime


class RSA:
    def __init__(self, bits: int = 512) -> None:
        """
        Initialize the RSA key generator.

        :param bits: The number of bits for the key.
        """
        self.bits: int = bits
        self.public_key: tuple[int, int] = None
        self.private_key: tuple[int, int] = None

    def generate_prime(self) -> int:
        """
        Generate a random prime number with the specified number of bits.

        :return: A randomly generated prime number.
        """
        while True:
            num: int = random.getrandbits(self.bits)
            if is_prime(num):
                return num

    def egcd(self, a: int, b: int) -> tuple[int, int, int]:
        """
        Extended euclidean algorithm.

        :param a: First integer.
        :param b: Second integer.
        :return: A tuple (g, x, y).
        """
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def modinv(self, a: int, m: int) -> int:
        """
        Calculate the modular multiplicative inverse of a modulo m.

        :param a: The base integer.
        :param m: The modulo.
        :return: The modular multiplicative inverse of a modulo m.
        """
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception("Modular inverse does not exist")
        else:
            return x % m

    def generate_keypair(self) -> None:
        """
        Generate a pair of public and private keys.
        """
        p: int = self.generate_prime()
        q: int = self.generate_prime()
        n: int = p * q
        phi: int = (p - 1) * (q - 1)

        e: int = random.randint(2, phi - 1)
        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)

        d: int = self.modinv(e, phi)

        self.public_key: tuple[int, int] = (n, e)
        self.private_key: tuple[int, int] = (n, d)

    def encrypt(self, message: str) -> list[int]:
        """
        Encrypt a string using the public key.

        :param message: The string to be encrypted.
        :return: A list of integers representing the encrypted message.
        """
        n, e = self.public_key
        return [pow(ord(char), e, n) for char in message]

    def decrypt(self, ciphertext: list[int]) -> str:
        """
        Decrypt a list of integers using the private key.

        :param ciphertext: The list of integers to be decrypted.
        :return: The decrypted string.
        """
        n, d = self.private_key
        return "".join([chr(pow(char, d, n)) for char in ciphertext])


def main() -> None:
    rsa = RSA()
    rsa.generate_keypair()

    print("Public Key:", rsa.public_key)
    print("Private Key:", rsa.private_key)

    original_message: str = "Hello, RSA!"
    print(f"\nOriginal message: {original_message}")

    encrypted_message: list[int] = rsa.encrypt(original_message)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message: str = rsa.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
