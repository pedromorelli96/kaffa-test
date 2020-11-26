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

def check_file_exists(filename):
    return os.path.exists(filename)

def empty_list(todolist):
    return not todolist

def add_task(todolist):
    print("-"*5)
    print("Enter your task below:")
    task = input()
    todolist.append(task)
    print(f"Task #{len(todolist)} added!")

def remove_task(todolist):
    print("-"*5)
    print("Which task (number) do you want to remove?")
    task = int(input())
    if (task <= len(todolist)):
        todolist.pop(task - 1)
        print("Task removed!")
    else:
        print(f"Task {task} does NOT exist!")

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

def task_request_msg():
    print("Enter:")
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Show Todo List")
    print("q - Quit Application")

def parse_input(keybinput, todolist):
    if (keybinput == '1'):
        add_task(todolist)
        print_todolist(todolist)
    elif (keybinput == '2'):
        remove_task(todolist)
        print_todolist(todolist)
    elif (keybinput == '3'):
        print_todolist(todolist)
    elif (keybinput == 'q'):
        print("Exiting Todo List...")
    else:
        print("Invalid input, try again!")

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



    




