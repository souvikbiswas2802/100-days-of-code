import os, time
def wait(seconds):
  time.sleep(seconds)
  os.system("clear")
def printList():
  print("The List is:")
  index = 1
  for name in myList:
    print(f"{index}. {name}")
    index += 1
def addName():
  name = f"{firstName} {lastName}"
  if name not in myList:
    myList.append(name)
  else:
    print("ERROR: Duplicate name")
    wait(1)
myList = []
while True:
  title = "Name List Generator"
  print(f"{title: ^50}")
  print()
  firstName = input("Enter Your First Name: ").strip().title()
  lastName = input("Enter Your Last Name: ").strip().title()
  wait(0)
  addName()
  printList()
  wait(3)
  confirm = input("Want to add another name? (y/n): ").strip().lower()
  if confirm == "y":
    wait(0)
    continue
  elif confirm == "n":
    break
  else:
    print("ERROR: Invalid Input")
    break


