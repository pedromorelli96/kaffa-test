#####################################################
# Kaffa - Pre-qualification Test
# 5) Simple Todo List
# Name: Pedro Rodrigo Ramos Morelli
# E-mail: pedromorelli96@gmail.com
#####################################################

# json module used to store and read data from json file
import json
# os.path module used to check if json file already exists
import os.path

# Function check_file_exists is literal
# returns True if 'filename' in same directory of code exists
def check_file_exists(filename):
    return os.path.exists(filename)

# Function empty_list checks if list used to store data is empty
# returns True if 'todolist' is empty
def empty_list(todolist):
    return not todolist

# Function add_task asks user for task input on stdin
# then adds task string to 'todolist' and shows a
# completion message on stdout
def add_task(todolist):
    print("-"*5)
    print("Enter your task below:")
    task = input()
    todolist.append(task)
    print(f"Task #{len(todolist)} added!")

# Function remove_task asks user for task number on stdin
# then removes task based on position from 'todolist' and shows
# a completion message on stdout if successful, otherwise
# warns user about incorrect task number entered
def remove_task(todolist):
    print("-"*5)
    print("Which task (number) do you want to remove?")
    task = int(input())
    if (task <= len(todolist)):
        todolist.pop(task - 1)
        print("Task removed!")
    else:
        print(f"Task {task} does NOT exist!")

# Function remove_all_tasks removes all tasks from 'todolist'
# returns a successful message to user on stdout
def remove_all_tasks(todolist):
    print("-"*5)
    for i in range(len(todolist)):
        todolist.pop(i)
    print("All tasks deleted.")

# Function print_todolist shows all tasks (if any) on stdout
def print_todolist(todolist):
    print("####### TODO LIST #######")
    if (empty_list(todolist)):
        print("There are no tasks!")
        print("#"*25)
    else:
        i = 1
        for task in todolist:
            print(f"{i} - {task}")
            i += 1
        print("#"*25)

# Function task_request_msg prints on stdout the
# possible command inputs for todo list control
def task_request_msg():
    print("Enter:")
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Show Todo List")
    print("4 - Delete all Tasks")
    print("q - Quit Application")

# Function parse_input checks parameter 'keybinput'
# and picks the correct method acording to its code
# otherwise, warns user about incorrect input
def parse_input(keybinput, todolist):
    if (keybinput == '1'):
        add_task(todolist)
        print_todolist(todolist)
    elif (keybinput == '2'):
        remove_task(todolist)
        print_todolist(todolist)
    elif (keybinput == '3'):
        print_todolist(todolist)
    elif (keybinput == '4'):
        remove_all_tasks(todolist)
    elif (keybinput == 'q'):
        print("Exiting Todo List...")
    else:
        print("Invalid input, try again!")

# Function manage_todolist is the main function of the program
# First, it checks if the file we use already exists and reads
# from it if it does, otherwise we create an empty list
# Second, it shows all tasks (if any) in current todo list
# Third, reads from user input and calls correspondent methods
# to control the list and its tasks
# Finally, it saves on the 'filename' json file the list of tasks
# and closes the file
def manage_todolist():

    filename = 'todo.json'
    if (check_file_exists(filename)):
        f = open(filename)
        todolist = json.load(f)
    else:
        todolist = []

    # First message on execution   
    print_todolist(todolist)

    keybinput = 0
    while (keybinput != 'q'):
        task_request_msg()
        keybinput = input()
        parse_input(keybinput, todolist)

        if (keybinput == 'q'):
            with open(filename, 'w') as f:
                json.dump(todolist, f)
            f.close()

# Start point
manage_todolist()



    




