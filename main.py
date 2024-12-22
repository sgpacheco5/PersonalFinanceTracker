
from expense_tracker.add_expense import add_expense
from expense_tracker.view_expense import view_expenses
from expense_tracker.analyze_expense import calculate_total_by_category, calculate_statistics
from expense_tracker.data_manager import save_expenses_to_file, load_expenses_from_file

def main():
    filename = "expenses.json"
    expenses = load_expenses_from_file(filename)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total by Category")
        print("4. View Statistics")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total_by_category(expenses)
        elif choice == '4':
            calculate_statistics(expenses)
        elif choice == '5':
            save_expenses_to_file(expenses, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
