#!/usr/bin/python3
from typing import Final, Literal


class VigenereCipher:
    """
    A class for encrypting and decrypting messages using a Vigenere cipher.
    """

    def __init__(self) -> None:
        """
        Initializes the VigenereCipher object and sets the alphabet.
        """
        self.alphabet: Final[str] = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

    def _shift_char(self, char: str, shift: int) -> str:
        """
        Shifts a character by a certain number of positions in the defined alphabet.

        :param char: The character to shift.
        :param shift: The number of positions to shift (can be negative).
        :return: The shifted characted.
        """
        if char in self.alphabet:
            current_index: int = self.alphabet.index(char)
            new_index: int = (current_index + shift) % len(self.alphabet)
            return self.alphabet[new_index]
        else:
            return char

    def _apply_cipher(self, message: str, key: str, decrypt: bool) -> str:
        """
        Applies the Vigenere cipher to the given message using the provided key.

        :param message: The message to be encrypted or decrypted.
        :param key: The key to be used for encryption or decryption.
        :param decrypt: True for decryption, False for encryption.
        :return: The result of the encryption or decryption.
        """
        message: str = message.replace(" ", "").lower()
        key: str = key.replace(" ", "").lower()

        result: list = []
        key_index: Literal[0] = 0

        for char in message:
            shift: int = self.alphabet.index(key[key_index])
            shifted_char: str = self._shift_char(char, -shift if decrypt else shift)
            result.append(shifted_char)

            key_index = (key_index + 1) % len(key)

        return "".join(result)

    def encrypt(self, message: str, key: str) -> str:
        """
        Encrypts the given message using the Vigenere cipher.

        :param message: The message to be encrypted.
        :param key: The key to be used for encryption.
        :return: The encrypted message.
        """
        return self._apply_cipher(message=message, key=key, decrypt=False)

    def decrypt(self, message: str, key: str) -> str:
        """
        Decrypts the given message using the Vigenere cipher.

        :param message: The message to be decrypted.
        :param key: The key to be used for decryption.
        :return: The decrypted message.
        """
        return self._apply_cipher(message=message, key=key, decrypt=True)


def main() -> None:
    message, key = "Наступаємо на світанку", "Віженер"
    vigenere_cipher: VigenereCipher = VigenereCipher()

    encrypted_message: str = vigenere_cipher.encrypt(message=message, key=key)
    decrypted_message: str = vigenere_cipher.decrypt(message=encrypted_message, key=key)

    return print(
        f"Initial message: {message}, key: {key}\n"
        f"Encrypted message: {encrypted_message}\n"
        f"Decrypted message: {decrypted_message}"
    )


if __name__ == "__main__":
    main()
