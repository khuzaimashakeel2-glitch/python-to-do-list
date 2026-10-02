tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
        print("Task added!")
        
    elif choice == "2":
        print("My tasks:")
        # loop to print the list
        for x in tasks:
            print(x)
            
    elif choice == "3":
        print("Bye!")
        break
        
    else:
        print("Wrong choice")