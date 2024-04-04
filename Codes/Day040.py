import os, time
def wait(seconds):
  time.sleep(seconds)
  os.system('clear')

while True:
  print("🌟Contact Card Generator🌟")
  print()
  name = input("Input your name > ").strip().title()
  dob = input("Input your date of birth(DD/MM/YYYY) > ")
  tel = input("Input your telephone number > ")
  email = input("Input your email > ")
  address = input("Input your address > ")
  contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}
  wait(1)
  print("Here's your contact card")
  print()
  print(f"Name: {contact['name']}")
  print(f"DOB: {contact['dob']}")
  print(f"Tel: {contact['tel']}")
  print(f"Email: {contact['email']}")
  print(f"Address: {contact['address']}")
  wait(4)
  confirm = input("Want to generate againg? (y/n) > ").strip().lower()
  if confirm == "y":
    wait(0)
    continue
  elif confirm == "n":
    wait(0)
    print("Thank You")
    wait(1)
    break
  else:
    wait(0)
    print("Invalide input")
