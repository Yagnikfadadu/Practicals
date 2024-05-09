import re


def prepare_text(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = re.sub(r'[^A-Za-z]', '', text)
    text = text.upper()
    # If there are adjacent identical letters, insert an 'X' between them
    text = re.sub(r'(.)\1', r'\1X\1', text)
    # If the length of the text is odd, append an 'X' to make it even
    if len(text) % 2 != 0:
        text += 'X'
    return text


def generate_key_table(key):
    key = key.upper().replace('J', 'I')  # Treat 'J' and 'I' as the same letter
    # Initialize the key table with the unique letters of the key
    key_table = []
    for char in key:
        if char not in key_table and char.isalpha():
            key_table.append(char)
    # Fill the key table with the remaining letters of the alphabet
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    return key_table


def find_position(key_table, char):
    # Find the position of a character in the key table
    row, col = 0, 0
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                row, col = i, j
                break
    return row, col


def playfair_encrypt(text, key):
    text = prepare_text(text)
    key_table = generate_key_table(key)
    encrypted_text = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(key_table, char1)
        row2, col2 = find_position(key_table, char2)
        if row1 == row2:  # Same row, shift right
            encrypted_text += key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column, shift down
            encrypted_text += key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
        else:  # Form a rectangle, swap columns
            encrypted_text += key_table[row1][col2] + key_table[row2][col1]
    return encrypted_text


def playfair_decrypt(text, key):
    key_table = generate_key_table(key)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(key_table, char1)
        row2, col2 = find_position(key_table, char2)
        if row1 == row2:  # Same row, shift left
            decrypted_text += key_table[row1][(col1 - 1) % 5] + key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column, shift up
            decrypted_text += key_table[(row1 - 1) % 5][col1] + key_table[(row2 - 1) % 5][col2]
        else:  # Form a rectangle, swap columns
            decrypted_text += key_table[row1][col2] + key_table[row2][col1]
    return decrypted_text


# Example usage:
plaintext = "HELLO WORLD"
key = "PLAYFAIREXAMPLE"
encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
