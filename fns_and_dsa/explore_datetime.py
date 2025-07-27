from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date
    print(f"Current date and time: {formatted}")

user_input = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=days)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")


display_current_datetime()
calculate_future_date(user_input)