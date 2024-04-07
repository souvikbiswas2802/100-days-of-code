import random, time, os

def wait(seconds):
  time.sleep(seconds)
  os.system('clear')

def number():
  number = random.randint(1,90)
  return number

while True:
  wait(1)
  print("Bingo Card Generator")
  print()
  bingoCard = [[number(), number(), number()],
               [number(), "BINGO", number()],
               [number(), number(), number()]]
  ele00 = f"{bingoCard[0][0]}"
  ele01 = f"{bingoCard[0][1]}"
  ele02 = f"{bingoCard[0][2]}"
  ele10 = f"{bingoCard[1][0]}"
  ele11 = f"{bingoCard[1][1]}"
  ele12 = f"{bingoCard[1][2]}"
  ele20 = f"{bingoCard[2][0]}"
  ele21 = f"{bingoCard[2][1]}"
  ele22 = f"{bingoCard[2][2]}"
  
  print(f"{ele00:^10} | {ele01:^10} | {ele02:^10}")
  print("------------------------------------")
  print(f"{ele10:^10} | {ele11:^10} | {ele12:^10}")
  print("------------------------------------")
  print(f"{ele20:^10} | {ele21:^10} | {ele22:^10}")
  print()
  confirm = input("Press 'Y' to generate a new card,\nPress anything else to exit.\n>  ").strip().lower()
  if confirm == "y":
    continue
  else:
    break
