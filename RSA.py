import random
import math
from sympy import isprime, mod_inverse


def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num


def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext


# Example usage
public_key, private_key = generate_keypair(128)  # 128-bit key
plaintext = "Hello, RSA!"
encrypted_message = encrypt(public_key, plaintext)
decrypted_message = decrypt(private_key, encrypted_message)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
