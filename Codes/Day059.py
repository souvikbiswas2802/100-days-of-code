import os, time

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

def palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

while True:
  print("🌟Palindrome Checker🌟")
  print()
  word = input("Input a word > ").lower()
  print()
  if palindrome(word) is True:
    print(f"{word} is a palindrome. Yay!")
  else:
    print(f"{word} is not a palindrome.")
  wait(2)
