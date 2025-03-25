# 24/03/25

'''ENCRYPTION'''
import string
def create_matrix(key):
    key=key.upper().replace('J','I')
    seen=set()
    matrix=[]
        
    for char in key:
        if char not in seen and char in string.ascii_uppercase:
            seen.add(char)
            matrix.append(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
            
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None 

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    prepared = ""
    
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i] == text[i + 1]:  
            prepared += text[i] + "X"
            i += 1
        else:
            prepared += text[i]
            if i + 1 < len(text):
                prepared += text[i + 1]
            i += 2
    
    if len(prepared) % 2 != 0:
        prepared += "X"
    print("Prepared text : ",prepared,end='\n\n')
    return prepared
def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    print("MATRIX: ")
    for i in matrix:
        for j in i :
            print(j,end="      ")
        print()
    print()

    text = prepare_text(text)
    ciphertext = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i + 1])

        if r1 == r2:  
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else: 
            ciphertext += matrix[r1][c2] + matrix[r2][c1]

    return ciphertext

key = "MONARCH"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted:", ciphertext)
# M      O      N      A      R
# C      H      B      D      E
# F      G      I      K      L
# P      Q      S      T      U
# V      W      X      Y      Z

# Prepared text :  HELXLOWORLDX

# Plaintext: HELLO WORLD
# Encrypted: BCIZGROHEUBY



print("\n")



'''DECRYPTION'''
def playfair_decrypt(text, key):
    matrix = create_matrix(key)
    print("MATRIX: ")
    for i in matrix:
        for j in i :
            print(j,end="      ")
        print()
    print()
    plaintext = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i + 1])

        if r1 == r2:  
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:  
            plaintext += matrix[r1][c2] + matrix[r2][c1]

    return plaintext

key = "MONARCH"
ciphertext = "BCIZGROHEUBY"
decrypted_text = playfair_decrypt(ciphertext, key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text)
# MATRIX:
# M      O      N      A      R
# C      H      B      D      E
# F      G      I      K      L
# P      Q      S      T      U
# V      W      X      Y      Z

# Ciphertext: BCIZGROHEUBY
# Decrypted: HELXLOWORLDX