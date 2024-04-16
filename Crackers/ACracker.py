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
        
        p = prevprime(p)

        count_prev = 0
        while True:
          count_next = 0
          q = p
          while (q * p) < n:
            print("PREV:", count_prev, "|| NEXT:", count_next)
            if (q * p == n) : break
            q = nextprime(q)
            count_next +=1 
          
          if (q * p == n) : break
          p = prevprime(p)
          count_prev +=1

        
        print("This is P\n", str(p))
        print("This is Q\n", str(q))
        decrypted_message = Utils.decrypt_rsa(encrypted_message, p, q, e)
        print("Decrypted message:\n\n"+ decrypted_message)

        # raise Exception("TODO: Implement this :)")
