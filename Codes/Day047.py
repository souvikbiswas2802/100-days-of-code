import os, time, random
trumps = {}
trumps["David"] = {"Intelligence": 98, "Speed": 40, "Guile": 70, "Baldness Level": 100}
trumps["Mr Spock"] = {"Intelligence": 20, "Speed": 50, "Guile": 50, "Baldness Level": 1}
trumps["Moica from Friends"] = {"Intelligence": 50, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 20, "Speed": 1, "Guile": 10, "Baldness Level": 20}

def clear(seconds):
  time.sleep(seconds)
  os.system("clear")

def cardinput():
  clear(0)
  name = input("Name: ")
  intelligence = int(input("Intelligence: "))
  speed = int(input("Speed: "))
  guile = int(input("Guile: "))
  baldness = int(input("Baldness Level: "))
  trumps[name] = {"Intelligence": intelligence, "Speed": speed, "Guile": guile, "Baldness Level": baldness}
  clear(1)

def chooseStat():
  clear(1)
  print("Choose your stat: \n1. Intelligence\n2. Speed\n3. Guile\n4. Baldness Level")
  answer = input("> ")
  if answer == "1":
    return "Intelligence"
  elif answer == "2":
    return "Speed"
  elif answer == "3":
    return "Guile"
  elif answer == "4":
    return "Baldness Level"
  else:
    print("Invalid input. Please try again.")
    chooseStat()

def printTrumps():
  clear(0)
  print("Choose your character:")
  for key in trumps:
    print(key)
  print()

def game(p1, p2, stat):
  clear(0)
  print(f"{p1}: {trumps[p1][stat]}")
  print(f"{p2}: {trumps[p2][stat]}")
  print()
  if trumps[p1][stat] > trumps[p2][stat]:
    print(p1, "wins")
  elif trumps[p1][stat] < trumps[p2][stat]:
    print(p2, "wins")
  else:
    print("Draw")
  clear(3)

while True:
  print("TOP TRUMPS")
  print()
  menu = input("1. Add a character\n2. Play 1 Player\n3. Play 2 Player\n4. Exit\n> ")
  if menu == "1":
    cardinput()
  elif menu == "2":
    printTrumps()
    player1 = input("> ")
    comp = random.choice(list(trumps.keys()))
    print("Computer has picked", comp)
    stat = chooseStat()
    game(player1, comp, stat)
  elif menu == "3":
    printTrumps()
    player1 = input("Player 1 >  ")
    player2 = input("Player 2 >  ")
    stat = chooseStat()
    game(player1, player2, stat)
  elif menu == "4":
    break
  else:
    print("Invalid Input")
    clear(1)
