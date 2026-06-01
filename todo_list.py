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

# ==========================================
# Project: To-Do List Application
# Developed by: Tazmeen Iram
# Internship Project - DecodeLabs
# ==========================================



my_tasks = []
 """
    Function to add tasks to the task list.

    The user can continuously enter tasks.
    Typing 'done' stops task entry and returns to the main menu.
    Empty inputs are not allowed.
    """
def add_task():
    while True:
        # Take task input from the user
        task = input("enter task (or 'done' to stop): ")
        
  	# Stop adding tasks when user enters 'done'

        if task == "done":
            break

	# Check if the input is empty or contains only spaces
        if task.strip() == "":
            print("please enter a valid task!")
            continue

	# Add the task to the list
        my_tasks.append(task)
        print("Task added!")
def view_tasks():
     """
    Function to display all saved tasks.

    Shows a numbered list of tasks.
    Displays a message if no tasks have been added.
    """    

    if len(my_tasks) == 0:
        print("no tasks added yet!")
    else:
        print("\nyour tasks:")
	# Display tasks with numbering starting from 1
        for number, task in enumerate(my_tasks, start=1):
            print(f"{number}. {task}")

def main():
	"""
    Main function that controls the menu-driven interface.

    Allows the user to:
    1. Add tasks
    2. View tasks
    3. Exit the application
    """

    # Blank lines for cleaner output appearance
    print("")
    print("")
    print("")

    while True:
	 # Display menu options

        print("\nwhat do you want to do?")
        print("1.Add tasks")
        print("2.view tasks")
        print("3.Exit")

	# Take user choice
        choice = input("\nEnter choice(1/2/3):")
	
	# Call add_task function
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()

	# Exit the application
        elif choice == "3":
            print(f"\nYou completed today with {len(my_tasks)} tasks!")
            print("Goodbye!")
            break

	# Handle invalid menu choices
        else:
            print("invalid choice! Enter 1, 2 or 3")

	# Program execution starts here
if __name__ == "__main__":
    main()
        

