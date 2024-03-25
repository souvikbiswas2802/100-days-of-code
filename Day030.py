print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^30}")
  print(f"{thought:^30}")
  print()
