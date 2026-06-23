import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount < 0:
                print("Amount cannot be negative! ")
                continue

            return amount
        
        except ValueError:
            print("please enter a valid number! ")    

def add_expense():
    expense_name = input("Enter Expense name: ")

    expense_amount = get_valid_amount()
    

    category = input("Enter category (Food/Transport/Bills/etc): ")         


    expense = {
        "name": expense_name,
        "amount": expense_amount,
        "category": category

    }

    return expense



def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpense List")
    print("-----------------------------------")
    print(f"{'Name':<15}{'Amount':<10}{'Category'}")
    print("-----------------------------------")

    for expense in expenses:
        print(f"{expense['name']:<15}{expense['amount']:<10}{expense['category']}")
    

def calculate_total(expenses):
    total =  0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total Expenses: {total}")              

def save_expenses(expenses):
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent = 4)
    except Exception as e:
        print("Error saving file:", e)

def find_expense(expenses, name):
    for expense in expenses:
        if expense["name"].lower() == name.lower():
            return expense

    return None          


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    name = input("Enter expense name to delete: ")
    
    expense = find_expense(expenses, name)
    
    if expense:
            expenses.remove(expense)
            save_expenses(expenses)

            print(f"Deleted: {expense['name']} - {expense['amount']}")
            
    else:
        print("Expense not found!")
            

    

def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit.")
        return

    view_expenses(expenses)

    name = input("Enter expense name to edit: ")
    
    expense = find_expense(expenses, name)

    if expense:
        
            new_amount = get_valid_amount()
            expense["amount"] = new_amount

            save_expenses(expenses)

            print(f"Updated: {expense['name']} - {expense['amount']}")
            return
        
    print("Expense not found!")

def search_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    name = input("Enter expense name to search: ")

    for expense in expenses:
        if expense["name"].lower() == name.lower():
            print(f"Found: {expense['name']} - {expense['amount']} - {expense.get('category','Uncategorized')}")
            return

    print("Expense not found!")

def category_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    totals = {}

    for expense in expenses:
        category = expense.get("category", "uncategorized")
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\nCategory Summary")
    print("-----------------------")
    print(f"{'category':<15}{'Total'}")
    print("-----------------------")

    for category, total in totals.items():
        print(f"{category:<15}{total}")

     






expenses = load_expenses()

while True:

    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Search Expense")
    print("7. Category summary")
    print("8. Exit")

    choice = (input("Enter your choice: "))

    if choice == "1":

        expense = add_expense()
        expenses.append(expense)

        save_expenses(expenses)

        print("Expense added successfully!")
        

    elif choice == "2":
        view_expenses(expenses)
        
    elif choice == "3":
        calculate_total(expenses)

    elif choice == "4":
        delete_expense(expenses)

    elif choice == "5":
        edit_expense(expenses)
        
    
    elif choice == "6":
        search_expense(expenses)

    elif choice =="7":
        category_summary(expenses)

    elif choice == "8":
        print("Exiting...........")
        break
    else:
        print("Invalid choice....")
