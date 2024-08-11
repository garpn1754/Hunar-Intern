def encrypt(message, shift):
    """Encrypt a message using the Caesar Cipher algorithm"""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    """Decrypt a message using the Caesar Cipher algorithm"""
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    while True:
        print("Simple Encryption and Decryption Tool")
        print("----------------------------------------")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted Message:", encrypted_message)
        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(encrypted_message, shift)
            print("Decrypted Message:", decrypted_message)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()