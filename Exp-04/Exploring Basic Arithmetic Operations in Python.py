'''
AIM: 6. Exploring Basic Arithmetic Operations in Python*:
Write a Python program to explore basic arithmetic operations.
The program should prompt the user to enter two numbers
and then perform addition, subtraction, multiplication,
division, and modulus operations on those numbers.
The results of each operation should be displayed to the user.

Hint:
Perform basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

NAME: SHAIKH MOHD ASHFAQUE
'''
# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined (modulus by zero)"

# Display the results
print(f"\nAddition of {num1} and {num2}: {addition}")
print(f"Subtraction of {num1} and {num2}: {subtraction}")
print(f"Multiplication of {num1} and {num2}: {multiplication}")
print(f"Division of {num1} by {num2}: {division}")
print(f"Modulus of {num1} and {num2}: {modulus}")
