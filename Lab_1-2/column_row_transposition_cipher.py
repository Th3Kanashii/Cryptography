#!/usr/bin/python3
class ColumnRowTranspositionCipher:
    def __init__(self, column_key: str, row_key: str) -> None:
        """
        Initializes a new ColumnRowTranspositionCipher.

        :param column_key: The key used for column transposition.
        :param row_key: The key used for row transposition.
        """
        self.column_key = column_key
        self.row_key = row_key

    def encrypt(self, message: str) -> str:
        """
        Encrypts the input message using a column and row transposition cipher.

        :param message: The text to be encrypted.
        :return: The encrypted text.
        """

        # Convert keys and message to lowercase for consistency and delete spaces
        column_key = self.column_key.replace(" ", "").lower()
        row_key = self.row_key.replace(" ", "").lower()
        message = message.replace(" ", "").lower()

        # Calculate the number of columns and rows in the transposition matrix
        num_columns = len(column_key)
        num_rows = -(
            -len(message) // num_columns
        )  # Calculate the number of rows, rounding up

        # Initialize the matrix with spaces
        matrix = [[" " for _ in range(num_columns)] for _ in range(num_rows)]

        # Fill the matrix with the characters from the text
        for i in range(len(message)):
            row = i // num_columns
            column = i % num_columns
            matrix[row][column] = message[i]

        # Sort the column key and row key for proper rearrangement
        sorted_column_key = "".join(sorted(column_key))
        sorted_row_key = "".join(sorted(row_key))

        # Rearrange the columns based on the sorted column key
        column_key_indices = [column_key.index(letter) for letter in sorted_column_key]
        matrix = [
            [matrix[row][idx] for idx in column_key_indices] for row in range(num_rows)
        ]

        # Rearrange the rows based on the sorted row key
        row_key_indices = [row_key.index(letter) for letter in sorted_row_key]
        matrix = [matrix[idx] for idx in row_key_indices]

        # Create the encrypted text by reading the matrix column by column
        result = "".join(
            matrix[row][column]
            for column in range(num_columns)
            for row in range(num_rows)
        )
        return result

    def decrypt(self, message: str) -> str:
        """
        Decrypts the input message using a column and row transposition cipher.

        :param message: The text to be decrypted.
        :return: The decrypted text
        """
        # Convert keys to lowercase and remove spaces
        column_key = self.column_key.replace(" ", "").lower()
        row_key = self.row_key.replace(" ", "").lower()

        # Calculate the number of columns and rows in the transposition matrix
        num_columns = len(column_key)
        num_rows = -(
            -len(message) // num_columns
        )  # Calculate the number of rows, rounding up

        # Rearrange the rows based on the sorted row key
        row_key_indices = [row_key.index(letter) for letter in sorted(row_key)]
        row_key_indices_inverse = [
            row_key_indices.index(i) for i in range(len(row_key_indices))
        ]

        # Rearrange the columns based on the sorted column key
        column_key_indices = [column_key.index(letter) for letter in sorted(column_key)]
        column_key_indices_inverse = [
            column_key_indices.index(i) for i in range(len(column_key_indices))
        ]

        # Initialize the matrix with spaces
        matrix = [[" " for _ in range(num_columns)] for _ in range(num_rows)]

        # Read the encrypted message into the matrix column by column
        message_index = 0
        for column in range(num_columns):
            for row in range(num_rows):
                matrix[row][column] = message[message_index]
                message_index += 1

        # Extract the characters from the matrix to get the decrypted message
        decrypted_message = "".join(
            matrix[row_key_indices_inverse[row]][column_key_indices_inverse[column]]
            for row in range(num_rows)
            for column in range(num_columns)
        )

        return decrypted_message


def main() -> None:
    column_key, row_key = "крипто", "шифр"
    message = "Програмне забезпечення"

    column_row_transposition_cipher = ColumnRowTranspositionCipher(
        column_key=column_key, row_key=row_key
    )

    encrypt = column_row_transposition_cipher.encrypt(message)
    decrypt = column_row_transposition_cipher.decrypt(encrypt)

    print(
        f"Initial message: {message}, keys: ({column_key}, {row_key})\n"
        f"Encrypted message: {encrypt}\n"
        f"Decrypted message: {decrypt}"
    )


if __name__ == "__main__":
    main()
