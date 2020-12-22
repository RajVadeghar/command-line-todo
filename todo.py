import sys, os
from os import path
from datetime import datetime

todoCount = 1
todosDoneCount = 1

if path.exists("done.txt"):
    with open("done.txt", "r") as todos:
        for todo in todos:
            todosDoneCount += 1
        todos.close()
else:
    with open("done.txt", "w") as todos:
        todos.close()

if path.exists("todo.txt"):
    with open("todo.txt", "r") as todos:
        for todo in todos:
            todoCount += 1
        todos.close()
else:
    with open("todo.txt", "w") as todos:
        todos.close()

def main():
    if not len(sys.argv) == 1:
        choice = sys.argv[1]
    if len(sys.argv) == 1 or choice == "help":
        todoHelp()
    elif choice == "add":
        try:
            todoAdd(sys.argv[2])
        except IndexError:
            print(
                '''Enter correct command: 
$ ./todo add 'todo item'  # Add a new todo'''
            )
    elif choice == "ls":
        todoList()
    elif choice == "del":
        try:
            todoDelete(sys.argv[2])
        except IndexError:
            print('''Enter correct command: 
$ ./todo del NUMBER       # Delete a todo''')
    elif choice == "done":
        try:
            todoDone(sys.argv[2])
        except IndexError:
            print('''Enter correct command: 
$ ./todo done NUMBER      # Complete a todo''')
    elif choice == "report":
        todoReport()

def todoHelp():
    print(
        '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''
    )

def todoAdd(todoItem):
    with open("todo.txt", "r+") as todos:
        totalTodos = todos.readlines()
        todos.seek(0)
        todos.write(f"[{todoCount}] {todoItem}\n")
        for todo in totalTodos:
            todos.write(todo)
        todos.truncate()
        print(f"Added todo: \"{todoItem}\"")
        todos.close()

def todoList():
    with open("todo.txt", "r") as todoFile:
        if todoCount == 1:
            print("Empty... ADD one using $ ./todo add 'todo item'  # Add a new todo")
        print(todoFile.read().rstrip("\n"))
        todoFile.close()

def todoDelete(todoItemIndex):
    if int(todoItemIndex) < todoCount and int(todoItemIndex) > 0:
        with open("todo.txt", "r+") as todoFile:
            lines = todoFile.readlines()
            todoFile.seek(0)
            count = todoCount
            for line in lines:
                if line[1] != f"{todoItemIndex}":
                    line = f"[{count - 2}]{line[3:]}"
                    count -= 1
                    todoFile.write(line)
            todoFile.truncate()
            todoFile.close()
            print(f"Deleted todo #{todoItemIndex}")
    else:
        print(f"Error: todo #{todoItemIndex} does not exist. Nothing deleted.")   

def todoDone(todoItemIndex):
    if int(todoItemIndex) < todoCount and int(todoItemIndex) > 0:
        with open("todo.txt", "r+") as todoFile:
            lines = todoFile.readlines()
            todoFile.seek(0)
            count = todoCount
            for line in lines:
                if line[1] == f"{todoItemIndex}":
                    with open("done.txt", "a+") as todosDone:
                        todosDone.write(f"x {datetime.today().strftime('%Y-%m-%d')}{line[3:]}")
                        todosDone.close()
                else:
                    line = f"[{count - 2}]{line[3:]}" 
                    count -= 1
                    todoFile.write(line)
            todoFile.truncate()
            todoFile.close()
            print(f"Marked todo #{todoItemIndex} as done")
    else:
        print(f"Error: todo #{todoItemIndex} does not exist.")

def todoReport():
    print(f"{datetime.today().strftime('%Y-%m-%d')} Pending:{todoCount - 1} Completed:{todosDoneCount - 1}")

main()