"""3. Temperature Conversion Tool
mandatory
Score: 100.0% (Checks completed: 100.0%)
Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

Task Description:
Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

Requirements:
Define Global Conversion Factors:

At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
Implement Conversion Functions:

Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
Inside each function, use the respective global conversion factor to perform the conversion.
User Interaction:

Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
Based on the user’s input, call the appropriate conversion function and display the converted temperature.
If gthe user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
Guidance:
Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
Use input validation to ensure that the user enters a valid temperature and unit.
Example Output (Hypothetical):
Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
Or:

Enter the temperature to convert: 0
Is this temperature in Celsius or Fahrenheit? (C/F): C
0.0°C is 32.0°F
Repo:

GitHub repository: alx_be_python
Directory: fns_and_dsa
File: temp_conversion_tool.py"""
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp:.1f}°C")
    return temp
def convert_to_fahrenheit(celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {temp:.1f}°F")
    return temp

temp_info = float(input("Enter the temperature to convert: "))
temp_type = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

if temp_type == "C":
    convert_to_fahrenheit(temp_info)
elif temp_type == "F":
    convert_to_celsius(temp_info)
else:
    print("Invalid temperature. Please enter a numeric value.")
