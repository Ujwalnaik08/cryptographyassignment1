def extendec_eucledian(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extendec_eucledian(b, a % b)
        return gcd, y, x - (a // b) * y

def mod_inverse(a, m):
    gcd, x, g = extendec_eucledian(a, m)
    if gcd == 1:
        return x % m
    return None

a = int(input('Enter a number:'))
m = int(input('Enter the lenght of Z*:'))

inverse = mod_inverse(a, m)

print("The modular inverse of the {0} modulo {1} is: {2}".format(a, m, inverse))