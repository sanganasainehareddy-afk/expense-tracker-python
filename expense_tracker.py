expenses=[]
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    choice=input("Enter choice: ")
    if choice == "1":
        name=input("Enter expense name: ")
        amount=float(input("Enter amount: "))
        expenses.append((name, amount))
        print("Expense added!")
    elif choice == "2":
        total=0
        for item in expenses:
            print(item[0],"-",item[1])
            total +=item[11]
        print("Total:", total)
    elif choice =="3":
        break
    else:
        print("Invalid choice")