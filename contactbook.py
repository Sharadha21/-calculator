class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Added {name} with number {number} to contacts.")

    def get_contact(self, name):
        if name in self.contacts:
            return f"{name}: {self.contacts[name]}"
        else:
            return f"{name} not found in contacts."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} deleted from contacts.")
        else:
            print(f"{name} not found in contacts.")

    def display_contacts(self):
        print("Contact List:")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")


def main():
    contact_book = ContactBook()
    while True:
        print("\n menu  Menu:")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            contact_book.add_contact(name, number)
        elif choice == '2':
            name = input("Enter name to get contact: ")
            print(contact_book.get_contact(name))
        elif choice == '3':
            name = input("Enter name to delete contact: ")
            contact_book.delete_contact(name)
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
