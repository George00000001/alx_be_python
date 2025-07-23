Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low) ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high":
        if time_bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires attention this week!")
        else:
            print(f"{Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "no":
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print("invalid input")