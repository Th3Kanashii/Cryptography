#!/usr/bin/python3
import random

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

    def diffie_hellman_key_exchange(self, private_key: int) -> int:
        """
        Perform the Diffie-Hellman key exchange to generate the public key.

        :param private_key: The private key for the key exchange.
        :return: The public key generated during the key exchange.
        """
        public_key = pow(self.g, private_key, self.p)
        return public_key

def main() -> None:
    alice = DiffieHellman()
    bob = DiffieHellman()

    private_key_alice = random.randint(2, alice.p - 2)
    private_key_bob = random.randint(2, bob.p - 2)

    public_key_alice = alice.diffie_hellman_key_exchange(private_key_alice)
    public_key_bob = bob.diffie_hellman_key_exchange(private_key_bob)

    shared_key_alice = pow(public_key_bob, private_key_alice, alice.p)
    shared_key_bob = pow(public_key_alice, private_key_bob, bob.p)

    print("Parameter p:", alice.p)
    print("Primitive root g:", alice.g)
    print("Public key for Alice:", public_key_alice)
    print("Public key for Bob:", public_key_bob)
    print("Shared key for Alice:", shared_key_alice)
    print("Shared key for Bob:", shared_key_bob)

if __name__ == "__main__":
    main()
