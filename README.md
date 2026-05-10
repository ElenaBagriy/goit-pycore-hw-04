# Homework Assignment goit-pycore-hw-04: Working with Files and the Module System
## Task 1

You have a text file that contains information about the monthly salaries of developers in your company. Each line in the file contains the developer's surname and salary separated by a comma without spaces.

For example:

```text
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

Your task is to develop a function `total_salary(path)` that analyzes this file and returns the total and average salary amount of all developers.

### Task Requirements

* The function `total_salary(path)` must accept one argument — the path to the text file (`path`).
* The file contains developers' salary data separated by commas. Each line represents one developer.
* The function must analyze the file and calculate the total and average salary amount.
* The result of the function must be a tuple of two numbers: the total salary amount and the average salary.

### Evaluation Criteria

* The function must correctly calculate the total and average amounts.
* Cases where the file is missing or corrupted must be handled.
* The code must be clean, well-structured, and understandable.

### Example of Function Usage

```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary amount: {total}, Average salary: {average}")
```

Expected result:

```text
Total salary amount: 6000, Average salary: 2000
```
---
## Task 2

You have a text file that contains information about cats. Each line in the file contains a unique cat identifier, its name, and age separated by commas. For example:

```text
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

The task is to develop a function `get_cats_info(path)` that reads this file and returns a list of dictionaries containing information about each cat.

### Task Requirements

* The function `get_cats_info(path)` must accept one argument — the path to the text file (`path`).
* The file contains cat data where each record includes a unique identifier, the cat's name, and age.
* The function must return a list of dictionaries, where each dictionary contains information about one cat.

### Evaluation Criteria

* The function must correctly process the data and return the correct list of dictionaries.
* Proper exception and error handling must be implemented.
* The code must be clean, well-structured, and understandable.

### Example of Function Usage

```python id="bq16zt"
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

Expected result:

```python id="zj8o4l"
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
```
---

## Task 3

Develop a script that accepts a directory path as a command-line argument and visualizes the structure of that directory by displaying the names of all subdirectories and files. For better visual perception, directory and file names should be displayed in different colors.

### Task Requirements

- Create a Python virtual environment to isolate project dependencies.
- The script must receive the directory path as an argument when launched. This path specifies where the directory whose structure should be displayed is located.
- Use the `colorama` library to implement colored output.
- The script must correctly display both directory names and file names using a recursive method for directory traversal (optionally, a non-recursive method may also be used).
- Error checking and handling must be implemented, for example if the specified path does not exist or does not point to a directory.

### Evaluation Criteria

- Creation and use of a virtual environment.
- Correct retrieval and processing of the directory path.
- Accurate display of the directory structure.
- Correct use of colored output with `colorama`.
- Code quality, including readability, structure, and comments.

### Example Usage

If you run the script and pass the absolute path to a directory as a parameter:

```bash
python hw03.py /path/to/your/directory
```

This will display in the terminal a list of all subdirectories and files in the specified directory using different colors for subdirectories and files, making the file structure easier to read.
---
## Task 4

Write a console assistant bot that recognizes commands entered from the keyboard and responds according to the entered command.

In this homework, we focus on the interface of the bot itself. The simplest and most convenient interface at the initial stage of development is a CLI (Command Line Interface) application. A CLI is relatively easy to implement.

Any CLI consists of three main elements:

- **Command parser** — responsible for parsing user input, extracting keywords and command modifiers from the string.
- **Command handler functions** — a set of functions (also called handlers) that are responsible for executing commands.
- **Request-response loop** — part of the application responsible for receiving user input and returning responses from handler functions.

At the first stage, the assistant bot must be able to store a name and phone number, find a phone number by name, change a saved phone number, and display all stored records. To implement this logic, we will use a dictionary. The dictionary will store the user's name as the key and the phone number as the value.

### Task Requirements

- The program must contain a `main()` function that manages the main command-processing loop.
- Implement a `parse_input()` function that parses the user's input into a command and its arguments. Commands and arguments must be recognized regardless of input case.
- The program must wait for user input and process commands using appropriate functions. If the user enters `"exit"` or `"close"`, the program must terminate.
- Implement handler functions for different commands such as `add_contact()`, `change_contact()`, `show_phone()`, etc.
- Use a Python dictionary to store names and phone numbers. The name is the key, and the phone number is the value.
- The program must detect and report invalid commands.

### Evaluation Criteria

- The bot must run in an infinite loop waiting for user commands.
- The bot must terminate when it receives `"close"` or `"exit"`.
- The bot is case-insensitive for commands.
- The bot supports the following commands:

#### `"hello"`
Responds with:
```text id="h2k8sa"
How can I help you?
```

#### `"add username phone"`

Stores a new contact in memory (dictionary).

Input:

```text id="p0q2ld"
add John 1234567890
```

Output:

```text id="k8s1mf"
Contact added.
```

#### `"change username phone"`

Updates an existing contact's phone number.

Input:

```text id="c1x9aa"
change John 0987654321
```

Output:

```text id="m4n8bb"
Contact updated.
```

(or an error message if the contact is not found)

#### `"phone username"`

Returns the phone number for the given contact.

Input:

```text id="t7v2cc"
phone John
```

Output:

```text id="z9k1dd"
1234567890
```

(or an error message if the contact is not found)

#### `"all"`

Displays all saved contacts.

#### `"close"` or `"exit"`

Terminates the program after printing:

```text id="g6p3ee"
Good bye!
```

Any command that does not match the defined formats is considered invalid and should output:

```text id="x1m9ff"
Invalid command.
```

### Additional Requirement

* Command logic must be implemented in separate functions.
* These functions must take one or more strings as input and return a string.
* All user interaction (`print` and `input`) must be implemented only inside the `main()` function.
