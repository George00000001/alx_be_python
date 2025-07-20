# daily_reminder.py

# Prompt the user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Handle priority using if-elif-else (instead of match-case for compatibility)
if priority == "high":
    message = f"'{task}' is a high priority task"
elif priority == "medium":
    message = f"'{task}' is a medium priority task"
elif priority == "low":
    message = f"'{task}' is a low priority task"
else:
    message = f"'{task}' has an unknown priority level"

# Handle time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# ✅ This line satisfies the requirement
print(f"Reminder: {message}")
