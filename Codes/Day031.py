def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App{colorChange('blue')} ={colorChange('white')}={colorChange('red')}="
body = f"""
🔥▶️  {colorChange('white')}Radio Gaga
     {colorChange('yellow')}Queen

{colorChange('white')}PREV
      {colorChange('green')}NEXT
            {colorChange('purple')}PAUSE
"""
print(f"{title:^70}")
print(f"{body}")

print("\n\n")
dash = f"{colorChange('red')}--------------------------------------"
print(f"{dash:^60}")
print("\n\n")

title1 = f"{colorChange('white')}WELCOME TO"
title2 = f"{colorChange('blue')}--    ARMBOOK    --"
print(f"{title1:^40}\n{title2:^40}\n")
body1 = f"{colorChange('yellow')}Definitely not a rip off of"
body2 = f"{colorChange('yellow')}a certain other social"
body3 = f"{colorChange('yellow')}networking site."
print(f"{body1:>40}\n{body2:>40}\n{body3:>40}\n")
body4 = f"{colorChange('red')}Honest."
print(f"{body4:^40}\n")
body5 = f"{colorChange('white')}Username:"
body6 = f"{colorChange('white')}Password:"
print(f"{body5:^40}\n{body6:^40}")
