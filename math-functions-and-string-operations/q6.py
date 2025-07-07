import random


def get_user_name():
    """Get first and last name from user input."""
    while True:
        user_input = input("Enter your first and last name: ").strip()
        parts = user_input.split()
        
        if len(parts) >= 2:
            first_name = parts[0]
            last_name = parts[1]
            return first_name, last_name
        else:
            print("Please enter both first and last name.")


def generate_username(first_name, last_name):
    """Generate a fun username based on the specified rules."""
    # First character: first letter of first name (lowercase)
    first_char = first_name[0].lower()
    
    # Next four characters: first four letters of last name (repeating as needed)
    last_name_lower = last_name.lower()
    middle_chars = ""
    
    # Repeat last name characters to get exactly 4 characters
    for i in range(4):
        middle_chars += last_name_lower[i % len(last_name_lower)]
    
    # Last two characters: random two-digit number
    random_number = random.randint(10, 99)
    
    # Combine all parts
    username = first_char + middle_chars + str(random_number)
    
    return username


def main():
    """Main function to orchestrate username generation."""
    # Get user input
    first_name, last_name = get_user_name()
    
    # Generate username
    username = generate_username(first_name, last_name)
    
    # Display result
    print(f"Your username is: {username}")


if __name__ == "__main__":
    main()