# Start with an empty dictionary called 'contacts'
contacts = {}

# Use a while loop to present a menu
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    # 1. Add contact (name and phone number)
    if choice == '1':
        name = input("Enter contact name: ").strip()
        if name in contacts:
            print(f"'{name}' already exists. Use a different name or update it.")
        else:
            phone = input("Enter phone number: ").strip()
            contacts[name] = phone
            print(f"Contact '{name}' added successfully!")
            
    # 2. Search contact (display phone number)
    elif choice == '2':
        name = input("Enter the name to search: ").strip()
        if name in contacts:
            print(f"Phone number for '{name}': {contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")
            
    # 3. Delete contact
    elif choice == '3':
        name = input("Enter the name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
            
    # 4. Display all contacts
    elif choice == '4':
        if not contacts:
            print("Your contact book is empty.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")
                
    # 5. Quit
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")