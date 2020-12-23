import sys, os
from os import path
from datetime import datetime

todosCount = 1 # counts no.of todos of todo.txt file
todosDoneCount = 1 # counts no.of todos of done.txt file

# Checking if todo.txt exists.
if path.exists("todo.txt"):
    with open("todo.txt", "r") as todos:
        for todo in todos:
            todosCount += 1
        todos.close()
# If not exsits below code creates one for us
else:
    with open("todo.txt", "w") as todos:
        todos.close()

# Checking if done.txt exists.
if path.exists("done.txt"):
    with open("done.txt", "r") as todos:
        for todo in todos:
            todosDoneCount += 1
        todos.close()
# If not exsits below code creates one for us
else:
    with open("done.txt", "w") as todos:
        todos.close()

# Driver code
def main():
    if not len(sys.argv) == 1:
        choice = sys.argv[1] # This variable helps us in switching diff tasks

    if len(sys.argv) == 1 or choice == "help":
        todoHelp()

    elif choice == "add":
        try:
            todoAdd(sys.argv[2])
        except IndexError:
            print("Error: Missing todo string. Nothing added!")

    elif choice == "ls":
        todoList()

    elif choice == "del":
        try:
            todoDelete(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for deleting todo.")

    elif choice == "done":
        try:
            todoDone(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for marking todo as done.")

    elif choice == "report":
        todoReport()

# This funcion helps user to reach out to functionalities of this app
def todoHelp():
    # Print statement isn't working in windows to pass test cases
    sys.stdout.buffer.write('''Usage :-
$ ./todo add \"todo item\"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''.encode('utf8'))

# function to know if there's substring in file
def isStringInFile(fileName, stringToSearch):
    with open(fileName, 'r') as readObj:
        for line in readObj:
            if stringToSearch in line:
                return True
    return False

# function to add todo item onto todo.txt file
def todoAdd(todoItem):
    with open("todo.txt", "a") as todos:
        if not isStringInFile("todo.txt", f"{todoItem}"):
            todos.writelines(f"{todoItem}\n")
        print(f"Added todo: \"{todoItem}\"")
        todos.close()

#function to list todo items
def todoList():
    with open("todo.txt", "r") as todoFile:
        if todosCount == 1:
            print("There are no pending todos!")
        lines = todoFile.readlines()
        count = todosCount
        for line in reversed(lines):
            sys.stdout.buffer.write(f"[{count -1}] {line}".encode('utf8'))
            # print(f"[{count -1}] {line}".rstrip("\n"))
            count -= 1
        
        todoFile.close()

# function to delete todo item using index
def todoDelete(todoItemIndex):
    if int(todoItemIndex) < todosCount and int(todoItemIndex) > 0:
        with open("todo.txt", "r+") as todoFile:
            lines = todoFile.readlines()
            del lines[int(todoItemIndex) - 1]
            todoFile.seek(0)
            for line in lines:
                todoFile.write(line)
            todoFile.truncate()
            todoFile.close()
            print(f"Deleted todo #{todoItemIndex}")
    else:
        print(f"Error: todo #{todoItemIndex} does not exist. Nothing deleted.")

# function to mark an item as done and push that todo item to done.txt file
def todoDone(todoItemIndex):
    if int(todoItemIndex) < todosCount and int(todoItemIndex) > 0:
        with open("todo.txt", "r+") as todoFile:
            lines = todoFile.readlines()
            with open("done.txt", "a+") as todosDone:
                todosDone.write(
                    f"x {datetime.today().strftime('%Y-%m-%d')}"
                    f"{lines[int(todoItemIndex) - 1]}"
                )
                todosDone.close()
            del lines[int(todoItemIndex) - 1]
            todoFile.seek(0)
            for line in lines:
                todoFile.write(line)
            todoFile.truncate()
            todoFile.close()
            print(f"Marked todo #{todoItemIndex} as done.")
    else:
        print(f"Error: todo #{todoItemIndex} does not exist.")

# function to print count of completed and pending todos
def todoReport():
    print(
        f"{datetime.today().strftime('%Y-%m-%d')}"
        f" Pending : {todosCount - 1}"
        f" Completed : {todosDoneCount - 1}"
    )

main() # Calling diver code