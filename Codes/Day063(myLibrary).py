import os, time, random

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

def textcolor(color, text):
  if color.lower() == "red":
    print(f"\033[31m{text}\033[0m", end ='')
  elif color.lower() == "green":
    print(f"\033[32m{text}\033[0m", end ='')
  elif color.lower() == "yellow":
    print(f"\033[33m{text}\033[0m", end ='')
  elif color.lower() == "blue":
    print(f"\033[34m{text}\033[0m", end ='')
  elif color.lower() == "purple":
    print(f"\033[35m{text}\033[0m", end ='')
  elif color.lower() == "cyan":
    print(f"\033[36m{text}\033[0m", end ='')
  elif color.lower() == "white":
    print(f"\033[37m{text}\033[0m", end ='')
  else:
    print(f"\033[0m{text}\033[0m", end ='')

def print_hearts(total_lives, remaining_lives):
  hearts = ""
  for i in range (remaining_lives):
    hearts = hearts + "❤️ "
  for i in range (total_lives - remaining_lives):
    hearts = hearts + "💔"
  print(hearts)

def rollDice():
  rolls = ""
  roll = random.randint(1, 6)
  rolls = f"{roll} "
  if roll == 6:
    rolls = rolls + rollDice()
  return rolls
