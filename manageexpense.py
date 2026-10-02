total = 0

while True:
    print("1. Add expense")
    print("2. Show total and quit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        # Convert the input to a float so we can do math with it
        amount = float(input("Enter expense amount: "))
        
        # adds the new amount to our running total
        total = total + amount
        print("Expense added!")
        
    elif choice == "2":
        print("---")
        print("Total Spent:", total)
        print("Goodbye!")
        break
        
    else:
        print("Wrong choice")