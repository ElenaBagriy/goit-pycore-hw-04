from colorama import Fore, Style, init
import sys
from pathlib import Path


# Initialize colorama so colors reset automatically after each print
init(autoreset=True)

# Recursively print the directory structure with indentation and colors
def create_path_tree(item: Path, depth: int = 0):
    # Create indentation based on directory depth
    indent = "    " * depth  # 4 spaces on the level

    # Check if the path exists
    if not item.exists():
        print(Fore.RED + Style.BRIGHT +f"The path {item} doesn't exist")
        return
    
    # If the item is a directory, print it and process its children recursively
    if item.is_dir():
        print(indent + Fore.BLUE + Style.BRIGHT + f"{item.name}")

        # Iterate through all files and folders inside the directory
        for child in item.iterdir(): 
            create_path_tree(child, depth + 1)
    # If the item is a file, print it in a different color
    else:
        print(indent + Fore.GREEN + f"{item.name}")


# Entry point for the script. Starts processing the provided path.
def main(path):
    item = Path(path)
    create_path_tree(item)

# Check if a path was provided
if len(sys.argv) < 2:
    print(Fore.BLUE + Style.BRIGHT + "Type in the terminal: python hw03.py <path>")
    sys.exit()
else:
    main(sys.argv[1])