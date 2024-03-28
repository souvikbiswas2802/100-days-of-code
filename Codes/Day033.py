import os, time
toDoList = []

def clear():
  os.system("clear")
def wait(seconds):
  time.sleep(seconds)
def printList():
  i = 1
  for items in toDoList:
    print(f"{i}. {items}")
    i += 1
def addItem():
  item = input("Enter Item> ")
  toDoList.append(item)
  print("Item added Succefully")
def removeItem():
  printList()
  print()
  index = int(input("Enter Todos index: "))
  if index > len(toDoList):
    print("Invalid index")
  else:
    toDoList.remove(toDoList[index-1])
    print("Item removed Succefully")

while True:
  title = "\033[34mTo Do List Manager\033[0m"
  print(f"{title: ^50}")
  print()
  menu = input("Do you want to view, add, or edit your to do list?\n>")
  print()
  if menu == "view":
    printList()
    wait(3)
    clear()
  elif menu == "add":
    addItem()
    wait(2)
    clear()
  elif menu == "edit":
    removeItem()
    wait(2)
    clear()
  else:
    print("Invalid input")
    wait(2)
    clear()
