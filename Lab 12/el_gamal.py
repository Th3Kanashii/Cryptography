#!/usr/bin/python3
from typing import Tuple


class EllipticCurve:
    def __init__(self, p: int, a: int, b: int) -> None:
        """
        Initialize an elliptic curve with parameters.

        :param p: Prime number defining the finite field.
        :param a: Coefficient 'a' in the elliptic curve equation.
        :param b: Coefficient 'b' in the elliptic curve equation.
        """
        self.p = p
        self.a = a
        self.b = b

    def extended_gcd(self, a: int, b: int) -> Tuple[int, int, int]:
        """
        Extended Euclidean Algorithm for finding the greatest common divisor and coefficients.

        :param a: First integer.
        :param b: Second integer.
        :return: Tuple (d, x, y) where d is gcd(a, b), and x, y are coefficients.
        """
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.extended_gcd(b, a % b)
            return d, y, x - y * (a // b)

    def mod_inverse(self, a: int) -> int:
        """
        Calculate the modular inverse of 'a' in the field defined by 'p'.

        :param a: Integer for which to find the inverse.
        :return: Modular inverse of 'a'.
        :raises ValueError: If the inverse does not exist.
        """
        d, x, _ = self.extended_gcd(a, self.p)
        if d != 1:
            raise ValueError("Inverse does not exist")
        else:
            return x % self.p

    def elliptic_addition(
        self, P: Tuple[float, float], Q: Tuple[float, float]
    ) -> Tuple[float, float]:
        """
        Perform elliptic curve point addition.

        :param P: First point as a tuple (x, y).
        :param Q: Second point as a tuple (x, y).
        :return: Resulting point of the addition.
        """
        if P == (float("inf"), float("inf")):
            return Q
        elif Q == (float("inf"), float("inf")):
            return P
        else:
            x_p, y_p = P
            x_q, y_q = Q

            if P != Q:
                m = (y_q - y_p) * self.mod_inverse(x_q - x_p) % self.p
            else:
                m = (3 * x_p**2 + self.a) * self.mod_inverse(2 * y_p) % self.p

            x_r = (m**2 - x_p - x_q) % self.p
            y_r = (m * (x_p - x_r) - y_p) % self.p

            return x_r, y_r

    def elliptic_multiply(self, P: Tuple[float, float], n: int) -> Tuple[float, float]:
        """
        Perform scalar multiplication of a point on the elliptic curve.

        :param P: Point as a tuple (x, y).
        :param n: Scalar multiplier.
        :return: Resulting point of the scalar multiplication.
        """
        Q = float("inf"), float("inf")
        for bit in bin(n)[2:]:
            Q = self.elliptic_addition(Q, Q)
            if bit == "1":
                Q = self.elliptic_addition(Q, P)
        return Q


class ElGamalEncryption:
    def __init__(self, curve: EllipticCurve, G: Tuple[float, float]) -> None:
        """
        Initialize ElGamal encryption with a specified elliptic curve and base point.

        :param curve: EllipticCurve object representing the curve.
        :param G: Base point as a tuple (x, y).
        """
        self.curve = curve
        self.G = G

    def generate_key_pair(self, private_key: int) -> Tuple[int, Tuple[float, float]]:
        """
        Generate a key pair given a private key.

        :param private_key: Private key for key pair generation.
        :return: Tuple (private_key, public_key) representing the key pair.
        """
        public_key = self.curve.elliptic_multiply(self.G, private_key)
        return private_key, public_key

    def encrypt(
        self, public_key: Tuple[float, float], plaintext: int
    ) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Encrypt a plaintext using ElGamal encryption.

        :param public_key: Public key as a tuple (x, y).
        :param plaintext: Integer representing the plaintext.
        :return: Tuple (C1, C2) representing the ciphertext.
        """
        k = 6  # random number (additional parameter)
        C1 = self.curve.elliptic_multiply(self.G, k)
        C2 = self.curve.elliptic_addition(
            (plaintext, 0), self.curve.elliptic_multiply(public_key, k)
        )
        return C1, C2

    def decrypt(
        self, private_key: int, C1: Tuple[float, float], C2: Tuple[float, float]
    ) -> int:
        """
        Decrypt a ciphertext using ElGamal decryption.

        :param private_key: Private key for decryption.
        :param C1: C1 component of the ciphertext.
        :param C2: C2 component of the ciphertext.
        :return: Integer representing the decrypted plaintext.
        """
        S = self.curve.elliptic_multiply(C1, private_key)
        S_neg = (S[0], -S[1] % self.curve.p)
        plaintext = self.curve.elliptic_addition(C2, S_neg)[0]
        return plaintext


def main() -> None:
    # Given parameters
    p = 23
    a = 1
    b = 1
    G = (17, 20)
    private_key_A = 4  # private key

    curve = EllipticCurve(p, a, b)
    elgamal = ElGamalEncryption(curve, G)

    # Generate key pair
    private_key_A, public_key_A = elgamal.generate_key_pair(private_key_A)

    # Test encryption and decryption
    plaintext = 10
    C1, C2 = elgamal.encrypt(public_key_A, plaintext)
    decrypted_text = elgamal.decrypt(private_key_A, C1, C2)

    print("Plaintext:", plaintext)
    print("Ciphertext (C1, C2):", C1, C2)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
