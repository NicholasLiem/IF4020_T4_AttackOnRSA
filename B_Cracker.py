from math import isqrt
from Crypto.Util.number import isPrime

def find_p(n):
    p_candidate = isqrt(n)

    while p_candidate > 1:
        if n % p_candidate == 0 and isPrime(p_candidate):
            return p_candidate
        p_candidate -= 1

    return None

if __name__ == "__main__":
    e = 65537
    n = 3721
    p = find_p(n)
    print("Found p:", p)

