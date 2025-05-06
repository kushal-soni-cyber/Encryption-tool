def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

if __name__ == "__main__":
    choice = input("Encrypt or Decrypt (e/d): ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift (e.g., 3): "))

    if choice == 'e':
        print("Encrypted:", caesar_cipher(text, shift))
    elif choice == 'd':
        print("Decrypted:", caesar_cipher(text, -shift))
    else:
        print("Invalid choice.")
