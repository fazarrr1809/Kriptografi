# -----------------------------
# VIGENERE CIPHER IMPLEMENTATION
# -----------------------------

# Fungsi Enkripsi
def vigenere_encrypt(plain, key):
    plain = plain.upper().replace(" ", "")
    key = key.upper()
    res = ''
    for i in range(len(plain)):
        res += chr(((ord(plain[i]) - 65 + ord(key[i % len(key)]) - 65) % 26) + 65)
    return res

# Fungsi Dekripsi
def vigenere_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    key = key.upper()
    res = ''
    for i in range(len(cipher)):
        res += chr(((ord(cipher[i]) - ord(key[i % len(key)])) % 26) + 65)
    return res

# Uji Program
plain = "HELLO WORLD"
key = "LEMON"

cipher = vigenere_encrypt(plain, key)
print("Plaintext :", plain)
print("Key       :", key)
print("Ciphertext:", cipher)

decrypted = vigenere_decrypt(cipher, key)
print("Dekripsi  :", decrypted)

from collections import Counter
import matplotlib.pyplot as plt

def frequency_analysis(text):
    text = text.upper().replace(" ", "")
    count = Counter(text)
    print("\n=== Analisis Frekuensi Huruf ===")
    for k, v in count.items():
        print(f"{k}: {v/len(text):.2f}")

    # Visualisasi
    plt.bar(count.keys(), [v/len(text) for v in count.values()])
    plt.title("Analisis Frekuensi Ciphertext")
    plt.xlabel("Huruf")
    plt.ylabel("Frekuensi Relatif")
    plt.show()

# Panggil fungsi untuk ciphertext yang dihasilkan
frequency_analysis(cipher)
