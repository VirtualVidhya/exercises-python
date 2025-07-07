def get_baby_names():
    """Return the list of popular baby names."""
    names = [
        "Amiya", "Aarav", "Aarna", "Avyaya", "Anura", "Barkha", "Chhavi", 
        "Chaah", "Dhithi", "Dvij", "Falak", "Hanita", "Izaan", "Jiyaan", 
        "Krishiv", "Laya", "Mahi", "Moh", "Navya", "Nirvan", "Nirmay", 
        "Nahar", "Nadhiya", "Ojal", "Ojas", "Parishi", "Praan", "Rahi", 
        "Sakhi", "Shay", "Yuti"
    ]
    return names


def get_first_letter():
    """Get the first letter from user input."""
    while True:
        letter = input("Enter the first letter: ").strip()
        
        if len(letter) == 1 and letter.isalpha():
            return letter.upper()
        else:
            print("Please enter a single letter.")


def find_names_by_letter(names, letter):
    """Find all names that start with the given letter."""
    matching_names = []
    
    for name in names:
        if name.upper().startswith(letter.upper()):
            matching_names.append(name)
    
    return matching_names


def display_results(names, letter):
    """Display the matching names or a message if none found."""
    if names:
        print("\nNames found:")
        for name in sorted(names):
            print(name)
    else:
        print(f"\nNo names found starting with '{letter}'.")


def main():
    """Main function to orchestrate the baby name search."""
    # Get the list of baby names
    baby_names = get_baby_names()
    
    # Get user input for the first letter
    first_letter = get_first_letter()
    
    # Find matching names
    matching_names = find_names_by_letter(baby_names, first_letter)
    
    # Display results
    display_results(matching_names, first_letter)


if __name__ == "__main__":
    main()