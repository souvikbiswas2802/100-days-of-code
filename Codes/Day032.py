import random
def index():
  return random.randint(0, 5)

greetings = [
  "Hello",
  "Bonjour",
  "Hola",
  "Zdravstvuyte",
  "Nǐn hǎo",
  "Konichiwa"
]

print(f"{greetings[index()]}")
