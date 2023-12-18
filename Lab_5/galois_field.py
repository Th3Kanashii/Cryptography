#!/usr/bin/python3
from typing import Literal


class GaloisField:
    """
    A class for operations in the Galois Field GF(2^8).
    """

    @staticmethod
    def mul02(byte: int) -> int:
        """
        Multiply a byte by 02 in the Galois Field GF(2^8) modulo m(x).

        :param byte: The input byte to be multiplied by 02.
        :return: The result of the multiplication by 02.
        """
        # Left shift by 1 bit
        result: int = byte << 1

        # Check the oldest bit is 1
        if result & 0x100:
            # 0x1b represents the polynomial m(x) in decimal.
            result ^= 0x1B

        return result & 0xFF

    @staticmethod
    def mul03(byte: int) -> int:
        """
        Multiply a byte by 03 in the Galois Field GF(2^8) modulo m(x).

        :param byte: The input byte to be multiplied by 03.
        :return: The result of the multiplication by 03.
        """
        # Multiplication by 02 (left shift by 1 bit) and addition of the original byte
        return GaloisField.mul02(byte=byte) ^ byte


def main() -> None:
    example_1: Literal[212] = 0xD4
    example_2: Literal[191] = 0xBF

    return print(
        f"{hex(example_1)} * 02 = {hex(GaloisField.mul02(example_1))}\n"
        f"{hex(example_2)} * 03 = {hex(GaloisField.mul03(example_2))}"
    )


if __name__ == "__main__":
    main()
