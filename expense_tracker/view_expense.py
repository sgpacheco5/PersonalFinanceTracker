def view_expenses(expenses):
    if not expenses: #if expenses is empty
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}") #.2f specifies amount to print up to 2 decimals
