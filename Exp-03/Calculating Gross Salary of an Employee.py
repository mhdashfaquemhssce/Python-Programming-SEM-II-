'''
AIM: 4. Calculating Gross Salary of an Employee*:
Write a Python program to calculate the gross salary of an employee.
The program should prompt the user for the basic salary (BS)
and then compute the dearness allowance (DA) as 70% of BS,
the travel allowance (TA) as 30% of BS,
and the house rent allowance (HRA) as 10% of BS. Finally,
it should calculate the gross salary as the sum of BS, DA, TA,
and HRA and display the result.

Hint:

Calculate allowances
dearness_allowance = 0.70 * basic_salary # 70% of BS
travel_allowance = 0.30 * basic_salary # 30% of BS
house_rent_allowance = 0.10 * basic_salary # 10% of BS

NAME: SHAIKH MOHD ASHFAQUE
'''

# Prompt the user for the basic salary
basic_salary = float(input("Enter the basic salary (BS) of the employee: "))

# Calculate allowances
dearness_allowance = 0.70 * basic_salary  # 70% of BS
travel_allowance = 0.30 * basic_salary    # 30% of BS
house_rent_allowance = 0.10 * basic_salary  # 10% of BS

# Calculate gross salary
gross_salary = basic_salary + dearness_allowance + travel_allowance + house_rent_allowance

# Display the result
print(f"\nBasic Salary (BS): {basic_salary:.2f}")
print(f"Dearness Allowance (DA): {dearness_allowance:.2f}")
print(f"Travel Allowance (TA): {travel_allowance:.2f}")
print(f"House Rent Allowance (HRA): {house_rent_allowance:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
