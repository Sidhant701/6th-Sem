from Crypto.Cipher import DES
import binascii

def encryption(des, P, key):  
    while len(P) % 8 != 0:  
        P += " "  # Padding to make length a multiple of 8  

    P = P.encode()  # Converts string to binary  
    C = des.encrypt(P)  # Encrypts the binary data  
    C = binascii.hexlify(C).decode()  # Hexadecimal encoding and decoding
    return C

def decryption(des, C, key):  
    C = binascii.unhexlify(C)  # Convert hexadecimal representation back to binary
    P = des.decrypt(C)  # Decrypt the binary data
    P = P.decode().rstrip(" ")  # Decode and remove padding (trailing spaces)
    return P

key = input("Enter Key: ")
PT = input("Enter PlainText: ")
print(f"PlaintText: {PT}")
key = key.encode()
desCipher = DES.new(key, DES.MODE_ECB)
CT = encryption(desCipher, PT, key)
print(f"Encrypted Text: {CT}")

PT = decryption(desCipher, CT, key)
print(f"Decrypted Text: {PT}") 
# Enter Key: 12345678
# Enter PlainText: Sid
# PlaintText: Sid
# Encrypted Text: a7b501933b92bf9b
# Decrypted Text: Sid



















'''
from Crypto.Cipher import DES
import binascii

def encryption(des, P):  
    while len(P) % 8 != 0:  
        P += " "  # Padding to make length a multiple of 8  

    P = P.encode()  # Converts string to binary  
    C = des.encrypt(P)  # Encrypts the binary data  
    C = binascii.hexlify(C).decode()  # Hexadecimal encoding and decoding
    return C
def decryption(des, C):  
    C = binascii.unhexlify(C)  # Convert hexadecimal representation back to binary
    P = des.decrypt(C)  # Decrypt the binary data
    P = P.decode().rstrip(" ")  # Decode and remove padding (trailing spaces)
    return P

# Example usage
key = b"abcdefgh"  # 8-byte DES key
des = DES.new(key, DES.MODE_ECB)  # Using ECB mode for simplicity
plaintext = "Hello World"
ciphertext = encryption(des, plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = decryption(des, ciphertext)
print("Decrypted text:", decrypted_text)
'''