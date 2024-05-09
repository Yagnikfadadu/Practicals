# Initial Permutation (IP)
IP = [2, 6, 3, 1, 4, 8, 5, 7]

# Inverse Initial Permutation (IP^-1)
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

# Expansion Permutation (EP)
EP = [4, 1, 2, 3, 2, 3, 4, 1]

# Permuted Choice 10 (PC-10)
PC_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

# Permuted Choice 8 (PC-8)
PC_8 = [6, 3, 7, 4, 8, 5, 10, 9]

# Straight Permutation (P4)
P4 = [2, 4, 3, 1]

# S-Box tables
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


def permutation(input_text, permutation_table):
    return [input_text[i - 1] for i in permutation_table]


def left_shift(input_text):
    return input_text[1:] + [input_text[0]]


def generate_keys(key):
    key = permutation(key, PC_10)
    key_halves = [key[:5], key[5:]]
    keys = []
    for i in range(2):
        key_halves[0] = left_shift(key_halves[0])
        key_halves[1] = left_shift(key_halves[1])
        round_key = permutation(key_halves[0] + key_halves[1], PC_8)
        keys.append(round_key)
    return keys


def feistel_round(text_half, key):
    text_half = permutation(text_half, EP)
    for i in range(8):
        text_half[i] = text_half[i] ^ key[i]
    text_half_0 = text_half[:4]
    text_half_1 = text_half[4:]
    row = text_half_0[0] * 2 + text_half_0[3]
    col = text_half_0[1] * 2 + text_half_0[2]
    s0_output = S0[row][col]
    row = text_half_1[0] * 2 + text_half_1[3]
    col = text_half_1[1] * 2 + text_half_1[2]
    s1_output = S1[row][col]
    output = permutation([s0_output, s1_output], P4)
    return output


def sdes_encrypt(plaintext, key):
    keys = generate_keys(key)
    plaintext = permutation(plaintext, IP)
    left_half = plaintext[:4]
    right_half = plaintext[4:]
    for i in range(2):
        new_right_half = feistel_round(right_half, keys[i])
        new_right_half = [left_half[j] ^ new_right_half[j] for j in range(4)]
        left_half, right_half = right_half, new_right_half
    ciphertext = permutation(right_half + left_half, IP_inv)
    return ciphertext


def sdes_decrypt(ciphertext, key):
    keys = generate_keys(key)
    ciphertext = permutation(ciphertext, IP)
    left_half = ciphertext[:4]
    right_half = ciphertext[4:]
    for i in range(1, -1, -1):
        new_right_half = feistel_round(right_half, keys[i])
        new_right_half = [left_half[j] ^ new_right_half[j] for j in range(4)]
        left_half, right_half = right_half, new_right_half
    plaintext = permutation(right_half + left_half, IP_inv)
    return plaintext


# Example usage:
plaintext = [1, 0, 1, 0, 0, 0, 1, 0]  # Example plaintext
key = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]  # Example key
encrypted_text = sdes_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = sdes_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
