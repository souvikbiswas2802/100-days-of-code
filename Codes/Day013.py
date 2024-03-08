print("Exam Grade Calculator")
print()
exam = input("Name of exam: ")
print()
maxScore = int(input("Max. Possible Score: "))
print()
yourScore = float(input("Your score: "))
print()
if yourScore <= maxScore:
  percetage = round(float(yourScore / maxScore) * 100, 2)
  if percetage >= 90:
    print("\033[32m", "You got", percetage, "% which is a A+", "\033[0m")
  elif percetage >= 80:
    print("\033[32mYou got", percetage, "% which is a A", "\033[0m")
  elif percetage >= 70:
    print("\033[34mYou got", percetage, "% which is a B", "\033[0m")
  elif percetage >= 60:
    print("\033[34mYou got", percetage, "% which is a C", "\033[0m")
  elif percetage >= 50:
    print("\033[33mYou got", percetage, "% which is a D", "\033[0m")
  else:
    print("\033[31mYou got", percetage, "% which is a U", "\033[0m")

else:
  print("You can't get more than the max score!")
