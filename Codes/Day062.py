from replit import db
import os, time, datetime, getpass

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
  
#Password = souvik2005
password = getpass.getpass("Enter Password: ")
if password == "souvik2005":
  wait(1)
  while True:
    print("Welcome to Private Diary📖\n")
    menu = input("1: Add\n2: View\n> ")
    wait(0)
    if menu == "1":
      add()
    elif menu == "2":
      view()
    else:
      print("Invalid Input")
      wait(1)
else:
  print("Incorrect Password")
