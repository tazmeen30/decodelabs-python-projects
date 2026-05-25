#my_tasks = []
#my_tasks.append("Finish Python Assignment")
#my_tasks.append("Buy Milk")
#my_tasks.append("Walk Dog")
#my_tasks.append("Code Project")
#print(my_tasks)

#basic loop
#for task in my_tasks:
    #print(task)


# Professional Loop
#for number, task in enumerate(my_tasks , start=1)
    #print(number, task)

my_tasks = []
def add_task():
    while True:
        task = input("enter task (or 'done' to stop): ")
        if task == "done":
            break
        if task.strip() == "":
            print("please enter a valid task!")
            continue
        my_tasks.append(task)
        print("Task added!")
def view_tasks():
    if len(my_tasks) == 0:
        print("no tasks added yet!")
    else:
        print("\nyour tasks:")
        for number, task in enumerate(my_tasks, start=1):
            print(f"{number}. {task}")

def main():
    print("")
    print("")
    print("")
    while True:
        print("\nwhat do you want to do?")
        print("1.Add tasks")
        print("2.view tasks")
        print("3.Exit")
        choice = input("\nEnter choice(1/2/3):")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print(f"\nYou completed today with {len(my_tasks)} tasks!")
            print("Goodbye!")
            break
        else:
            print("invalid choice! Enter 1, 2 or 3")
if __name__ == "__main__":
    main()
        

