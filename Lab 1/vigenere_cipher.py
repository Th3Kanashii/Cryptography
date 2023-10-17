def vigenere_cipher(message: str,
                    key: str,
                    decrypt: bool = False) -> str:
    """
    Encrypts or decrypts the message using the Vigenere cipher with the given key.

    :param message: The text to be encrypted or decrypted.
    :param key: The encryption key.
    :param decrypt: If True, the function will perform decryption. If False (default), it will encrypt.
    :return: The encrypted or decrypted message.
    """
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

    # Remove spaces and convert the message and key to lowercase
    message = message.replace(" ", "").lower()
    key = key.replace(" ", "").lower()

    result = []
    key_index = 0

    for char in message:
        if char in alphabet:
            # Determine the shift based on the key
            shift = alphabet.index(key[key_index])
            if decrypt:
                # For decryption, we shift in the opposite direction
                new_index = (alphabet.index(char) - shift) % len(alphabet)
            else:
                new_index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_char = alphabet[new_index]
            result.append(encrypted_char)

            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    _message, _key = "Наступаємо на світанку", "Віженер"
    _encrypt = vigenere_cipher(message=_message, key=_key)
    _decrypt = vigenere_cipher(message=_encrypt, key=_key, decrypt=True)
    print(f"Initial message: {_message}, key: {_key}\n"
          f"Encrypted message: {_encrypt}\n"
          f"Decrypted message: {_decrypt}")
