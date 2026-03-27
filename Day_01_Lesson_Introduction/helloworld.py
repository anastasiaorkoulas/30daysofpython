import math

# [03/26/2026] Introduction

"""
Working Notes - Right out the gate, I'm doing some things that aren't explicitly recommended by the challenge,
Working Notes - I noticed that the exercises for Day 1 are very similar to the exercises for Day 2, just focused
on getting familiar with simple print statements, testing different operations, and using a couple of built-in
functions. I *did* notice that there is a third difficulty level for Day 1 that includes a few more data types,
so this file is focused on that.
"""

#1 . Write an example for the following data types: Number (int, float, complex), String, Boolean, List, Tuple, Set and Dictionary.

# Numbers (Int, Float, Complex)
print("\n=== Numbers ===")
integer_number = 10 # Integer (int)
float_number = 3.14 # Float (float)
complex_number = 1 + 2j # Complex number (complex)
string_variable = "String" # String (str)
boolean_variable = True # Boolean (bool)
list_variable = [1, 2, 3] # List (list)
tuple_variable = (1, 2, 3) # Tuple (tuple)
set_variable = {1, 2, 3} # Set (set)
dictionary_variable = {"key": "value"} # Dictionary (dict)

print(f"Integer: {integer_number} \u2022 Type: {type(integer_number)}")
print(f"Float: {float_number} \u2022 Type: {type(float_number)}")
print(f"Complex Number: {complex_number} \u2022 Type: {type(complex_number)}")
print(f"String: {string_variable} \u2022 Type: {type(string_variable)}")
print(f"Boolean: {boolean_variable} \u2022 Type: {type(boolean_variable)}")
print(f"List: {list_variable} \u2022 Type: {type(list_variable)}")
print(f"Tuple: {tuple_variable} \u2022 Type: {type(tuple_variable)}")
print(f"Set: {set_variable} \u2022 Type: {type(set_variable)}")
print(f"Dictionary: {dictionary_variable} \u2022 Type: {type(dictionary_variable)}")

 # 2. Find a Euclidean distance between (2, 3) and (10, 8)
point_a = (2, 3)
point_b = (10, 8)
euclidean_distance = math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)
print(f"\nThe Euclidean distance between {point_a} and {point_b} is {euclidean_distance}.\n") 