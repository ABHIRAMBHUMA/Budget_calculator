def calculate_budget(income, expenses):
    total_expenses = sum(expenses)
    budget = income - total_expenses
    return budget

def main():
    print("Welcome to the Budget Calculator!")
    income = float(input("Enter your total income: $"))
    num_expenses = int(input("How many expenses do you have? "))
    
    expenses = []
    for i in range(num_expenses):
        expense = float(input(f"Enter expense {i+1}: $"))
        expenses.append(expense)
    
    remaining_budget = calculate_budget(income, expenses)
    
    print("\nBudget Summary:")
    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${sum(expenses)}")
    print(f"Remaining Budget: ${remaining_budget}")

if __name__ == "__main__":
    main()
