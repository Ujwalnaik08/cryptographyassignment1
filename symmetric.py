def diffie_hellman(g, p, x, y):
    public_key_A = (g ** x) % p
    public_key_B = (g ** y) % p

    shared_secret_A = (public_key_B ** x) % p
    shared_secret_B = (public_key_A ** y) % p

    assert shared_secret_A == shared_secret_B

    return shared_secret_A

g = 5  
p = 23  
x = 6  
y = 15  

symmetric_key = diffie_hellman(g, p, x, y)

print("Symmetric Key:", symmetric_key)
