#!/usr/bin/python3
from typing import Dict, List

from constant import (
    exp_d,
    final_perm,
    initial_perm,
    key_comp,
    keyp,
    per,
    sbox,
    shift_table,
)


def hex2bin(s: str) -> str:
    """
    Convert a hexadecimal string to binary.

    :param s: Hexadecimal string to convert.
    :return: Binary representation of the input hexadecimal string.
    """
    mp: Dict[str, str] = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    bin_str = ""
    for i in range(len(s)):
        bin_str = bin_str + mp[s[i]]
    return bin_str


def bin2hex(s: str) -> str:
    """
    Convert a binary string to hexadecimal.

    :param s: Binary string to convert.
    :return: Hexadecimal representation of the input binary string.
    """
    mp: Dict[str, str] = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    hex_str = ""
    for i in range(0, len(s), 4):
        ch = s[i : i + 4]
        hex_str = hex_str + mp[ch]

    return hex_str


def bin2dec(binary: int) -> int:
    """
    Convert a binary number to decimal.

    :param binary: Binary number to convert.
    :return: Decimal representation of the input binary number.
    """
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def dec2bin(num: int) -> str:
    """
    Convert a decimal number to binary.

    :param num: Decimal number to convert.
    :return: Binary representation of the input decimal number.
    """
    res = bin(num).replace("0b", "")
    if len(res) % 4 != 0:
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for _ in range(0, counter):
            res = "0" + res
    return res


def permute(k: str, arr: List[int], n: int) -> str:
    """
    Perform permutation on a binary string.

    :param k: Binary string to permute.
    :param arr: Permutation array.
    :param n: Length of the permutation array.
    :return: Permuted binary string.
    """
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation


def shift_left(k: str, nth_shifts: int) -> str:
    """
    Perform left circular shift on a binary string.

    :param k: Binary string to shift.
    :param nth_shifts: Number of left circular shifts.
    :return: Shifted binary string.
    """
    s = ""
    for _ in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k


def xor(a: str, b: str) -> str:
    """
    Perform bitwise XOR on two binary strings.

    :param a: First binary string.
    :param b: Second binary string.
    :return: Result of the XOR operation as a binary string.
    """
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def encrypt(pt: str, rkb: List[str], rk: List[str]) -> str:
    """
    Encrypt a plaintext using the DES algorithm.

    :param pt: Plaintext in hexadecimal format.
    :param rkb: Round keys in binary format.
    :param rk: Round keys in hexadecimal format.
    :return: Cipher text in hexadecimal format.
    """
    pt = hex2bin(pt)

    # Initial Permutation
    pt = permute(pt, initial_perm, 64)
    print("After initial permutation", bin2hex(pt))

    # Splitting
    left = pt[0:32]
    right = pt[32:64]
    for i in range(0, 16):
        # Expansion D-box: Expanding the 32 bits data into 48 bits
        right_expanded = permute(right, exp_d, 48)

        # XOR RoundKey[i] and right_expanded
        xor_x = xor(right_expanded, rkb[i])

        # S-boxex: substituting the value from s-box table by calculating row and column
        sbox_str = ""
        for j in range(0, 8):
            row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin2dec(
                int(
                    xor_x[j * 6 + 1]
                    + xor_x[j * 6 + 2]
                    + xor_x[j * 6 + 3]
                    + xor_x[j * 6 + 4]
                )
            )
            val = sbox[j][row][col]
            sbox_str = sbox_str + dec2bin(val)

        # Straight D-box: After substituting rearranging the bits
        sbox_str = permute(sbox_str, per, 32)

        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result

        # Swapper
        if i != 15:
            left, right = right, left
        print("Round ", i + 1, " ", bin2hex(left), " ", bin2hex(right), " ", rk[i])

    # Combination
    combine = left + right

    # Final permutation: final rearranging of bits to get cipher text
    cipher_text = permute(combine, final_perm, 64)
    return cipher_text


def main() -> None:
    pt = "123456ABCD132536"
    key = "AABB09182736CCDD"

    key = hex2bin(key)
    # getting 56 bit key from 64 bit using the parity bits
    key = permute(key, keyp, 56)

    # Splitting
    left = key[0:28]  # rkb for RoundKeys in binary
    right = key[28:56]  # rk for RoundKeys in hexadecimal

    rkb: list = []
    rk: list = []
    for i in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        # Combination of left and right string
        combine_str = left + right

        # Compression of key from 56 to 48 bits
        round_key = permute(combine_str, key_comp, 48)

        rkb.append(round_key)
        rk.append(bin2hex(round_key))

    print("Encryption")
    cipher_text = bin2hex(encrypt(pt, rkb, rk))
    print("Cipher Text : ", cipher_text)

    print("Decryption")
    rkb_rev = rkb[::-1]
    rk_rev = rk[::-1]
    text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
    print("Plain Text : ", text)


if __name__ == "__main__":
    main()
