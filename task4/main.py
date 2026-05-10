from handlers import parse_input, add_contact, change_contact, show_phone, show_all


# Main function that runs the assistant bot
def main():
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        # Get user input
        user_input = input("Enter a command: ")
        # Parse command and arguments
        command, *args = parse_input(user_input)

        # Exit the program
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Greeting command
        elif command == "hello":
            print("How can I help you?")

        # Add new contact
        elif command == "add":
            print(add_contact(args, contacts))

        # Change existing contact
        elif command == "change":
            print(change_contact(args, contacts))

        # Show phone number
        elif command == "phone":
            print(show_phone(args, contacts))

        # Show all contacts
        elif command == "all":
            print(show_all(contacts))

        # Handle unknown commands
        else:
            print("Invalid command.")

# Start the program
if __name__ == "__main__":
    main()