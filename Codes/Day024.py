def rollDice(sides):
  import random
  roll = random.randint(1, sides)
  print("You rolled", roll)

print("Infinity Dice 🎲")
print()
sides = int(input("How many sides?: "))
while True:
  rollDice(sides)
  print()
  again = input("Roll again? ")
  if again == "No" or again == 'no':
    break
  
