from Crackers.Strategy import Strategy
from Utils import Utils
import math

class DCracker(Strategy):
    def execute(self, encrypted_message, n, e):
        # decrypted_message = self.integer_cube_root(encrypted_message)
        decrypted_message = int(math.sqrt(encrypted_message))

        print("Decrypted message:\n\n"+ Utils.decode_message(decrypted_message))
    
    def integer_cube_root(n):
        # Custom cube root for big numbers
        if n < 0:
            raise ValueError("Negative number")
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            mid_cubed = mid**3
            if mid_cubed < n:
                low = mid + 1
            elif mid_cubed > n:
                high = mid - 1
            else:
                return mid
        return high
