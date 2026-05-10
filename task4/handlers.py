# Parse user input into command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Add a new contact to the dictionary
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Change phone number for an existing contact
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    
    return "Contact not found."

# Show phone number for a specific contact
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if name in contacts:
        return contacts[name]
    
    return "Contact not found."

# Show all saved contacts
def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()