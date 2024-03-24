def colorPrinting(color, text):
  if color == "red":
    print("\033[31m", text, sep="", end="")
  elif color == "green":
    print("\033[32m", text, sep="", end="")
  elif color == "blue":
    print("\033[34m", text, sep="", end="")
  elif color == "purple":
    print("\033[35m", text, sep="", end="")
  elif color == "yellow":
    print("\033[33m", text, sep="", end="")
  else:
    print("\033[0m", text, sep="", end="")

print("Super Subroutine")
print()
print("With my ", end="")
colorPrinting("purple", "new program")
colorPrinting("reset", " I can just call red('and') ")
colorPrinting("red", "and ")
colorPrinting("reset", "that word will appear in the color I set it to.")
print()
print()
print("With no ", end="")
colorPrinting("green", "weird gaps")
print(".")
print()
colorPrinting("reset", "Epic.")
