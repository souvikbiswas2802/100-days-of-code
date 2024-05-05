import os, time, random

from replit import db

def wait(seconds):
  time.sleep(seconds)
  os.system('clear')

def salt():
  salt = random.randint(1000, 9999)
  return salt

def addUser():
  print("Add User")
  print()
  keys = db.keys()
  username = input("Username: ")
  if username in keys:
    print("Username already exists")
  else:
    password = input("Password: ")
    saltValue = salt()
    newPassword = f"{password}{saltValue}"
    newPassword = hash(newPassword)
    db[username] = {"password": newPassword, "salt": saltValue}
    print("User added")
  wait(1)

def login():
  print("Log In")
  print()
  username = input("Username: ")
  keys = db.keys()
  if username not in keys:
    print("Username does not exist")
  else:
    password = input("Password: ")
    saltValue = db[username]["salt"]
    newPassword = f"{password}{saltValue}"
    newPassword = hash(newPassword)
    if newPassword == db[username]["password"]:
      print("Login successful")
    else:
      print("Incorrect password")
  wait(1)

while True:
  print("Login System")
  print()
  menu = input("1: Add User\n2: Login\n> ")
  wait(0)
  if menu == "1":
    addUser()
  elif menu == "2":
    login()
  else:
    print("Invalid input")
