from pathlib import Path

# Create a path to the file relative to the current script location
path = Path(__file__).parent / "salary_file.txt"

def total_salary(path: Path) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            number_of_employees = 0
            salary_sum = 0

            for line in file:
                try:
                    # Split each line into name and salary
                    _, salary = line.split(',')
                    # Remove newline and convert salary to integer
                    salary_sum += int(salary.strip())
                    # Count employees
                    number_of_employees += 1
                except ValueError:
                    # Skip lines with incorrect format
                    continue

            if number_of_employees == 0:
                return (0, 0.0)
            # Calculate average salary
            average_salary = round(salary_sum / number_of_employees, 2)
            return (salary_sum, average_salary)
            
    except FileNotFoundError:
        print("Файл не існує.")
        return (0, 0.0)
    

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

