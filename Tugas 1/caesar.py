def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

if __name__ == "__main__":
    print("=== Caesar Cipher ===")
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan kunci (angka pergeseran): "))
    cipher = caesar_encrypt(text, shift)
    print("Ciphertext:", cipher)
    print("Dekripsi:", caesar_decrypt(cipher, shift))
