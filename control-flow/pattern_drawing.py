# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern:"))

# Validate that the input is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        # Print a row of asterisks using a for loop
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line
        row += 1
