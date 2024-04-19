import os, time, random
todoList = []

def clear(seconds):
  time.sleep(seconds)
  os.system("clear")

os.mkdir("Backups")

files = os.listdir()
if "to.do" in files:
  f = open("to.do", "r")
  todoList = eval(f.read())
  f.close()

def add():
  clear(0)
  print("ADD\n")
  thing = input("What task do you want to add? > ").strip().capitalize()
  due = input("When is it due? > ").strip().capitalize()
  priority = input("What is the priority?(High/Medium/Low) > ").strip().capitalize()
  if priority == "High" or priority == "Medium" or priority == "Low":
    tempList = [thing, due, priority]
    todoList.append(tempList)
    print("Thanks, this task has been added.")
    clear(1)
  else:
    print("prioirty must be High, Medium or Low")
    clear(1)  
def view():
  clear(0)
  print("VIEW\n")
  viewType = input("1: View all\n2: View by priority\n> ")
  if viewType == "1":
    for row in todoList:
      for item in row:
        print(f"{item:^10}", end=" | ")
      print()
    print()
  elif viewType == "2":
    priority = input("Enter Priority(High/Medium/Low) > ").strip().capitalize()
    if priority == "High" or priority == "Medium" or priority == "Low":
      for row in todoList:
        if priority in row:
          for item in row:
            print(f"{item:^10}", end=" | ")
          print()
          clear(3)
        else:
          print("No tasks with that priority.")
          clear(1)
    else:
      print("Priority is not valid.")
      clear(1)

def remove():
  clear(0)
  print("REMOVE\n")
  remove = input("What task do you want to remove? > ").strip().capitalize()
  for row in todoList:
    if remove in row:
      todoList.remove(row)
      print("Thanks, this task has been removed.")
    else:
      print("Sorry, this task is not in the list.")
  clear(1)

def edits():
  clear(0)
  print("EDIT\n")
  edit = input("Which task do you want to edit? > ").strip().capitalize()
  for row in todoList:
    if edit in row:
      row[0] = input("Add New task > ").strip().capitalize()
      row[1] = input("Add New Due Date > ").strip().capitalize()
      row[2] = input("Add New Priority (High/Medium/Low) > ").strip().capitalize()
      print("Thanks, this task has been edited.")
    else:
      print("Sorry, this task is not in the list.")
  clear(1)

while True:
  print("TODO LIST MANAGER\n")
  menu = input("1: Add\n2: View\n3: Remove\n4: Edit\n> ").strip()
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    remove()
  elif menu == "4":
    edits()
  else:
    print("Sorry, this is not a valid option.")
  clear(1)

  backupfile = os.path.join("Backups/",f"backup{random.randint(1, 99999999999)}.txt")
  if "to.do" not in files:
    f = open(backupfile, "w")
    f.write(str(todoList))
    f.close()
  
  f = open("to.do", "w")
  f.write(str(todoList))
  f.close()
  
