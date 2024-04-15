from Crackers.Strategy import Strategy
from Crypto.Util.number import inverse
import sympy

# GOALS: decrypt_rsa(encrypted_message, p, q, e):


def wiener_attack(e, n):
    """
    Wiener's attack to recover the private exponent d.
    Returns the private exponent d if successful, otherwise returns None.
    """
    # Step 1: Compute continued fraction expansion of e/n
    rational = sympy.Rational(e, n)
    frac = sympy.continued_fraction(rational)
    expansion = list(sympy.continued_fraction_convergents(frac))
    
    # Step 2: Iterate over convergents
    for conv in expansion:
        k, d = conv.denominator, conv.numerator
        if k == 0:
            continue
        # Step 3: Check if d is valid
        phi = (e * d - 1) // k
        # Step 4: Compute private exponent
        x = sympy.symbols('x', integer=True)
        roots = sympy.solve(x ** 2 - (n - phi + 1) * x + n, x)
        for root in roots:
            if root.is_integer and root > 0:
                d_found = int(root)
                if e * d_found % phi == 1:
                    return d_found
    return None

class CCracker(Strategy):
    def execute(self, encrypted_message, n, e):
        
        # D range 2**15 to 2**16 (small digit compared to E and N)
        # Assume D < 1/3 (N**(1/4))
        # Use Wiener Attack

        d = wiener_attack(e, n)
        print(d)


        raise Exception("TODO: Implement this :)")
    
    