import string

def generate_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [c for c in key + ''.join([x for x in alphabet if x not in key])]
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) and text[i+1] != a else 'X'
        pairs.append((a, b))
        i += 2 if i+1 < len(text) and text[i+1] != a else 1

    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

if __name__ == "__main__":
    print("=== Playfair Cipher ===")
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci: ")
    cipher = playfair_encrypt(text, key)
    print("Ciphertext:", cipher)