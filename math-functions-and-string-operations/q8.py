def encode_message():
    """Encode a plain-text message into Unicode numbers."""
    message = input("Enter your secret message: ")
    
    # Convert each character to its Unicode number
    encoded_numbers = []
    for char in message:
        unicode_number = ord(char)
        encoded_numbers.append(str(unicode_number))
    
    # Join the numbers with spaces and display
    encoded_message = ' '.join(encoded_numbers)
    print("\nHere is your encoded message:")
    print(encoded_message)


def decode_message():
    """Decode a string of numbers back into the original message."""
    secret_code = input("Enter the secret code: ")
    
    # Split the code into individual numbers
    numbers = secret_code.split()
    
    # Convert each number back to its character
    decoded_characters = []
    for number in numbers:
        try:
            unicode_number = int(number)
            character = chr(unicode_number)
            decoded_characters.append(character)
        except ValueError:
            print(f"Error: '{number}' is not a valid number.")
            return
        except ValueError:
            print(f"Error: {unicode_number} is not a valid Unicode number.")
            return
    
    # Join all characters into the original message
    decoded_message = ''.join(decoded_characters)
    print("\nYour decoded message:")
    print(decoded_message)


def main():
    """Main function to choose between encoding and decoding."""
    print("Secret Message Encoder & Decoder")
    print("1. Encode a message")
    print("2. Decode a message")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            encode_message()
            break
        elif choice == '2':
            decode_message()
            break
        else:
            print("Please enter 1 or 2.")


if __name__ == "__main__":
    main()