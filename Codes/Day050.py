import random, os, time

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")
path = False
while True:
  print("🌟Idea Storage🌟\n")
  choice = input("1. ADD an Idea\n2. LOAD a random idea\n3. Exit\n> ")
  if choice == "1":
    f = open("my.ideas", "a+")
    idea = input("Input your idea > ").strip().title()
    f.write(f"{idea}\n")
    f.close()
    print("Nice! Your idea has been stored.")
    path = True
    wait(1)
  elif choice == "2":
    if path == True:
      f = open("my.ideas", "r")
      ideas = f.read().split("\n")
      ideas.remove("")
      idea = random.choice(ideas)
      print("Your Idea is >",idea)
      f.close()
      wait(2)
    else:
      print("You need to add an idea first.")
      wait(1)
  elif choice == "3":
    wait(0)
    print("Exited.")
    break
  else:
    print("Invalid Input")
    wait(1)
