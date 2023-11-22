#!/usr/bin/python3
def mul02(byte: int) -> int:
    """
    Multiply a byte by 02 in the Galois Field GF(2^8) modulo m(x).

    :param byte: The input byte to be multiplied by 02.
    :return: The result of the multiplication by 02.
    """
    # Left shift by 1 bit
    result = byte << 1
    # If the most significant bit after the shift is negative, XOR with m(x)
    if result & 0x100:
        result ^= 0x1b  # 0x1b represents the polynomial m(x) in decimal
    return result

def mul03(byte: int) -> int:
    """
    Multiply a byte by 03 in the Galois Field GF(2^8) modulo m(x).

    :param byte: The input byte to be multiplied by 03.
    :return: The result of the multiplication by 03.
    """
    # Multiplication by 02 (left shift by 1 bit) and addition of the original byte
    result = mul02(byte) ^ byte
    return result


if __name__ == "__main__":
    example1 = 0xD4  # D4 * 02 = B3
    result1 = mul02(example1)
    print(hex(result1))

    example2 = 0xBF  # BF * 03 = DA
    result2 = mul03(example2)
    print(hex(result2))
