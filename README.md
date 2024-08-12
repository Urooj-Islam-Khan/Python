

# Python Learning Guide By Urooj Islam

## 1. Introduction to Python

### Definition
Python is a high-level, interpreted, and general-purpose programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

### Features
- **Easy to Learn**: Python’s syntax is clear and intuitive.
- **Interpreted**: Python code is executed line-by-line, making debugging easier.
- **Dynamic Typing**: Variables in Python do not need an explicit declaration.
- **Extensive Libraries**: Python has a rich standard library and third-party packages for various applications.
- **Cross-Platform**: Python is available on all major operating systems.

## 2. Basic Syntax

### Structure of a Python Program
```python
# This is a comment
print("Hello, World!")  # This prints text to the console
```

### Comments
```python
# This is a single-line comment

"""
This is a 
multi-line comment
"""
```

## 3. Data Types

### Primitive Data Types
- **int**: Integer values.
- **float**: Floating-point values.
- **str**: String values.
- **bool**: Boolean values (True or False).

**Example**:
```python
age = 25  # int
height = 5.9  # float
name = "Alice"  # str
is_student = True  # bool
```

### Non-Primitive Data Types
- **list**: Ordered, mutable collection of items.
- **tuple**: Ordered, immutable collection of items.
- **set**: Unordered collection of unique items.
- **dict**: Collection of key-value pairs.

**Example**:
```python
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.0, 20.0)

# Set
unique_numbers = {1, 2, 3, 4}

# Dictionary
person = {"name": "Alice", "age": 25}
```

## 4. Operators

### Arithmetic Operators
```python
a = 10
b = 5
sum = a + b          # Addition
difference = a - b   # Subtraction
product = a * b      # Multiplication
quotient = a / b     # Division
remainder = a % b    # Modulus
```

### Comparison Operators
```python
is_equal = (a == b)        # Equal to
is_not_equal = (a != b)    # Not equal to
is_greater = (a > b)       # Greater than
is_less = (a < b)          # Less than
is_greater_or_equal = (a >= b) # Greater than or equal to
is_less_or_equal = (a <= b)    # Less than or equal to
```

### Logical Operators
```python
result = (a > b) and (b < 10)  # Logical AND
result = (a > b) or (b > 10)   # Logical OR
result = not (a > b)           # Logical NOT
```

## 5. Control Structures

### Conditional Statements

#### If-Else
```python
num = 10
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

### Loops

#### For Loop
```python
for i in range(5):
    print(i)
```

#### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### List Comprehensions
```python
squares = [x**2 for x in range(10)]  # List comprehension
```

## 6. Functions

### Function Definition
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

### Lambda Functions
```python
add = lambda x, y: x + y
print(add(5, 3))  # Outputs: 8
```

## 7. Modules and Packages

### Importing Modules
```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```

### Creating a Module
**file: my_module.py**
```python
def greet(name):
    return f"Hello, {name}!"
```

**Usage**
```python
from my_module import greet
print(greet("Bob"))
```

## 8. File Handling

### Reading from a File
```python
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Writing to a File
```python
with open('output.txt', 'w') as file:
    file.write("Hello, World!")
```

## 9. Classes and Objects

### Class Definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.introduce())
```

## 10. Inheritance

### Inheritance Basics
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Inherited method
print(dog.bark())   # Derived method
```

## 11. Exception Handling

### Try-Except-Finally
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block always executes.")
```

### Raising Exceptions
```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
```

## 12. Regular Expressions

### Using Regular Expressions
```python
import re

pattern = re.compile(r'\d+')
matches = pattern.findall("There are 12 apples and 34 oranges.")
print(matches)  # Outputs: ['12', '34']
```

## 13. Working with Databases

### SQLite Example
```python
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert a record
cursor.execute('''INSERT INTO users (name) VALUES ('Alice')''')

# Query the table
cursor.execute('''SELECT * FROM users''')
print(cursor.fetchall())

# Commit changes and close the connection
conn.commit()
conn.close()
```

## 14. Multithreading

### Using the Threading Module
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create and start a new thread
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait for the thread to finish
```

## 15. Python Standard Libraries

### Commonly Used Libraries
- **os**: Interacting with the operating system (e.g., file operations).
- **sys**: System-specific parameters and functions.
- **datetime**: Working with dates and times.

### Example Usage
```python
import os
import datetime

print(os.getcwd())  # Outputs the current working directory
print(datetime.datetime.now())  # Outputs the current date and time
```



