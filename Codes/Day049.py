import time
f = open("high.score", "r")
scores = f.read().split("\n")
f.close()
highscore = 0
name = ""
print("🌟Current Leader🌟")
print()
print("Analyzing high scores......\n")
for score in scores:
  data = score.split()
  for i in data:
    if i.isnumeric() and int(i) > highscore:
      highscore = int(i)
      name = data[0]
time.sleep(2)
print(f"The winner is {name} with a score of {highscore}")
