from replit import db

import os, time, datetime, getpass, random

def salting():
  salt = random.randint(1000,9999)
  return salt

def userDiary():
  print("Welcome to Private Diary📖\n")
  menu = input("1: Add\n2: View\n> ")
  wait(0)
  if menu == "1":
    add()
    userDiary()
  elif menu == "2":
    view()
    userDiary()
  else:
    print("Invalid Input")
    userDiary()
    wait(1)

def wait(sec):
  time.sleep(sec)
  os.system('clear')

def add():
  note = input("Enter your note: ").strip().title()
  timestamp = datetime.datetime.now()
  key = f"{timestamp}"
  db[key] = note
  print("Note Added to Diary")
  wait(1)

def view():
  keys = db.keys()
  keys = db.prefix("2")
  if keys:
    for key in keys:
      print(f"{key} : {db[key]}")
      choice = input("\nPress:\n1: See Previous Note\n2: Exit\n> ")
      if choice == "1":
        wait(0)
        continue
      else:
        break
  else:
    print("No notes found")
  wait(1)

keys = db.keys()
if len(keys) < 1:
  print("Create a new account to continue\n")
  username = input("Enter your username: ")
  password = getpass.getpass("Enter your password: ")
  salt = salting()
  newPassword = f"{password}{salt}"
  db[username] = {"password": newPassword, "salt": salt}
  wait(1)
  userDiary()
else:
  print("Login to your account\n")
  username = input("Enter your username: ")
  password = getpass.getpass("Enter your password: ")
  if username in keys:
    salt = db[username]["salt"]
    newPassword = f"{password}{salt}"
    if newPassword == db[username]["password"]:
      wait(0)
      userDiary()
    else:
      print("Incorrect Password")
      wait(1)
