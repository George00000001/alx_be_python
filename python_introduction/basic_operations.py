"""0. Basic Arithmetic Exercise
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: To practice basic arithmetic operations in Python by performing predefined calculations.

Task Description:

You are required to complete a Python script that performs basic arithmetic operations with two predefined numbers. The script should do the following:

Assign specific values to two variables, number1 and number2.
Perform addition, subtraction, and multiplication on these numbers.
Print the results of these operations in a human-readable format.
Instructions:

Create a file named basic_operations.py.
In this file, you will define two variables: number1 and number2, with the values 10 and 5, respectively.
You do not need to write any functions or import any modules.
Calculate the sum, difference (by subtracting number2 from number1), and product of number1 and number2.
Print the results of each operation in the format: [operation] of [number1] and [number2] is [result].
Expected Output:

When executed, your script should print the following (assuming number1 = 10 and number2 = 5):

How to execute

python3 basic_operations.py
Here is the outcome

Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: basic_operations.py
 
1. Simple Interest Calculator
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Apply basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.

Task Description:

Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
Instructions:

Create a file named simple_interest.py.
Define three variables in this file:
principal with a value of 1000 (representing $1000),
rate with a value of 0.05 (representing 5% annual interest rate),
time with a value of 3 (representing 3 years).
Calculate the simple interest using the formula provided and store the result in a variable named interest.
Print the calculated interest in a format: The simple interest is: [interest].
Expected Output:

When executed, your script should print the simple interest calculated with the provided values. For principal = 1000, rate = 0.05, and time = 3, the output should be:

The simple interest is: 150.0
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: simple_interest.py"""
number1 = 10
number2 = 5

print("Addition of number1 and number2 is", (number1 + number2))
print("Subtraction of number1 and number2 is", (number1 - number2))
print("Multiplication of number1 and number2 is", (number1 * number2))
