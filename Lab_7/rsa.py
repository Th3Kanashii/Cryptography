#!/usr/bin/python3
import math
import random
from typing import List, Tuple, Union

from miller_rabin import is_prime
from mod_inverse import ModInverse


class RSA(ModInverse):
    """
    This class provides methods for generating RSA key pairs, encrypting and decrypting messages using RSA.
    """

    def __init__(self, bits: int = 512) -> None:
        """
        Initialize the RSA key generator.

        :param bits: The number of bits for the key.
        """
        self.bits = bits
        self.public_key, self.private_key = self.generate_keypair()

    def _generate_prime(self) -> int:
        """
        Generate a random prime number with the specified number of bits.

        :return: A randomly generated prime number.
        """
        while True:
            num = random.getrandbits(self.bits)
            if is_prime(num):
                return num

    def _generate_keypair(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Generate a pair of public and private keys.

        :return: A tuple containing public and private keys.
        """
        p = self.generate_prime()
        q = self.generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        # Choose public key e
        e = random.randint(1, phi - 1)
        while math.gcd(e, phi) != 1:
            e = random.randint(1, phi - 1)

        # Find private key d
        d: Union[int, None] = self.inverse_gcdex(e, phi)

        return ((n, e), (n, d))

    def encrypt(self, message: str) -> List[int]:
        """
        Encrypt a message using RSA.

        :param message: The message to be encrypted.
        :return: A list of encrypted integers representing the cipher text.
        """
        n, e = self.public_key
        cipher_text: List[int] = [pow(ord(char), e, n) for char in message]
        return cipher_text

    def decrypt(self, cipher_text: List[int]) -> str:
        """
        Decrypt a cipher text using RSA.

        :param cipher_text: A list of encrypted integers.
        :return: The decrypted plain text.
        """
        n, d = self.private_key
        plain_text: List[str] = [chr(pow(char, d, n)) for char in cipher_text]
        return "".join(plain_text)


def main() -> None:
    rsa: RSA = RSA()

    message = "Hello, RSA!"

    cipher_text: List[int] = rsa.encrypt(message)
    decrypted_message: str = rsa.decrypt(cipher_text)

    return print(
        f"Initial message: {message}\n"
        f"Encrypted message: {cipher_text}\n"
        f"Decrypted message: {decrypted_message}"
    )


if __name__ == "__main__":
    main()
