# Expense Tracker and Financial Health Checker

# Taking user inputs for name and profession
name = input("Enter your name: ")
profession = input("Enter your profession: ")
print(f"\nWelcome, {name}! Let's analyze your financial health as a {profession}.\n")

# Loop to ensure valid income and expenses input
while True:
    try:
        income = float(input("Enter your monthly income: "))
        expenses = float(input("Enter your monthly expenses: "))
        if income < 0 or expenses < 0:
            print("Income and expenses must be non-negative numbers. Try again.")
            continue
        savings = income - expenses  # Calculating savings
        savings_percentage = (savings / income) * 100 if income > 0 else 0  # Calculating savings percentage
        break
    except ValueError:
        print("Invalid input! Please enter numerical values only.")

# Displaying savings percentage and financial health insights
print(f"\nTotal Savings: {savings_percentage:.2f}%\n")
if savings_percentage >= 20:
    print(f"Great job, {name}! You have a strong savings habit.\n")
elif 10 <= savings_percentage < 20:
    print(f"Good, {name}, but you could save a bit more.\n")
else:
    print(f"Warning, {name}: Your savings are too low. Consider cutting expenses!\n")

# Loop to categorize and validate expenses
while True:
    try:
        essentials = float(input("How much do you spend on Essentials? "))
        wants = float(input("How much do you spend on Wants? "))
        savings_investments = float(input("How much do you save or invest? "))
        total = essentials + wants + savings_investments  # Checking if total matches income
        if total != income:
            print("Your expenses do not match your income. Please re-enter values correctly.")
            continue
        print("\nExpense Breakdown:")
        print(f"Essentials: {(essentials/income)*100:.2f}%")
        print(f"Wants: {(wants/income)*100:.2f}%")
        print(f"Savings/Investments: {(savings_investments/income)*100:.2f}%\n")
        break
    except ValueError:
        print("Invalid input! Please enter numerical values only.")

# Loop to validate and compare savings goal with actual savings
while True:
    try:
        goal = float(input("What is your savings goal (in %)? "))
        if goal < 0:
            print("Goal must be a non-negative number. Try again.")
            continue
        print(f"\nYour savings percentage is {savings_percentage:.2f}%.")
        if savings_percentage >= goal:
            print(f"Congratulations, {name}! You’ve achieved your savings goal.\n")
        else:
            print(f"Keep working on your savings, {name}. You're {goal - savings_percentage:.2f}% away from your goal.\n")
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Generating financial summary
summary = (f"Financial Health Summary for {name}:\n"
           f"Income: {income}\n"
           f"Expenses: {expenses}\n"
           f"Savings: {savings} ({savings_percentage:.2f}%)\n"
           f"Expense Breakdown:\n"
           f"Essentials: {(essentials/income)*100:.2f}%\n"
           f"Wants: {(wants/income)*100:.2f}%\n"
           f"Savings/Investments: {(savings_investments/income)*100:.2f}%\n"
           f"Savings Goal: {goal}%\n"
           f"Status: {goal - savings_percentage:.2f}% away from your goal.\n")

# Displaying the summary
print(summary)
