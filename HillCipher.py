import numpy as np
from sympy import Matrix


def prepare_text(text, block_size):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(filter(str.isalpha, text.upper()))
    # If the length of the text is not divisible by the block size, pad it with 'X'
    while len(text) % block_size != 0:
        text += 'X'
    return text


def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]


def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])


def matrix_mod_inv(matrix, modulus):
    det = Matrix(matrix).det()
    adjugate = Matrix(matrix).adjugate()
    inverse_det = pow(int(det), -1, modulus)
    inverse_matrix = np.array(adjugate.applyfunc(lambda x: (x * inverse_det) % modulus))
    return inverse_matrix


def hill_encrypt(plaintext, key):
    block_size = len(key)
    plaintext = prepare_text(plaintext, block_size)
    key_matrix = np.array(key)
    ciphertext = ""
    for i in range(0, len(plaintext), block_size):
        block = np.array(text_to_numbers(plaintext[i:i + block_size]))
        encrypted_block = np.dot(block, key_matrix) % 26
        ciphertext += numbers_to_text(encrypted_block)
    return ciphertext


def hill_decrypt(ciphertext, key):
    block_size = len(key)
    key_matrix = np.array(key)
    decryption_key = matrix_mod_inv(key_matrix, 26)
    decrypted_text = ""
    for i in range(0, len(ciphertext), block_size):
        block = np.array(text_to_numbers(ciphertext[i:i + block_size]))
        decrypted_block = np.dot(block, decryption_key) % 26
        decrypted_text += numbers_to_text(decrypted_block)
    return decrypted_text


# Example usage:
plaintext = "HELLO"
key = [[3, 3], [2, 5]]
encrypted_text = hill_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = hill_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
