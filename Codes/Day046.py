import os, time
mokedex = {}

def textcolor(type):
  if type == "Fire":
    return "\033[31m"
  elif type == "Grass":
    return "\033[32m"
  elif type == "Electric":
    return "\033[33m"
  elif type == "Water":
    return "\033[34m"
  elif type == "Ghost":
    return "\033[35m"
  elif type == "Flying":
    return "\033[36m"
  elif type == "Fairy":
    return "\033[37m"
  else:
    return "\033[0m"

def prettyprint():
  print(f"""{"Name":^12}|{"Type":^12}|{"HP":^12}|{"MP":^12}""")
  for key, value in mokedex.items():
    print(textcolor(value["Type"]))
    print(f"""{key:^12}|{value["Type"]:^12}|{value["HP"]:^12}|{value["MP"]:^12}""")
  
while True:
  print("MokéBeast - The Non-Copyright Generic Beast Battle Game")
  print()
  name = input("Input your beast's name > ").strip().title()
  type = input("Input your beast's type > ").strip().title()
  hp = input("Input your beast's starting HP > ")
  mp = input("Input your beast's starting MP > ")
  mokedex[name] = {"Type": type, "HP": hp, "MP": mp}
  print("-----------------------------------")
  print()
  prettyprint()
  print("\033[0m")
  
  exit = input("Press 'Y' to exit or any other key to continue: ")
  if exit.strip().lower() == "y":
    break
  else:
    time.sleep(1)
    os.system("clear")
  
