import os, time
toDoList = []
if os.path.exists("to.do"):
  f = open("to.do", "r")
  toDoList = eval(f.read())
  f.close()
def wait(seconds):
  time.sleep(seconds)
  os.system("clear")
def printList():
  if len(toDoList) == 0:
    print("There are no items in your list")
  else:
    i = 1
    for items in toDoList:
      print(f"{i}. {items}")
      i += 1
def addItem():
  item = input("Enter Item> ").strip().title()
  if item in toDoList:
    print("Item already in list")
  else:
    toDoList.append(item)
    print("Item added Successfully")
def removeItem():
  if len(toDoList) == 0:
    print("There are no items in your list")
  else:
    printList()
    print()
    index = int(input("Enter Todos index: "))
    if index > len(toDoList):
      print("Invalid index")
    else:
      confirm = input("Are you sure you want to remove ToDo?(y/n) >")
      if confirm == "y":
        toDoList.remove(toDoList[index-1])
        print("Item removed Successfully")
      else:
        print("Item not removed")
def editItem():
  if len(toDoList) == 0:
    print("There are no items in your list")
  else:
    printList()
    print()
    index = int(input("Enter Todos index: "))
    if index > len(toDoList):
      print("Invalid index")
    else:
      newItem = input("Enter new Item: ").strip().title()
      toDoList[index-1] = newItem
      print("Item edited Successfully")

while True:
  title = "\033[34mTo Do List Manager\033[0m"
  print(f"{title: ^50}")
  print()
  menu = input("1. Add\n2. View\n3. Remove\n4. Edit\n5. Exit\n> ")
  wait(1)
  if menu == "1":
    addItem()
    wait(2)
  elif menu == "2":
    printList()
    wait(3)
  elif menu == "3":
    removeItem()
    wait(2)
  elif menu == "4":
    editItem()
    wait(2)
  elif menu == "5":
    break
  else:
    print("Invalid input")
    wait(2)
  
  f = open("to.do", "w")
  f.write(str(toDoList))
  f.close()
