def add_expense(expenses):
    date = input("Enter date (YYY-MM-DD): ")
    paymentMethod = input("Enter payment method (credit/cash): ")
    category = input("Enter expense category (ex: housing, food, nonessential, etc.): ")
    amount = float(input("Enter the amount: "))
    expense = {"date": date, "paymentMethod": paymentMethod, "category": category, "amount": amount}
    expenses.append(expense)  #appends expense list by adding above input to end of expense[] array
    print("Expense added successfully!")