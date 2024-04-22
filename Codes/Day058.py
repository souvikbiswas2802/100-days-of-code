import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
      wait(1)
    elif guess < number:
      print("Too low")
      attempts+=1
      wait(1)
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      wait(2)
      return attempts

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  wait(0.5)
  if menu == "1":
    totalAttempts+= game()
  elif menu == "2":
    print(f"You've had {totalAttempts} attempts")
    wait(1)
  else:
    break
