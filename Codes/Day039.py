hangman = [
"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,
"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___
    """,
"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___
    """,
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___
    """,
"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___
    """,

"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___
    """]

import random, os, time

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")
def print_hangman(tries):
  print(hangman[tries])
def print_hearts(lives):
  hearts = ""
  for i in range (lives):
    hearts = hearts + "❤️ "
  return hearts
def brokenHearts(lost):
  hearts = ""
  for i in range (lost):
    hearts = hearts + "💔"
  return hearts
  
listOfWords = ["apple", "earth", "peach", "grape", "chair", "table", "mouse", "candy", "happy", "mango", "berry", "water"]
word = random.choice(listOfWords)
lives = 5
letterList = []
lostlives = 0
while True:
  name = "HANGMAN GAME"
  print(f"{name:^35}")
  print_hangman(5-lives)
  print()
  print("Lives left: ", print_hearts(lives), brokenHearts(lostlives), sep="")
  print()
  letter = input("Guess a letter: ").lower()
  if letter in letterList:
    print("You already guessed that letter!")
  else: 
    if letter in word:
      print("Correct!")
      letterList.append(letter)
    else:
      print("Nope, not in there.")
      lives -= 1
      lostlives += 1
  allLetters = True
  for letters in word:
    if letters in letterList:
      print(letters, end="")
    else:
      print("_", end="")
      allLetters = False
  print()
  wait(2)
  if lives == 0:
    print("You lost!💔💔💔💔💔")
    break
  if allLetters == True:
    print("You won with", print_hearts(lives), "lives left!🤠")
    break
  
    
