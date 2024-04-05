from Crypto.Util.number import inverse, long_to_bytes
import random

class Utils:
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    @staticmethod
    def is_an_integer(x):
        return isinstance(x, int) or (isinstance(x, float) and int(x) == x)
    
    @staticmethod
    def decrypt_rsa(encrypted_message, p, q, e):
        N = p * q

        phi_N = (p - 1) * (q - 1)

        d = inverse(e, phi_N)

        decrypted_message = pow(encrypted_message, d, N)
        decrypted_message = long_to_bytes(decrypted_message)
        decrypted_message = decrypted_message.decode('utf-8', errors='replace')
        return decrypted_message
    
    @staticmethod
    def find_prime_factor(n):
        if n % 2 == 0:
            return 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return i
            i += 2
        return None
    
    @staticmethod
    def pollards_rho(n):
        if n % 2 == 0:
            return 2
        
        x = random.randint(2, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1

        def f(x):
            return (x*x + c) % n

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = Utils.gcd(abs(x - y), n)

        if d == n:
            return None
        return d
