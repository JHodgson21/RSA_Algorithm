# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:42:11 2024

@author: Jakob
"""

from sympy import isprime, mod_inverse

def generate_keys(p, q):
    """Generate public and private keys."""
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi_n) != 1:
        e += 2

    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def gcd(a, b):
    """Calculate the GCD."""
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(plaintext, public_key):
    """Encrypt PT using the public key."""
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt cipherT using the private key."""
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

def main():
    p = int(input("Enter the first prime number: "))
    q = int(input("Enter the second prime number: "))

    if not (isprime(p) and isprime(q)):
        print("Both numbers must be prime.")
        return

    public_key, private_key = generate_keys(p, q)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    plaintext = int(input("Enter plaintext (as an integer): "))
    
    #Encryption
    ciphertext = encrypt(plaintext, public_key)
    print("Encrypted ciphertext:", ciphertext)

    #decryption
    decrypted_plaintext = decrypt(ciphertext, private_key)
    print("Decrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
