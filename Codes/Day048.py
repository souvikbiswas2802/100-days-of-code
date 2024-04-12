import os, time

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("ENTER INITIALS OF YOUR NAME > ").strip().upper()
  score = input("ENTER YOUR SCORE > ").strip()
  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()
  print("\nADDED")
  wait(1)
  exit = input("Press 1 to exit or anything else to continue > ")
  if exit == "1":
    break
  else:
    wait(0)
