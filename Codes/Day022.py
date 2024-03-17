import random

print("Totally Random One-Million-to-One")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high")
print()
number = random.randint(1, 1000000)
attempt = 1
while True:
  guess = int(input("Pick a number between 1 and 1,000,000: "))
  if guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if guess < number:
    print("That number is too low. Try again!")
    attempt += 1
  elif guess > number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif guess == number:
    print("You are a winner! 🥳🥳")
    print("It took you", attempt, "attempt(s) to get the correct answer.")
    print()
    print("Click on 'Run' to try again with a different number")
    break
  else:
    print("That is not a number I recognize.")
    exit()
