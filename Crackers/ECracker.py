from Crackers.Strategy import Strategy
from Crypto.Util.number import inverse
from Utils import Utils 

class ECracker(Strategy):
    def execute(self, encrypted_message, n, e):
        d = inverse(e, n-1)
        decrypted_message = pow(encrypted_message, d,n)
        print("Message: ",Utils.decode_message(decrypted_message))
