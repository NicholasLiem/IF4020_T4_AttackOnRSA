from Crackers.Strategy import Strategy
from Crypto.Util.number import inverse
import sympy
from Utils import *

# GOALS: decrypt_rsa(encrypted_message, p, q, e):


class CCracker(Strategy):
    def execute(self, encrypted_message, n, e):
        
        # D range 2**15 to 2**16 (small digit compared to E and N)
        # Assume D < 1/3 (N**(1/4))
        # Use Wiener Attack

        p, q = wiener_attack(e, n)
        print("This is P\n", str(p))
        print("This is Q\n", str(q))

        decrypted_message = Utils.decrypt_rsa(encrypted_message, int(p), int(q), e)
        print("Decrypted message:\n\n"+ decrypted_message)

        # raise Exception("TODO: Implement this :)")
    

def wiener_attack(e, n):
    """
    Wiener's attack to approximate N value (p, q). Otherwise returns None.
    """

    # Step 1: Compute continued fraction expansion of e/n
    rational = sympy.Rational(e, n)
    frac = sympy.continued_fraction(rational)
    expansion = list(sympy.continued_fraction_convergents(frac))
    
    count = 0
    print("Get", len(expansion), "amount of continued fracion convergents.")
    # Step 2: Iterate over convergents
    for conv in expansion:
        k, d = conv.numerator, conv.denominator

        print("Iteration", count, "|| k:", str(k)[:10], "|| d:", str(d)[:10])

        if k == 0:
            continue
        # Step 3: Check if d is valid
        phi = (e * d - 1) // k
        # Step 4: Compute private exponent
        x = sympy.symbols('x', integer=True)
        roots = sympy.solve(x ** 2 - (n - phi + 1) * x + n, x)

        if (len(roots) > 0): # Check if there is any roots of the equation
            n_predict = roots[0] * roots[1]
            if (n_predict == n):
                return roots 
            else :
                print("Prediction Failed")
        
        count +=1
        
    return None, None



    