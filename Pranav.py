# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift alphabetic characters
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Reverse shift alphabetic characters
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

# Main program
def caesar_cipher():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")

# Run the program
caesar_cipher()
