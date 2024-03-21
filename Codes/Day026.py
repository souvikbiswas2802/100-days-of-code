from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    print("Press 2 to stop playback and go back to the menu")
    userInput = int(input("> "))
    if userInput == 2:
      source.paused = True
      return
    else:
      continue
    
while True:
  os.system("clear")
  print("🎶MUSIC PLAYER")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  time.sleep(1)
  userInput = int(input("> "))
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue
  
