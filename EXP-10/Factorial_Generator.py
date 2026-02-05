'''
Factorial Generator*:
Design a Python program to compute the factorial of a given integer N.
Name: Mohd Ashfque Shaikh
'''

# Factorial Calculation Without Function:
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")
