import requests, json, os, time

from replit import db

def wait(seconds):
  time.sleep(seconds)
  os.system("clear")

def getJoke():
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  joke = result.json()
  joketext = joke["joke"]
  jokeid = joke["id"]
  print(f"{joketext}\n\n")
  choice = input("1. Save joke\n2. Load old jokes\n3. New joke\n> ")
  if choice == "1":
    db[jokeid] = joketext
    print("Joke Saved!")
    wait(1)
    getJoke()
  elif choice == "2":
    i = 1
    wait(0)
    keys = db.keys()
    if keys:
      for key in keys:
        print(f"{i}. {db[key]}\n\n")
        i+=1
      newjoke = input("Generate new joke? (y/n): ")
      if newjoke.lower() == "y":
        wait(0)
        getJoke()
      else:
        print("\nGoodbye!")
    else:
      print("You havent saved any jokes yet!")
      wait(1)
      getJoke()
  elif choice == "3":
    wait(0)
    getJoke()
  
getJoke()
