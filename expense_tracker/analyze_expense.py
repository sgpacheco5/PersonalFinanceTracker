#calculates total spent in a specific category
def calculate_total_by_category(expenses):
    category = input("Enter the category to calculate total: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'] == category)
    print(f"Total expenses for {category}: ${total:.2f}")

#calculates average daily spending and overall spending
def calculate_statistics(expenses):
    total = sum(exp['amount'] for exp in expenses)
    days = len(set(exp['date'] for exp in expenses))
    avg_daily = total / days if days > 0 else 0
    print(f"Total Spending: ${total:.2f}")
    print(f"Average Daily Spending: ${avg_daily:.2f}")
