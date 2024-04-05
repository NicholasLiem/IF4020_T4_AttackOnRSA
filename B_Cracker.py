from Utils import Utils

if __name__ == "__main__":
    e = 65537
    encrypted_message = int(input("Encrypted message: "))
    n = int(input("Input n: "))
    p = Utils.find_prime_sqrt(n)
    if p is not None:
        decrypted_message = Utils.decrypt_rsa(encrypted_message, p, p, e)
        decrypted_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')
        print("Decrypted message:", decrypted_bytes.decode('utf-8'))
    else:
        print("Prime factor not found.")
