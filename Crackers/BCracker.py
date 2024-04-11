from Crackers.Strategy import Strategy
from Utils import Utils
from sympy import isprime
import math

class BCracker(Strategy):
    def execute(self, encrypted_message, n, e):
        e = 65537
        p = math.isqrt(n)
        if isprime(p):
            print("The p value: ", p)
            decrypted_message = Utils.decrypt_rsa(encrypted_message, p, p, e)
            print("Decrypted message:", decrypted_message)
        else:
            print("Prime factor not found.")
