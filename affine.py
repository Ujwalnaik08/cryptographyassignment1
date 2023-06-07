# affine_cipher.py

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) == 1:
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
    return None

def affine_encrypt(text, key):
    a, b = key
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((a * (ord(char) - 65) + b) % 26 + 65)
            else:
                encrypted_text += chr((a * (ord(char) - 97) + b) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(ciphertext, key):
    a, b = key
    decrypted_text = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "Error: Invalid key. 'a' and 26 must be coprime."

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((a_inverse * (ord(char) - 65 - b)) % 26 + 65)
            else:
                decrypted_text += chr((a_inverse * (ord(char) - 97 - b)) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text


# Example usage:
plaintext = "Hello, World!"
key = (5, 7)  # 'a' = 5, 'b' = 7
encrypted_text = affine_encrypt(plaintext, key)
decrypted_text = affine_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
