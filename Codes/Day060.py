import datetime

print("Event Count Down Timer")
print()
date = input("Input Event Date: ")
month = input("Input Event Month: ")
year = input("Input Event Year: ")
event = datetime.date(year=int(year), month=int(month), day=int(date))
today = datetime.date.today()
if event > today:
  print(f"Coming soon in {event - today}")
elif event < today:
  print(f"Hope you enjoyed it {today - event}, time ago.")
else:
  print("HOLIDAY TIME!")
