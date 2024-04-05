myDictionary = {"Name" : None, "URL": None, "Description": None, "Rating": None}
print("🌟Website Rating🌟")
print()
myDictionary["Name"] = input("Input the website name: ").strip()
myDictionary["URL"] = input("Input the URL: ").strip()
myDictionary["Description"] = input("Input your a description: ").strip()
myDictionary["Rating"] = input("Input the a star rating out of 5: ").strip()
print()
for name, value in myDictionary.items():
  print(f"{name}: {value}")
