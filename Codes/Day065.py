class charecter:
  name = ""
  health = 0
  magicpoints = 0
  
  def __init__(self, name):
    self.name = name
    
  def setStats(self, health, magicpoints):
    self.health = health
    self.magicpoints = magicpoints

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicpoints}")


class player(charecter):
  nickname = ""
  lives = 0

  def __init__(self, nickname, lives):
    self.name = "Player"
    self.nickname = nickname
    self.lives = lives

  def setStats(self, health, magicpoints):
    self.health = health
    self.magicpoints = magicpoints

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} is Alive!")
    else:
      print(f"{self.nickname} is Dead!")
      
  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicpoints}\nNickname: {self.nickname}\nLives: {self.lives}")


class enemy(charecter):
  type = ""
  strength = 0

  def __init__(self, type, strength):
    self.name = "Enemy"
    self.type = type
    self.strength = strength

  def setStats(self, health, magicpoints):
    self.health = health
    self.magicpoints = magicpoints

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicpoints}\nType: {self.type}\nStrength: {self.strength}")


class orc(enemy):
  speed = 0

  def __init__(self, speed):
    self.name = "Enemy"
    self.type = "Orc"
    self.speed = speed

  def setStats(self, health, magicpoints, strength):
    self.health = health
    self.magicpoints = magicpoints
    self.strength = strength

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicpoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Enemy"
    self.type = "Vampire"
    self.day = day

  def setStats(self, health, magicpoints, strength):
    self.health = health
    self.magicpoints = magicpoints
    self.strength = strength

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicpoints}\nType: {self.type}\nStrength: {self.strength}\nDay: {self.day}")

ankit = vampire(False)
ankit.setStats(100, 50, 10)
ankit.print()
print()
orc = orc(100)
orc.setStats(100, 50, 10)
orc.print()
