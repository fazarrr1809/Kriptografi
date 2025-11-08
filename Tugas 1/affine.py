def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    inv = mod_inverse(a, 26)
    result = ""
    for char in cipher.upper():
        if char.isalpha():
            result += chr(((inv * ((ord(char) - 65) - b)) % 26) + 65)
        else:
            result += char
    return result

if __name__ == "__main__":
    print("=== Affine Cipher ===")
    text = input("Masukkan teks: ")
    a = int(input("Masukkan nilai a (coprime dengan 26): "))
    b = int(input("Masukkan nilai b: "))
    cipher = affine_encrypt(text, a, b)
    print("Ciphertext:", cipher)
    print("Dekripsi:", affine_decrypt(cipher, a, b))
