# Alice Code
# Imports
import sympy
from sympy import *
import random
import math


# Generate prime numbers for p and q
def generate_prime():
    while True:
        num = random.randint(10, 1000)
        if isprime(num):
            return num

# Generate Euler's Totient, which is the amount of coprimes until X.
def Eulers_Totient(p, q):
    Phi_n = (p - 1) * (q - 1)
    return Phi_n

# Generate e, which is a random number between 1 and euler's totient, which is coprime to euler's totient.
def generate_e(Eulers_Totient):
    while True:
        e = random.randint(2, Eulers_Totient)
        if math.gcd(e, Eulers_Totient) == 1:
            return e


# Generate d, which is the modular inverse of e mod (Eulers_Totient)
def generate_d(Eulers_Totient, e):
    d = sympy.mod_inverse(e, Eulers_Totient)
    return d


# Initialize all the variables and functions for ease of use later on.
p = generate_prime()
q = generate_prime()
n = p * q
t = Eulers_Totient(p, q)
e = generate_e(t)
d = generate_d(t, e)

# The public key is made of the pair (n, e) and the private key is the number d
print("Public key: ", (n, e))

# The private key is kept secret
print("Private key: ", d)

# Alice writes the public key in a file called "public_key.txt"
with open("public_key.txt", "w") as file:
    file.write(str(n) + "\n")
    file.write(str(e))

# Alice writes the private key in a file called "private_key.txt"
with open("private_key.txt", "w") as file:
    file.write(str(d) + "\n")
    file.write(str(n))
