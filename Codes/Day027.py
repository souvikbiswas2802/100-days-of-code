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
  print("⚔️ CHARACTER BUILDER ⚔️")
  time.sleep(2)
  os.system("clear")
  name = input("Name your Legend: ")
  time.sleep(1)
  os.system("clear")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  time.sleep(1)
  os.system("clear")
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend...")
  print()
  again = input("Wanna build again?(Y/N): ")
  if again == "n" or again == "N":
    exit()
  else:
    continue
