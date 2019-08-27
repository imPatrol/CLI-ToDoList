import json
import os

open('todo.json', 'a').close()

def getTodoList():

    #Opening "todo.json" as "file"
    with open("todo.json", "r") as file:
        
        #Loading the file
        return json.load(file)
    
#Checking if the file is empty, and if it is empty then write "[]"
if os.stat("todo.json").st_size == 0:
    with open("todo.json", "w") as file:
        file.write("[]")
else:
    pass

#Updating the list (so it keeps printing the new tasks)
def updatelist(task, add=True):

    todoList = getTodoList()

    #task.capitalize capitalizes the first letter of the task entered
    if add:
        todoList.append(task.capitalize())


    else:
    #Must be here since we're starting to enumerate from 1 and computers start indexing from 0
        del todoList[task-1]

    with open("todo.json", "w") as file:
        json.dump(todoList, file)

# Main Function, where everything goes :D
def main():

    #Exit codes list
    exits = ["q", "exit", "done"]

    while True:
        #types "cls" into the command line, which clears all text on the screen. (So it looks cleaner)
        os.system("cls")
        todolist = getTodoList()

        #start=1 will start enumerating the list from 1
        for index, todo in enumerate(todolist, start=1):
            print("{}. {}".format(index, todo))

        cmds()
        
        #.strip() strips away whitespaces, .lower() makes it lowercase
        prompt = input("Menu> ").strip().lower()
        
        #If user input from prompt is in exits (List at the first line of this function) it will quit the program
        if prompt in exits:
            break
        
        #Checking if the prompt starts with add, if it does then it will add the task
        elif prompt.startswith("add "):
            task = prompt[4:].strip()
            updatelist(task)
            
        #Checking if the prompt starts with del, if it does then it will delete the task
        elif prompt.startswith("del "):
            index = int(prompt[3:])
            updatelist(index, False)
#Commands to print
def cmds():
    
    print("\nMenu: ")
    print("add <task>")
    print("del <ID (task number)>")
    print("exit (q, exit, done)")

# Calling the main function
main()
