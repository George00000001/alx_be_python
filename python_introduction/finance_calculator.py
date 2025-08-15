"""3. Convert Hours to Seconds
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Demonstrate understanding of variable assignments and arithmetic operations by converting a given number of hours into seconds.

Task Description:

For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.

Instructions:

Create a file named hours_to_seconds.py.
Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
Store the result of the conversion in a variable named seconds.
Print the result in the format: [hours] hour(s) is [seconds] seconds.
Expected Output:

Given the value hours = 2, your script should output:

2 hour(s) is 7200 seconds.
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: hours_to_seconds.py
 
4. User Input Age Calculator
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.

Task Description:

Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

Instructions:

Create a file named future_age_calculator.py.
Prompt the user to input their current age with the question: “How old are you? ”.
Assume the user will input a valid integer value.
Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
Expected Script Flow:

The script prompts the user for their current age.
The user enters their age.
The script calculates and prints how old the user will be in 2050.
Example Interaction:

If the user inputs 30 when prompted for their current age, the output should be:

In 2050, you will be 57 years old.
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: future_age_calculator.py
 
5. Personal Finance Calculator
#advanced
Score: 100.0% (Checks completed: 100.0%)
Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

Task Description:

You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

Instructions:

User Input for Financial Details:

Prompt the user for their monthly income: “Enter your monthly income: ”.
Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
Calculate Monthly Savings:

Calculate the monthly savings by subtracting monthly expenses from the monthly income.
Project Annual Savings:

Assume a simple annual interest rate of 5%.
Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
Output Results:

Display the user’s monthly savings.
Display the projected annual savings after including interest.
Example Interaction:

Enter your monthly income: 5000
Enter your total monthly expenses: 4000
Your monthly savings are $1000.
Projected savings after one year, with interest, is: $12600.
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: finance_calculator.py"""
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your totaly monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
annual_rate = 0.05 
print("Your monthly savings are", "${}".format(monthly_savings))
print("Projected Savings after one year, with interest, is:", "${}".format(monthly_savings * 12 + (monthly_savings * 12 * 0.05)))
