#!/usr/bin/python3
import math
from typing import List


class MD5Hasher:
    """
    This class provides methods for computing the MD5 hash of an input message.
    """

    def __init__(self) -> None:
        """
        Initializes an MD5Hasher object.
        """
        # Additional constants for MD5
        self.T: List[int] = [
            int(4294967296 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)
        ]

        # Initial values for MD5
        self.a0: int = 0x67452301
        self.b0: int = 0xEFCDAB89
        self.c0: int = 0x98BADCFE
        self.d0: int = 0x10325476

    def left_rotate(self, x: int, c: int) -> int:
        """
        Perform a left circular rotation on a 32-bit integer.

        :param x: The input value.
        :param c: The number of positions to rotate.
        :return: The rotated 32-bit integer.
        """
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    def hash(self, message: str) -> str:
        """
        Compute the MD5 hash of the input message.

        :param message: The input message as a string.
        :return: The MD5 hash as a string.
        """
        # Represent the message as a list of 32-bit words
        message = bytearray(message, "utf-8")
        orig_len: int = (8 * len(message)) & 0xFFFFFFFF
        message.append(0x80)
        while len(message) % 64 != 56:
            message.append(0)

        message += orig_len.to_bytes(8, "little")

        # Process message blocks
        for i in range(0, len(message), 64):
            chunk: List[int] = list(message[i : i + 64])
            a, b, c, d = self.a0, self.b0, self.c0, self.d0

            for j in range(64):
                if 0 <= j <= 15:
                    F = (b & c) | ((~b) & d)
                    g = j
                elif 16 <= j <= 31:
                    F = (d & b) | ((~d) & c)
                    g = (5 * j + 1) % 16
                elif 32 <= j <= 47:
                    F = b ^ c ^ d
                    g = (3 * j + 5) % 16
                elif 48 <= j <= 63:
                    F = c ^ (b | (~d))
                    g = (7 * j) % 16

                d_temp = d
                d = c
                c = b
                b = (
                    b
                    + self.left_rotate(
                        (
                            a
                            + F
                            + self.T[j]
                            + int.from_bytes(chunk[g * 4 : g * 4 + 4], "little")
                        ),
                        7,
                    )
                ) & 0xFFFFFFFF
                a = d_temp

            self.a0 = (self.a0 + a) & 0xFFFFFFFF
            self.b0 = (self.b0 + b) & 0xFFFFFFFF
            self.c0 = (self.c0 + c) & 0xFFFFFFFF
            self.d0 = (self.d0 + d) & 0xFFFFFFFF

        # Return the hash as a string
        return f"{self.a0:08x}{self.b0:08x}{self.c0:08x}{self.d0:08x}"


def main() -> None:
    message: str = "Hello, World!"
    md5hasher: MD5Hasher = MD5Hasher()
    hashed_message: str = md5hasher.hash(message)

    return print(f"Message: {message}\nMD5 Hash: {hashed_message}")


if __name__ == "__main__":
    main()
