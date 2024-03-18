def login():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == "admin" and password == "password":
    print("Login successful!")
    exit()
  else:
    print("Login failed. Please try again.")
    print()

print("Replit Login System")
print()
while True:
  login()
