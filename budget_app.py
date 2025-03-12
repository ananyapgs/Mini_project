import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount:.2f}")

def get_total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return total

def get_balance(budget, expenses):
    return budget - get_total_expense(expenses)

def show_budget_details(budget, expenses):
    print(f"\nTotal Budget: {budget:.2f}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']:.2f}")
    print(f"Total Spent: {get_total_expense(expenses):.2f}")
    print(f"Remaining Budget: {get_balance(budget, expenses):.2f}\n")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to Budget Tracker App\n")
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)

    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(initial_budget, expenses)
        elif choice == "3":
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
