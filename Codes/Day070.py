import os

adminUsername = os.environ['adminUsername']
adminPassword = os.environ['adminPassword']

username = input("Username: ")
userpass = input("Password: ")

if username == adminUsername and userpass == adminPassword:
  print("Welcome Admin")
else:
  print("Welcome Regular User")
