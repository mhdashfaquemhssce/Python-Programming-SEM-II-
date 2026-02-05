'''
Number Type Identifier*:
Develop a Python program that takes a numerical input and
identifies whether it is even or odd,
utilizing conditional statements and loops.
Name: Mohd Ashfaque Shaikh
'''

while True:
    num = input("Enter a number (or type '0' to exit): ")

    if num == "0":
        print("Exiting program.")
        break

    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):  # Check if input is a valid integer
        num = int(num)
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    else:
        print("Invalid input! Please enter an integer.")
