from Crypto.Util.number import inverse

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
        return decrypted_message
