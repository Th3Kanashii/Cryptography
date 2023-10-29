def encrypt_message(message: str,
                    column_key: str,
                    row_key: str) -> str:
    """
    Encrypts the input text using a column and row transposition cipher.

    :param message: The text to be encrypted.
    :param column_key: The column key for transposition.
    :param row_key: The row key for transposition.
    :return: The encrypted text.
    """

    # Convert keys and message to lowercase for consistency and delete spaces
    column_key = column_key.replace(" ", "").lower()
    row_key = row_key.replace(" ", "").lower()
    message = message.replace(" ", "").lower()

    # Calculate the number of columns and rows in the transposition matrix
    num_columns = len(column_key)
    num_rows = -(-len(message) // num_columns)  # Calculate the number of rows, rounding up

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
    matrix = [[matrix[row][idx] for idx in column_key_indices] for row in range(num_rows)]

    # Rearrange the rows based on the sorted row key
    row_key_indices = [row_key.index(letter) for letter in sorted_row_key]
    matrix = [matrix[idx] for idx in row_key_indices]

    # Create the encrypted text by reading the matrix column by column
    result = "".join(matrix[row][column] for column in range(num_columns) for row in range(num_rows))
    return result


if __name__ == "__main__":
    _message = "Програмне забезпечення"
    _column_key, _row_key = "крипто", "шифр"
    encrypted_message = encrypt_message(message=_message,
                                        column_key=_column_key,
                                        row_key=_row_key)
    print(f"Initial message: {_message}, keys: {_column_key, _row_key}\n"
          f"Encrypted message: {encrypted_message}\n")
