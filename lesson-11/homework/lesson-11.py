# Task1. 
# step1:Open the terminal and command prompt
# step2: Create a folder for your project ;
#     mkdir my_project
#     cd my_project
# create a virtual environment:
# python -m venv venv

# Step3: Activate the virtual environment
# venv\Scripts\activate
# Step4: Install python packages;
# pip install requests numpy pandas

# Step5: Freeze installed packages 
# pip freeze > requirements.txt

# Step6: Deactivate the virtual environment
# deactivate 
# Directory Example;
# my_project/
# |__venv/
# |__requirements.txt
# |__main.py 

# Task2.
# Step 1: Create a module named math_operations.py

# # math_operations.py
# # This module includes basic mathematical operations: add, subtract, multiply, and divide

# def add(a, b):
#     """Return the sum of two numbers."""
#     return a + b

# def subtract(a, b):
#     """Return the difference between two numbers."""
#     return a - b

# def multiply(a, b):
#     """Return the product of two numbers."""
#     return a * b

# def divide(a, b):
#     """Return the division of two numbers. Raises an error if b is zero."""
#     if b == 0:
#         raise ValueError("Cannot divide by zero.")
#     return a / b


# Step 2: Create a module named string_utils.py

# # string_utils.py
# # This module includes string utilities: reverse_string and count_vowels

# def reverse_string(s):
#     """Return the reverse of the input string."""
#     return s[::-1]

# def count_vowels(s):
#     """Return the number of vowels in the input string."""
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in s if char in vowels)

# Task3.
# Step 1: Create a directory named 'geometry'
# This will be your Python package.

# Step 2: Inside the 'geometry' directory, create a file named '__init__.py'
# This file makes 'geometry' a Python package.

# # geometry/__init__.py
# # (This file can be left empty or used to import components from submodules)

# Step 3: Create a file named 'circle.py' inside the 'geometry' directory

# # geometry/circle.py
# # This module includes functions to calculate area and circumference of a circle

# import math

# def calculate_area(radius):
#     """Return the area of a circle given the radius."""
#     return math.pi * radius ** 2

# def calculate_circumference(radius):
#     """Return the circumference of a circle given the radius."""
#     return 2 * math.pi * radius

# Step 1: Create a directory named 'file_operations'
# This will be your Python package.

# Step 2: Inside the 'file_operations' directory, create a file named '__init__.py'
# This file makes 'file_operations' a Python package.

# # file_operations/__init__.py
# # (This file can be left empty or used to import components from submodules)

# Step 3: Create a file named 'file_reader.py' inside the 'file_operations' directory

# # file_operations/file_reader.py
# # This module defines a function to read contents from a file

# def read_file(file_path):
#     """Read and return the content of the specified file."""
#     try:
#         with open(file_path, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return "File not found."


# Step 4: Create a file named 'file_writer.py' inside the 'file_operations' directory

# # file_operations/file_writer.py
# # This module defines a function to write content to a file

# def write_file(file_path, content):
#     """Write the given content to the specified file."""
#     with open(file_path, 'w') as file:
#         file.write(content)





 