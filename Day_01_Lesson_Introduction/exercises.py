"""
Day 1: Exercises

Complete the three levels of exercises:
Level 1: Basics
Level 2: Intermediate
Level 3: Advanced

Instructions:
1. Read the problem
2. Write the code to solve it
3. Test your code
"""

# =======================================
# LEVEL 1: EXERCISES
# ==========================================

# 1. Check the python version
import sys
print(f"Python version: {sys.version}")

# 2. Create a string 'Flutter is awesome'
flutter_string = 'Flutter is awesome'
print(flutter_string)

# 3. Print the following string in different ways
# 'I hope you are enjoying this challenge.'
print('I hope you are enjoying this challenge.')
print("I hope you are enjoying this challenge.")

# 4. Check the data types of the following values
print(type(1))                          # int
print(type(9.8))                        # float
print(type(3.14))                       # float
print(type(4 - 4j))                     # complex
print(type(['Asabeneh', 'Python', 'Finland']))  # list
print(type('Asabeneh'))                 # str
print(type('Finland'))                  # str

# ==========================================
# LEVEL 2: EXERCISES
# ==========================================

# 1. Write a script that prompts user input
# Uncomment the following to use it
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# country = input("What is your country? ")
# print(f"Hello {first_name} {last_name}, from {country}")

# 2. Check data types of some variables
my_name = "John"
my_age = 25
height = 5.9
is_married = False
skills = ["Python", "JavaScript", "HTML"]

print(type(my_name))
print(type(my_age))
print(type(height))
print(type(is_married))
print(type(skills))

# ==========================================
# LEVEL 3: EXERCISES
# ==========================================

# 1. Write examples for different data types
# Number
integer = 10
floating = 3.14
complex_number = 4 + 2j

# String
name = "John Doe"

# Boolean
has_license = True
is_smart = False

# List
fruits = ['apple', 'banana', 'orange']

# Dictionary
person = {
    'name': 'John',
    'age': 30,
    'country': 'USA'
}

# Tuple
coordinates = (10, 20, 30)

# Set
unique_numbers = {1, 2, 3, 4, 5}

print("=== Data Types Examples ===")
print(f"Integer: {integer}, Type: {type(integer)}")
print(f"Float: {floating}, Type: {type(floating)}")
print(f"Complex: {complex_number}, Type: {type(complex_number)}")
print(f"String: {name}, Type: {type(name)}")
print(f"Boolean: {has_license}, Type: {type(has_license)}")
print(f"List: {fruits}, Type: {type(fruits)}")
print(f"Dictionary: {person}, Type: {type(person)}")
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")
print(f"Set: {unique_numbers}, Type: {type(unique_numbers)}")

# 2. Find Euclidean distance between (2, 3) and (10, 8)
import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"\nEuclidean distance between ({x1}, {y1}) and ({x2}, {y2}): {distance}")
