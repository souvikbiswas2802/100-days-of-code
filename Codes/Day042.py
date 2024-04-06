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

mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}
print("MokéBeast - The Non-Copyright Generic Beast Battle Game")
print()
mokedex["Beast Name"] = input("Input your beast's name > ").strip().title()
mokedex["Type"] = input("Input your beast's type > ").strip().title()
mokedex["Special Move"] = input("Input your beast's special move > ").strip().title()
mokedex["HP"] = input("Input your beast's starting HP > ").strip().title()
mokedex["MP"] = input("Input your beast's starting MP > ").strip().title()
print(textcolor(mokedex["Type"]))
print()
for name, value in mokedex.items():
  print(f"{name:<15}: {value}")

