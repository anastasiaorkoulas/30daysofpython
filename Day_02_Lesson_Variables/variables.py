# [03/26/2026] Variables

"""
Working Notes - Right out the gate, I'm doing some things that aren't explicitly recommended by the challenge,
mostly best practice things like consolidating simple variables into single line declarations and trimming
down some print statements. I'm trying to strike a balance between following the instructions (because it has been
something like five years since I've coded anything) and writing code as cleanly as I can right now. I have had
to restrain myself from using dictionaries and loops, which I figure will come up soon enough.

I removed the Boolean variables 'is_true' and 'is_light_on' from the first exercise because they aren't used in any
of the exercises in the same way that the other variables are - 'is_married' should be sufficient for the purposes
of these exercises :)
"""

first_name, last_name, country, city = 'Anastasia', 'Orkoulas', 'United States of America', 'Fort Lauderdale'
age, year = 31, 2026
is_married = False

#1 . Declare variables for your name, country, city, and age,
# as well as the current year and whether you are married or not.
first_name_information = f"First Name: {first_name} \u2022 Type: {type(first_name)}\n"
last_name_information = f"Last Name: {last_name} \u2022 Type: {type(last_name)}\n"
country_information = f"Country: {country} \u2022 Type: {type(country)}\n"       
city_information = f"City: {city} \u2022 Type: {type(city)}\n"
age_information = f"Age: {age} \u2022 Type: {type(age)}\n"
year_information = f"Year: {year} \u2022 Type: {type(year)}\n"
is_married_information = f"Is the user married?: {is_married} \u2022 Type: {type(is_married)}\n"

print(f"Variable Information:\n")
print(first_name_information, last_name_information, country_information, city_information, age_information, year_information, is_married_information)


#2. Using the len() built-in function, find the length of your first name and your last name.
first_name_length, last_name_length = f"Length of First Name ({first_name}): {len(first_name)}\n", f"Length of Last Name ({last_name}): {len(last_name)}\n"


#3. Compare the length of your first name and your last name.
if len(first_name) > len(last_name):
    name_comparison = f"The subject's first name, {first_name}, is longer than their last name, {last_name}.\n"
elif len(first_name) < len(last_name):
    name_comparison = f"The subject's last name, {last_name}, is longer than their first name, {first_name}.\n"
else:
    name_comparison = f"The subject's first name, {first_name}, and last name, {last_name}, are of equal length.\n"

print(f"String Lengths and Comparison:\n")
print(first_name_length, last_name_length, name_comparison)


#4. Declare 5 as num_one and 4 as num_two. Perform addition, subtraction, multiplication, division and modulus operations and print the results.
num_one, num_two = 5, 4
total, diff, product, division, remainder, exp, floor_division = num_one + num_two, num_one - num_two, num_one * num_two, num_one / num_two, num_one % num_two, num_one ** num_two, num_one // num_two

print(f"Arithmetic Operators:\n")
print(f"{num_one} + {num_two} = {total}")
print(f"{num_one} - {num_two} = {diff}")
print(f"{num_one} * {num_two} = {product}")
print(f"{num_one} / {num_two} = {division}")
print(f"{num_one} % {num_two} = {remainder}")
print(f"{num_one} ** {num_two} = {exp}")
print(f"{num_one} // {num_two} = {floor_division}\n")


#5. Take the radius of a circle as user input, then calculate its area and circumference.
print(f"Calculating the area and circumference of a circle:\n\n")
radius = float(input("Enter the radius of the circle:\n"))
circle_area, circle_circumference = 3.14 * radius ** 2, 2 * 3.14 * radius

print(f"\nThe area of a circle with a radius of {radius} is {circle_area}.\n")
print(f"The circumference of a circle with a radius of {radius} is {circle_circumference}.\n")


#6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names.
user_first_name = input("Please enter your first name:\n")
user_last_name = input("Please enter your last name:\n")
user_country = input("Please enter your country:\n")
user_age = int(input("Please enter your age:\n"))

print(f"User Input:\n")
print(f"Hello, {user_first_name} {user_last_name} from {user_country}. You are {user_age} years old.\n")


# I can't help myself :^)
if first_name == user_first_name and last_name == user_last_name and country == user_country and age == user_age:
    print(f"It looks like you're me.\n")
else:    print(f"Nice to meet you, {user_first_name} {user_last_name} from {user_country}. You are {user_age} years old.\n")

print(f"\nEnd of Day 2 exercises.\n") 