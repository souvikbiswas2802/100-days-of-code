import csv

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file) 
  totalcost = 0  
  for row in reader: 
    totalcost += (float(row["Cost"]) * int(row["Quantity"]))
    
print("Calculating...")
print(f"\n\nTotal Cost: {round(totalcost,3)}")
