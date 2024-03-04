print("\033[32m", "Generation Generator")
print("-----------------------", "\033[0m")
print()
age = int(input("What year were you born? "))
if age >= 1925 and age <= 1946:
  print("You are a Traditionalist.")
elif age >= 1947 and age <= 1964:
  print("You are a Baby Boomer.")
elif age >= 1965 and age <= 1981:
  print("You are a Generation X.")
elif age >= 1982 and age <= 1995:
  print("You are a Millenial.")
elif age >= 1996 and age <= 2015:
  print("You are a Generation Z.")
else:
  print("You are either too young or too old.")
