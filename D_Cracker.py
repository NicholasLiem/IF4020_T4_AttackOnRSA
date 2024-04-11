from Utils import Utils

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

if __name__ == "__main__":
    e = 3
    encrypted_message = int(input("Encrypted message: "))
    decrypted_message = integer_cube_root(encrypted_message)
    print("Message: ", Utils.decode_message(decrypted_message))
