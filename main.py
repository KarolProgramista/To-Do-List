from termcolor import colored
import list as lst
import os
import pickle
import sys


# Declare a clear function
def clear(): return os.system("cls")


savePath = 'save.dat'


picture = """
    ___    ___
    (0)    (0)
        <
      _____

"""


# Drawing firsts part of the application
def drawStartScreen():
    print(colored("To ", 'red'), colored("Do ", 'green'), colored("List", 'blue'))
    print(colored(picture, 'yellow'))
    print(colored("Your To Do List:", 'blue'))
    drawToDoList()


# Drawing To Do List
def drawToDoList():
    if(len(lst.ToDoList) <= 0):
        print("No things to do")
        GetCommand()
    for a in lst.ToDoList:
        print(a)

    GetCommand()


# Getting the Command from the user
def GetCommand():
    comand = input(">>>")
    words = comand.split(" ", 1)
    if(words[0] == 'Add' or words[0] == 'add'):
        AddToDo(words[1])
    elif(words[0] == 'Exit' or words[0] == 'exit'):
        Exit()
    elif(words[0] == 'delete' or words[0] == "Delete"):
        Del(words[1])
    elif(words[0] == 'clear' or 'Clear'):
        ClearList()


# Adding new element
def AddToDo(ToDo):
    lst.ToDoList.append(ToDo)
    clear()
    drawStartScreen()


# Exit from application
def Exit():
    Save()
    sys.exit


# Deleting element form the list
def Del(ToDo):
    lst.ToDoList.remove(ToDo)
    clear()
    drawStartScreen()


# Clearing list
def ClearList():
    lst.ToDoList.clear()
    clear()
    drawStartScreen()


# Saveing To Do List to the file with pickle
def Save():
    saveFile = open(savePath, 'wb')
    pickle.dump(lst.ToDoList, saveFile)
    saveFile.close()


# Load data
try:
    loadFile = open(savePath, 'rb')
    loadData = pickle.load(loadFile)
    lst.ToDoList = loadData
    loadFile.close()
except:
    print('No load file')

# Clear window on Start
clear()
# Star app
drawStartScreen()
