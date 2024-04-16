import time, os
def clear(seconds):
  time.sleep(seconds)
  os.system('clear')
pizza = []
def prettyPrint():
  for rows in pizza:
    for items in rows:
      print(f"{items:^15}", end=" | ")
    print()
  print()

while True:
  try:
    f = open("pizza.txt", "r")
    pizza = eval(f.read())
  except:
    print("ERROR: No existing pizza list, using a blank list")
    clear(2)
    
  print("Welcome to the Pizza Shop!")
  menu = input("1: Add Pizza\n2: View Pizzas\n3: Exit\n> ")
  print()
  if menu == "1":
    name = input("Name: ").strip().title()
    toppings = input("Toppings: ").strip().title()
    size = input("Size (s/m/l): ").lower()
    if size =="s":
      cost = 5
    elif size =="m":
      cost = 10
    elif size =="l":
      cost = 15
    
    try:
      quantity = int(input("Quantity: "))
    except:
      print("ERROR: Quantity must be a whole number")
      quantity = int(input("Quantity: "))
    total = cost * quantity
    temp = [name, toppings, size, quantity, total]
    pizza.append(temp)
    clear(1)
  elif menu == "2":
    print("\033[32m")
    print(f"{'Name':^15} | {'Toppings':^15} | {'Size':^15} | {'Quantity':^15} | {'Total':^15}\033[0m\n")
    prettyPrint()
    clear(3)
  elif menu == "3":
    break
  else:
    print("ERROR: Not a valid option")
  f = open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()
  clear(1)
