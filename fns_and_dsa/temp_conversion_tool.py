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
    print("Invalid temperature type. Please enter C or F.")
