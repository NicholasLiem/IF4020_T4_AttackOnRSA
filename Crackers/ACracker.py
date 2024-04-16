from Crackers.Strategy import Strategy
from sympy import nextprime, prevprime
from Utils import *
import math

# GOALS: decrypt_rsa(encrypted_message, p, q, e):
    
class ACracker(Strategy):
    def execute(self, encrypted_message, n, e):
        e = 65537

        sqrt = int(math.isqrt(n))
        print("Approximated Value of P and Q\n", str(sqrt))
        p = sqrt


        while (True):
          p = nextprime(p)
          q = p
          # Check if happens to be the same
          if (q * p == n): break

          # Check forward
          for i in range (3):
            q = nextprime(q)
            if (q * p == n): break
          if (q * p == n): break
        
          q = p
          # Check backward
          for i in range (3):
            q = prevprime(q)
            if (q * p == n): break
          if (q * p == n): break
        
        print("This is P\n", str(p))
        print("This is Q\n", str(q))
        decrypted_message = Utils.decrypt_rsa(encrypted_message, p, q, e)
        print("Decrypted message:\n\n"+ decrypted_message)

        # raise Exception("TODO: Implement this :)")
