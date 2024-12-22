def save_expenses_to_file(expenses, filename):
    import json
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print(f"Expenses saved to {filename}.")

def load_expenses_from_file(filename):
    import json
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
        print(f"Expenses loaded from {filename}.")
        return expenses
    except FileNotFoundError:
        print(f"No file found with name {filename}. Starting fresh.")
        return []
