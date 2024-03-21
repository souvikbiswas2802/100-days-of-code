print("⚔️CHARECTER STAT GENERATOR⚔️")
print()
import random
def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

while True:
  charecter = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("\033[92m","His health is", health,"hp","\033[0m")
  print()
  confirm = input("Do you want to create another charecter?(Y/N):  ")
  if confirm == "n" or confirm == "N":
    break
