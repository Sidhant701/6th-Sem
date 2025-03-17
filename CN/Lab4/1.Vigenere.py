def vigenereCipher(text, key, encrypt = True):
    result = []
    key = key.lower()
    keyLen = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % keyLen]) - ord('a')
            key_index += 1
            if not encrypt:
                shift = -shift
            if char.islower():
                newChar = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # for lowercase letter
            else:
                newChar = chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # for uppercase letter
            result.append(newChar)
        else:
            result.append(char)
    return "".join(result)

PT = "Hello World"
k = "KEY"
CT = vigenereCipher(PT, k) # For Encryption
print(CT) 
# Rijvs Uyvjn

PT = vigenereCipher(CT, k, encrypt=False) # For Decryption
print(PT)
# Hello World