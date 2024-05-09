import random


def generate_key():
    # Generate a random permutation of the alphabet
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)
    return ''.join(alphabet)


def monoalphabetic_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            if char.islower():  # For lowercase letters
                encrypted_text += key[ord(char) - ord('a')]
            elif char.isupper():  # For uppercase letters
                encrypted_text += key[ord(char) - ord('A')].upper()
        else:
            encrypted_text += char  # Preserve non-alphabetic characters
    return encrypted_text


def monoalphabetic_decrypt(text, key):
    # To decrypt, we need the inverse of the key
    inverse_key = ''.join(sorted(key, key=lambda x: key.index(x)))
    return monoalphabetic_encrypt(text, inverse_key)


# Example usage:
plaintext = "Hello, World!"
key = generate_key()
encrypted_text = monoalphabetic_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = monoalphabetic_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
