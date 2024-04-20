import csv, os
os.mkdir("Songs")
with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    folder = row["Artist(s)"]
    allfiles = os.listdir("Songs")
    if folder not in allfiles:
      os.mkdir(f"Songs/{folder}")
    filename = os.path.join(f"Songs/{folder}/", f"{row['Song']}.txt")
    f = open(filename, "w")
    f.close()
    print(f"Adding, {row['Song']} by {row['Artist(s)']}")
