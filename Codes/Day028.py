import os, time
def rollDice(sides):
  import random
  roll = random.randint(1, sides)
  return roll

def health():
  return (rollDice(6)*rollDice(12)/2)+10

def strength():
  return (rollDice(6)*rollDice(12)/2)+12

while True:
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  name1 = input("Name your Legend: ")
  type1 = input("Character Type (Human, Elf, Wizard, Orc): ")
  print(name1)
  health1 = health()
  strength1 = strength()
  print("HEALTH:", health1)
  print("STRENGTH:", strength1)
  print()
  print("Who are they battling?")
  print()
  name2 = input("Name your Legend: ")
  type2 = input("Character Type (Human, Elf, Wizard, Orc): ")
  print(name2)
  health2 = health()
  strength2 = strength()
  print("HEALTH:", health2)
  print("STRENGTH:", strength2)
  round = 1
  while True:
    time.sleep(2)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    roll1 = rollDice(6)
    roll2 = rollDice(6)
    print("Round: ", round, "begins!")
    print()
    if roll1 > roll2:
      print(name1, "wins the first blow")
      damage = abs(strength1 - strength2)+1
      health2 -= damage
      print(name2, "takes a hit, with", damage, "damage")
      print(name1)
      print("HEALTH:", health1)
      print()
      print(name2)
      print("HEALTH:", health2)
      if health2 <= 0:
        print("Oh no", name2, "has died!")
        print(name1, "destroyed", name2, "in", round, "rounds!")
        exit()
    elif roll2 > roll1:
      print(name2, "wins the first blow")
      damage = abs(strength1 - strength2)+1
      health1 -= damage
      print(name1, "takes a hit, with", damage, "damage")
      print(name1)
      print("HEALTH:", health1)
      print()
      print(name2)
      print("HEALTH:", health2)
      if health1 <= 0:
        print("Oh no", name1, "has died!")
        print(name2, "destroyed", name1, "in", round, "rounds!")
        exit()
    else:
      print("It's a draw!")
    round += 1
