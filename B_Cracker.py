from Utils import Utils
from sympy import isprime
import math

if __name__ == "__main__":
    e = 65537
    encrypted_message = int(input("Encrypted message: "))
    n = int(input("Input n: "))
    p = math.isqrt(n)
    if isprime(p):
        print("The p value: ", p)
        decrypted_message = Utils.decrypt_rsa(encrypted_message, p, p, e)
        print("Decrypted message:", decrypted_message)
    else:
        print("Prime factor not found.")
