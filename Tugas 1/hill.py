import numpy as np

def hill_encrypt(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i+1]) - 65]
        enc = np.dot(key_matrix, pair) % 26
        result += chr(int(enc[0]) + 65) + chr(int(enc[1]) + 65)
    return result

if __name__ == "__main__":
    print("=== Hill Cipher ===")
    text = input("Masukkan teks: ")
    print("Gunakan matriks 2x2 (contoh: 3 3; 2 5)")
    a, b = map(int, input("Baris 1 (dua angka): ").split())
    c, d = map(int, input("Baris 2 (dua angka): ").split())
    key = np.array([[a, b], [c, d]])
    cipher = hill_encrypt(text, key)
    print("Ciphertext:", cipher)