def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift
            if char.islower():  # For lowercase letters
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # For uppercase letters
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Preserve non-alphabetic characters
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decryption is just encryption with negative shift


# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted:", encrypted_text)
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)
