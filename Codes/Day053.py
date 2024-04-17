import os, time
inventory = []
def clear(seconds):
  time.sleep(seconds)
  os.system("clear")

def additem():
  item = input("What item would you like to add to your inventory?\n>  ").capitalize()
  inventory.append(item)
  print(f"{item} has been added to your inventory")
  clear(2)

def viewitem():
  items = {}
  for item in inventory:
    if item in items:
      items[item] += 1
    else:
      items[item] = 1
  
  print(f"\033[36m{'Item':^15} : {'Quantity':^15}\033[0m")
  for item, count in items.items():
    print(f"{item:^15} : {count:^15}")
  clear(2)

def removeitem():
  item = input("What item would you like to remove from your inventory?\n> ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed from your inventory")
  else:
    print(f"{item} is not in your inventory")
  clear(1)

while True:
  try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
  except:
    print("Can't find file, creating new file")
    clear(1)
    
  print("RPG Inventory")
  menu = input("1: Add\n2: View\n3: Remove\n4: Exit\n> ")
  clear(0)
  if menu == "1":
    additem()
  elif menu == "2":
    viewitem()
  elif menu == "3":
    removeitem()
  elif menu == "4":
    break
  else:
    print("Invalid input")
    clear(1)

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
