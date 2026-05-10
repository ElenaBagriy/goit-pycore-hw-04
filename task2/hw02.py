from pathlib import Path


# Create a path to the file relative to the current script location
path = Path(__file__).parent / "cats_kile.txt"

def get_cats_info(path: Path) -> list[dict]:
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:    
                    id, name, age = line.strip().split(',')
                    cats_info.append({"id": id, "name": name, "age": age})
                except ValueError:
                    # Skip malformed lines
                    continue
    except FileNotFoundError:
        return []
    return cats_info


cats_info = get_cats_info(path)
print(cats_info)