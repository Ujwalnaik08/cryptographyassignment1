import hashlib
import os

def generate_salt(length=16):
    return os.urandom(length)

def compute_hash(password, salt):
    hash_object = hashlib.sha256()
    salted_password = password.encode('utf-8') + salt
    hash_object.update(salted_password)
    hash_value = hash_object.hexdigest()
    return hash_value

def verify_password(password, salt, hash_value):
    computed_hash = compute_hash(password, salt)
    if computed_hash == hash_value:
        return True
    return False

passwords = [
    "password1",
    "abc123",
    "qwerty",
    "letmein",
    "pass1234",
    "hello123",
    "password123",
    "changeme",
    "iloveyou",
    "admin123"
]

salts = []
for _ in range(len(passwords)):
    salts.append(generate_salt())

hashes = []
for i, password in enumerate(passwords):
    hash_value = compute_hash(password, salts[i])
    hashes.append(hash_value)

input_password = input("Enter your password: ")
input_index = int(input("Enter the index of your password (0-9): "))

if verify_password(input_password, salts[input_index], hashes[input_index]):
    print("Access granted: Password is correct.")
else:
    print("Access denied: Password is incorrect.")
