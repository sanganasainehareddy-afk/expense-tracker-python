expenses=[]
def load_expenses():
    try:
        with open("expenses.txt","r") as file:
            for line in file:
                name,amount=line.strip().split(",")
                expenses.append((name,float(amount)))
    except FileNotFoundError:
        pass
def save_expense(name,amount):
    with open("expense.txt","a") as file:
        file.write(f"{name},{amount},{category}\n")
load_expenses()
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    choice=input("Enter choice: ")
    if choice == "1":
        name=input("Enter expense name: ")
        amount=float(input("Enter amount: "))
        category=input("Enter category: ")
        expenses.append((name, amount,category))
        save_expense(name,amount,category)
    elif choice == "2":
        total=0
        for item in expenses:
            print(item[0],"-",item[1],"-",item[2])
            total +=item[1]
        print("Total:", total)
    elif choice =="3":
        break
    else:
        print("Invalid choice")
