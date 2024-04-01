import os, time

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

while True:
  title = "🌟Star Wars Name Generator🌟"
  print(f"{title: ^50}")
  print()
  name = input("Enter Your First Name, Last Name, Mom's Maiden Name, and the City You Were Born In(Space Seperated): ").lower().strip().split()
  wait(0)
  print(f"Your Star Wars Name is {name[0][0:3].capitalize()}{name[1][0:3]} {name[2][0:2].capitalize()}{name[3][-3:]}")
  wait(3)
  confirm = input("Would you like to generate another name? (y/n) ").lower()
  if confirm == "y":
    wait(0)
    continue
  elif confirm == "n":
    break
  else: 
    print("Invalid Input")


