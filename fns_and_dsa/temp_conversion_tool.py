FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp}°C")
    return temp
def convert_to_fahrenheit(celsius):
    temp = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {temp}°F")
    return temp

temp_info = int(input("Enter the temperature to convert: "))
temp_type = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

if temp_type == "C":
    convert_to_celsius(temp_info)
else:
    convert_to_fahrenheit(temp_info)
