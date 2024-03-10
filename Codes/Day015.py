exit=""
while exit != "yes" and exit != "Yes":
  animal=input("What animal do you want?: ")
  if animal=="cow" or animal=="Cow":
    print("A cow goes moo.")
  elif animal=="cat" or animal=="Cat":
    print("A cat goes meow.")
  elif animal=="dog" or animal=="Dog":
    print("A dog goes woof.")
  elif animal=="sheep" or animal=="Sheep":
    print("A sheep goes baa.")
  elif animal=="horse" or animal=="Horse":
    print("A horse goes neigh.")
  elif animal=="pig" or animal=="Pig":
    print("A pig goes oink.")
  elif animal=="chicken" or animal=="Chicken":
    print("A chicken goes cluck.")
  elif animal=="duck" or animal=="Duck":
    print("A duck goes quack.")
  elif animal=="lion" or animal=="Lion":
    print("A lion goes roar.")
  elif animal=="tiger" or animal=="Tiger":
    print("A tiger goes roar.")
  elif animal=="bear" or animal=="Bear":
    print("A bear goes growl.")
  else:
    print("I don't know that animal.")

  exit=input("Do you want to exit?: ")
    
