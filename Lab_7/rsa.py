#!/usr/bin/python3
import math
import random
from miller_rabin_simplicity_test import is_prime

class RSA:
    def __init__(self, bits: int = 512) -> None:
        self.bits: int = bits
        self.public_key: tuple[int, int] = None
        self.private_key: tuple[int, int] = None

    def generate_prime(self) -> int:
        while True:
            num: int = random.getrandbits(self.bits)
            if is_prime(num):
                return num

    def egcd(self, a: int, b: int) -> tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def modinv(self, a: int, m: int) -> int:
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def generate_keypair(self) -> None:
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

    def encrypt(self, message: str) -> int:
        n, e = self.public_key
        return [pow(ord(char), e, n) for char in message]

    def decrypt(self, ciphertext: list[int]) -> str:
        n, d = self.private_key
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])

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
