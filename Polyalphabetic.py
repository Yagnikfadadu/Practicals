def extend_key(plaintext, key):
    # Extend the key to the length of the plaintext
    extended_key = key
    while len(extended_key) < len(plaintext):
        extended_key += key
    return extended_key[:len(plaintext)]


def vigenere_encrypt(plaintext, key):
    key = extend_key(plaintext, key.upper())
    encrypted_text = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if plaintext[i].islower():
                encrypted_text += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
            elif plaintext[i].isupper():
                encrypted_text += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += plaintext[i]
    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    key = extend_key(ciphertext, key.upper())
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if ciphertext[i].islower():
                decrypted_text += chr((ord(ciphertext[i]) - ord('a') - shift + 26) % 26 + ord('a'))
            elif ciphertext[i].isupper():
                decrypted_text += chr((ord(ciphertext[i]) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text


# Example usage:
plaintext = "HELLO WORLD"
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
