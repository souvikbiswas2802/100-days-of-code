from replit import db
import datetime, os, time

def add():
  tweet = input("Enter Your Tweet: ")
  timestamp = datetime.datetime.now()
  key = f"{timestamp}"
  db[key] = tweet

def view():
  keys = db.keys()
  i = 1
  for key in keys:
    print(f"{key}: {db[key]}")
    if i % 10 == 0:
      more = input("Do you want to see more tweets? (y/n): ")
      if more == "n":
        break
      os.system("clear")

def delete():
  keys = db.keys()
  for key in keys:
    print(f"{key}: {db[key]}")
  delete = input("Enter the key to delete: ")
  del db[delete]

while True:
  time.sleep(4)
  os.system("clear")
  print("Welcome to Tweeter\n")
  menu = input("1: Add Tweet\n2: View Tweets\n3: Delete Tweet\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    delete()
  else:
    print("Invalid Input")
