# Digital Contact Manager

# Pre-initialize contacts dictionary with sample data
contacts = {
    "Lukasz Langa": {
        "phones": ["9876543210", "8765432109"],
        "email": "lukasz@email.com"
    },
    "Daniel Feldroy": {
        "phones": ["9123456780"],
        "email": "daniel@email.com"
    },
    "Doug Hellmann": {
        "phones": ["9988776655"],
        "email": "doug@email.com"
    }
}

def display_initial_contacts():
    """Display initial contacts as shown in expected output"""
    print("// Initial Contacts:")
    for name in contacts:
        phones_str = ", ".join(contacts[name]["phones"])
        email = contacts[name]["email"]
        print(f"{name}: phones: {phones_str}, email: {email}")

def display_menu():
    """Display the menu options"""
    print("\n### MENU: ###")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. Display contacts")
    print("5. Exit")

def add_contact():
    """Add a new contact to the dictionary"""
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contacts[name] = {
        "phones": [phone],
        "email": email
    }
    print(f"Contact '{name}' added.")

def delete_contact():
    """Remove a contact from the dictionary"""
    name = input("Enter name: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Not found.")

def update_contact():
    """Add a new phone number to an existing contact"""
    name = input("Enter name: ")
    
    if name in contacts:
        new_phone = input("Enter new phone: ")
        contacts[name]["phones"].append(new_phone)
        print(f"Phone number added for '{name}'.")
    else:
        print("Not found.")

def display_contacts():
    """Display all contacts sorted alphabetically by name"""
    print("\nContacts list:")
    
    # Sort contacts alphabetically by name
    sorted_names = sorted(contacts.keys())
    
    for name in sorted_names:
        phones_str = ", ".join(contacts[name]["phones"])
        email = contacts[name]["email"]
        print(f"# {name}:")
        print(f"   Phones: {phones_str}")
        print(f"   Email: {email}")

def main():
    """Main program loop"""
    # Display initial contacts
    display_initial_contacts()
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Program closed!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()