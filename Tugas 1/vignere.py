def vigenere_encrypt(text, key):
    text, key = text.upper(), key.upper()
    result, key_index = "", 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    cipher, key = cipher.upper(), key.upper()
    result, key_index = "", 0
    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    print("=== Vigenère Cipher ===")
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci (kata): ")
    cipher = vigenere_encrypt(text, key)
    print("Ciphertext:", cipher)
    print("Dekripsi:", vigenere_decrypt(cipher, key))