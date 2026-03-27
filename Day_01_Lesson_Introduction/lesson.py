"""
Day 1: Introduction to Python

Topics:
- Environment Setup
- Python Syntax
- Variables and Data Types
- Comments
- Print function

Resources:
https://github.com/asabeneh/30-days-of-python/blob/master/01_Day_Introduction/01_introduction.md
"""

# ##### Day 1 - 30 Days of Python Challenge #####

# ==== PRINT AND COMMENTS ====

print("Day 1 - 30DaysOfPython Challenge")
print("Welcome to Python!")

# This is a single line comment
# Comments start with # symbol

# Multiline comments can be written using triple quotes
""" 
This is a multiline comment.
You can use it to write longer explanations
or documentation.
"""

# ==== BASIC ARITHMETIC ====

print("\n=== Basic Arithmetic ===")
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# ==== STRINGS ====

print("\n=== Strings ===")
first_name = "Asabeneh"
last_name = "Yetayeh"
full_name = first_name + " " + last_name

print(f"Hello {first_name}")
print(f"My name is {full_name}")
print(f"I am enjoying 30 days of Python")

# ==== DATA TYPES ====

print("\n=== Data Types ===")
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex number
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(True))                # Boolean

# ==== VARIABLES ====

print("\n=== Variables ===")
my_age = 250
my_height = 1.80
my_complex_number = 1 + 3j

is_light_on = True
is_light_off = False

print(f"My age: {my_age}")
print(f"My height: {my_height}")
print(f"My complex number: {my_complex_number}")
print(f"Light on: {is_light_on}")

# ==== EXERCISES ====

# Exercise: Write your own information using variables
your_name = "Your Name Here"
your_age = 0
your_country = "Your Country"

print(f"\nHello, my name is {your_name}")
print(f"I am {your_age} years old")
print(f"I live in {your_country}")
