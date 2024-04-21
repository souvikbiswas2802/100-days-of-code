def factorial (number):
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)
print("Factorial Calculator")
num = int(input("Enter a number: "))
print(f"Facotrial of {num} is {factorial(num)}")
