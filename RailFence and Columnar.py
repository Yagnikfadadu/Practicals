def rail_fence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    encrypted_text = ''.join([''.join(row) for row in fence])
    return encrypted_text


def rail_fence_decrypt(ciphertext, rails):
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    for i in range(len(ciphertext)):
        fence[rail][i] = '#'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '#':
                fence[i][j] = ciphertext[index]
                index += 1
    rail = 0
    direction = 1  # 1 for down, -1 for up
    plaintext = ''
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][_]
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return plaintext


# Example usage:
plaintext = "HELLO WORLD"
rails = 3
encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Encrypted:", encrypted_text)
decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)


def columnar_transposition_encrypt(plaintext, key):
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)
    # Pad the plaintext with spaces if necessary
    plaintext += ' ' * (num_rows * num_columns - len(plaintext))
    # Create the grid
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            grid[row][col] = plaintext[index]
            index += 1
    # Arrange columns based on key order
    arranged_columns = [grid[:, i] for i in key]
    # Join the columns to form the ciphertext
    ciphertext = ''.join(''.join(column) for column in arranged_columns)
    return ciphertext


def columnar_transposition_decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)
    # Calculate the number of characters in the last column
    last_col_chars = len(ciphertext) % num_columns
    # Calculate the number of characters in other columns
    other_col_chars = len(ciphertext) // num_columns
    # Initialize the grid
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    # Calculate the number of rows in the last column
    last_col_rows = other_col_chars + 1 if last_col_chars > 0 else other_col_chars
    # Calculate the number of rows in other columns
    other_col_rows = other_col_chars
    # Calculate the index of the last non-full column
    last_non_full_col = last_col_chars if last_col_chars > 0 else num_columns
    # Calculate the length of ciphertext chunks for each column
    chunk_lengths = [last_col_rows if col < last_non_full_col else other_col_rows for col in range(num_columns)]
    index = 0
    # Fill the grid
    for col, length in zip(key, chunk_lengths):
        for row in range(length):
            grid[row][col] = ciphertext[index]
            index += 1
    # Extract plaintext from the grid
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext.strip()


# Example usage:
plaintext = "HELLO WORLD"
key = [2, 0, 1]
encrypted_text = columnar_transposition_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = columnar_transposition_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
