# =====================================================
# Tugas Mini - Kriptografi 02
# Implementasi Caesar & Vigenère Cipher (Enkripsi & Dekripsi Otomatis)
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


# =====================================================
# Program Utama
# =====================================================

print("=== Tugas Mini Kriptografi 02 ===")
print("Implementasi Caesar & Vigenère Cipher\n")

# Baca input dari file
try:
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("⚠️ File 'input.txt' tidak ditemukan.")
    exit()

# Parameter Cipher
shift = 3
key = "LEMON"

# Siapkan file output
with open('output.txt', 'w') as f:
    f.write("=== Hasil Tugas Mini Kriptografi 02 ===\n\n")

    # Proses tiap baris teks dari file input
    for i, text in enumerate(lines, start=1):
        f.write(f"Plaintext [{i}]: {text}\n")

        # Caesar Cipher
        c_cipher = caesar_encrypt(text, shift)
        c_plain = caesar_decrypt(c_cipher, shift)
        f.write(f"  Caesar Encrypt : {c_cipher}\n")
        f.write(f"  Caesar Decrypt : {c_plain}\n")

        # Vigenere Cipher
        v_cipher = vigenere_encrypt(text, key)
        v_plain = vigenere_decrypt(v_cipher, key)
        f.write(f"  Vigenère Key   : {key}\n")
        f.write(f"  Vigenère Encrypt : {v_cipher}\n")
        f.write(f"  Vigenère Decrypt : {v_plain}\n\n")

print("✅ Proses selesai! Hasil tersimpan di 'output.txt'")