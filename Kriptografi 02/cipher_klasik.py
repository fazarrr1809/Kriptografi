# =====================================================
# Praktikum Kriptografi 02 - Implementasi Cipher Klasik
# Implementasi Caesar dan Vigenère Cipher dengan File I/O
# =====================================================

# --- Caesar Cipher ---
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)


# --- Vigenère Cipher ---
def vigenere_encrypt(plain, key):
    key = key.upper()
    result = ''
    for i, char in enumerate(plain.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    key = key.upper()
    result = ''
    for i, char in enumerate(cipher.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

print("=== Praktikum Kriptografi 02 ===")
print("Implementasi Caesar & Vigenère Cipher\n")

# Membaca teks dari file input.txt
try:
    with open('input.txt', 'r') as f:
        text = f.read().strip()
except FileNotFoundError:
    print("⚠️ File 'input.txt' tidak ditemukan. Buat file input.txt terlebih dahulu.")
    exit()

print(f"Teks Asli   : {text}")

# Parameter
shift = 3              # nilai geser untuk Caesar
key = "LEMON"          # kunci untuk Vigenere

# Proses Caesar Cipher
caesar_cipher = caesar_encrypt(text, shift)
caesar_plain = caesar_decrypt(caesar_cipher, shift)

# Proses Vigenere Cipher
vigenere_cipher = vigenere_encrypt(text, key)
vigenere_plain = vigenere_decrypt(vigenere_cipher, key)

print("\n=== Hasil Caesar Cipher ===")
print(f"Ciphertext : {caesar_cipher}")
print(f"Dekripsi   : {caesar_plain}")

print("\n=== Hasil Vigenère Cipher ===")
print(f"Kunci       : {key}")
print(f"Ciphertext  : {vigenere_cipher}")
print(f"Dekripsi    : {vigenere_plain}")

with open('output.txt', 'w') as f:
    f.write("=== Caesar Cipher ===\n")
    f.write(f"Ciphertext: {caesar_cipher}\n")
    f.write(f"Dekripsi: {caesar_plain}\n\n")
    f.write("=== Vigenère Cipher ===\n")
    f.write(f"Kunci: {key}\n")
    f.write(f"Ciphertext: {vigenere_cipher}\n")
    f.write(f"Dekripsi: {vigenere_plain}\n")

print("\n✅ Hasil enkripsi dan dekripsi telah disimpan ke 'output.txt'")
