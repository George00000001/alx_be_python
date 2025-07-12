monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your totaly monthly expenses"))
monthly_savings = monthly_income - monthly_expenses
annual_rate = 0.05 
print("Your monthly savings are", "${}".format(monthly_savings))
print("Projected Savings after one year, with interest, is:", "${}".format(monthly_savings * 12 + (monthly_savings * 12 * 0.05)))
