from typing import List

from constant import RCON, S_BOX


def key_expansion(key: bytes) -> List[List[int]]:
    """
    Expand the given AES key into a key schedule for encryption.

    :param key: The AES key as bytes (16, 24, or 32 bytes).
    :return: The key schedule as a list of 4-byte words.
    """
    key_schedule: List[List[int]] = [
        list(key[i : i + 4]) for i in range(0, len(key), 4)
    ]

    while len(key_schedule) < 44:
        word = key_schedule[-1]
        if len(key_schedule) % 4 == 0:
            # Rotate word
            word = [word[1], word[2], word[3], word[0]]
            # SubBytes
            word = [S_BOX[b] for b in word]
            # XOR with RCON
            word[0] ^= RCON[len(key_schedule) // 4 - 1]
        key_schedule.append([a ^ b for a, b in zip(key_schedule[-4], word)])

    return key_schedule


def sub_bytes(state: List[List[int]]) -> List[List[int]]:
    """
    Apply the SubBytes operation to the AES state.

    :param state: The current state of the AES encryption.
    :return: The state after applying the SubBytes operation.
    """
    return [[S_BOX[b] for b in row] for row in state]


def shift_rows(state: List[List[int]]) -> List[List[int]]:
    """
    Apply the ShiftRows operation to the AES state.

    :param state: The current state of the AES encryption.
    :return: The state after applying the ShiftRows operation.
    """
    return [row[i:] + row[:i] for i, row in enumerate(state)]


def mix_columns(state: List[List[int]]) -> List[List[int]]:
    """
    Apply the MixColumns operation to the AES state.

    :param state: The current state of the AES encryption.
    :return: The state after applying the MixColumns operation.
    """

    def mix_column(column):
        result = []
        for i in range(4):
            result.append(
                (
                    2 * column[i]
                    ^ 3 * column[(i + 1) % 4]
                    ^ column[(i + 2) % 4]
                    ^ column[(i + 3) % 4]
                )
                % 256
            )
        return result

    return [mix_column(column) for column in zip(*state)]


def add_round_key(
    state: List[List[int]], round_key: List[List[int]]
) -> List[List[int]]:
    """
    Add the current round key to the AES state.

    :param state: The current state of the AES encryption.
    :param round_key: The round key to be added.
    :return: The state after adding the round key.
    """
    return [
        [a ^ b for a, b in zip(row, round_key_row)]
        for row, round_key_row in zip(state, round_key)
    ]


def aes_encrypt(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypt the given plaintext using AES with the specified key.

    :param plaintext: The plaintext to be encrypted as bytes.
    :param key: The AES key as bytes (16, 24, or 32 bytes).
    :return: The encrypted ciphertext as bytes.
    """
    key_schedule = key_expansion(key)
    state = [list(plaintext[i : i + 4]) for i in range(0, len(plaintext), 4)]

    state = add_round_key(state, key_schedule[:4])

    for round_num in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule[round_num * 4 : (round_num + 1) * 4])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[40:])

    ciphertext = [byte for row in state for byte in row]
    return bytes(ciphertext)


def aes_round(state: List[List[int]], round_key: List[List[int]]) -> List[List[int]]:
    """
    Perform one round of AES encryption.

    :param state: The current state of the AES encryption.
    :param round_key: The round key for the current round.
    :return: The state after one round of AES encryption.
    """
    state = sub_bytes(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, round_key)
    return state


def main():
    plaintext = bytes.fromhex("3243F6A8885A308D313198A2E0370734")
    key = bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C")

    key_schedule = key_expansion(key)
    state = [list(plaintext[i : i + 4]) for i in range(0, len(plaintext), 4)]

    print("Plaintext:", plaintext.hex())
    print("Initial state:", state)

    # Initial round
    state = add_round_key(state, key_schedule[:4])
    print("\nRound 0 - Initial Round:")
    print("State after AddRoundKey:", state)

    # 9 main rounds
    for round_num in range(1, 10):
        state = aes_round(state, key_schedule[round_num * 4 : (round_num + 1) * 4])
        print(f"\nRound {round_num}:")
        print("State after SubBytes:", sub_bytes(state))
        print("State after ShiftRows:", shift_rows(state))
        print("State after MixColumns:", mix_columns(state))
        print("State after AddRoundKey:", state)

    # Final round
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[40:])
    print("\nRound 10 - Final Round:")
    print("State after SubBytes:", state)
    print("State after ShiftRows:", shift_rows(state))
    print("State after AddRoundKey:", state)

    # Output the final encrypted result
    encrypted_result = [byte for row in state for byte in row]
    print("\nEncrypted Result:", bytes(encrypted_result).hex())


if __name__ == "__main__":
    main()
