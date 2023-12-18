#!/usr/bin/python3
from typing import List, Literal


class MatrixCipher:
    """
    A class for encrypting and decrypting messages using a matrix cipher.
    """

    @staticmethod
    def encrypt(message: str, column_key: str, row_key: str) -> str:
        """
        Encrypts the input message using a column and row transposition cipher.

        :param message: The text to be encrypted.
        :param column_key: The key used for column transposition.
        :param row_key: The key used for row transposition.
        :return: The encrypted text.
        """
        # Preprocess the message, column_key and row_key removing spaces and converting to lowercase
        message: str = message.replace(" ", "").lower()
        column_key: str = column_key.replace(" ", "").lower()
        row_key: str = row_key.replace(" ", "").lower()

        # Calculate the number of rows and colums, rounding up
        num_columns: int = len(column_key)
        num_rows: int = -(-len(message) // num_columns)

        # Initialize the matrix with spaces
        matrix: List[List[str]] = [
            [" " for _ in range(num_columns)] for _ in range(num_rows)
        ]

        # Fill the matrix with characters from the message
        for i, char in enumerate(message):
            matrix[i // num_columns][i % num_columns] = char

        # Sort the column key and rearrange the columns
        column_key_indices: List[int] = [
            column_key.index(letter) for letter in sorted(column_key)
        ]
        matrix: List[List[str]] = [
            [matrix[row][idx] for idx in column_key_indices] for row in range(num_rows)
        ]

        # Sort the row key and rearrange the rows
        row_key_indices: List[int] = [
            row_key.index(letter) for letter in sorted(row_key)
        ]
        matrix: List[List[str]] = [matrix[idx] for idx in row_key_indices]

        # Create the encrypted text by reading the matrix column by column
        result: str = "".join(
            matrix[row][column]
            for column in range(num_columns)
            for row in range(num_rows)
        )

        return result

    @staticmethod
    def decrypt(message: str, column_key: str, row_key: str) -> str:
        """
        Decrypts the input message using a column and row transposition cipher.

        :param message: The text to be decrypted.
        :param column_key: The key used for column transposition.
        :param row_key: The key used for row transposition.
        :return: The decrypted text.
        """
        # Get the indices for rearranging columns and rows
        column_key_indices: List[int] = [
            column_key.index(letter) for letter in sorted(column_key)
        ]
        row_key_indices: List[int] = [
            row_key.index(letter) for letter in sorted(row_key)
        ]

        num_columns: int = len(column_key)

        # Calculate the number of rows, rounding up
        num_rows: int = -(-len(message) // num_columns)

        # Initialize the matrix with spaces
        matrix: List[List[str]] = [
            [" " for _ in range(num_columns)] for _ in range(num_rows)
        ]

        # Fill the matrix with characters from the encrypted message
        message_index: Literal[0] = 0
        for column in range(num_columns):
            for row in range(num_rows):
                matrix[row][column] = message[message_index]
                message_index += 1

        # Extract characters from the matrix to get the decrypted message
        decrypted_message: str = "".join(
            matrix[row_key_indices.index(row)][column_key_indices.index(column)]
            for row in range(num_rows)
            for column in range(num_columns)
        )

        return decrypted_message


def main() -> None:
    column_key, row_key = "крипто", "шифр"
    message = "Програмне забезпечення"

    encrypt: str = MatrixCipher.encrypt(
        message=message, column_key=column_key, row_key=row_key
    )
    decrypt: str = MatrixCipher.decrypt(
        message=encrypt, column_key=column_key, row_key=row_key
    )

    return print(
        f"Initial message: {message}, keys: ({column_key}, {row_key})\n"
        f"Encrypted message: {encrypt}\n"
        f"Decrypted message: {decrypt}"
    )


if __name__ == "__main__":
    main()
