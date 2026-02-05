'''
Triangle Pattern Generator Using Loops
This program prints a right-angled triangle pattern using stars (*)
It demonstrates Python loop syntax similar to C but simpler and cleaner.
'''

# Take number of rows from the user
# In C: scanf("%d", &rows);
# In Python: input() is used and converted to int
rows = int(input("Enter the number of rows: "))

# for loop in Python
# range(1, rows + 1) generates numbers from 1 to rows
# In C: for(i = 1; i <= rows; i++)
for i in range(1, rows + 1):
    
    # "*" * i repeats the star character i times
    # This replaces the inner loop commonly used in C
    print("*" * i)

