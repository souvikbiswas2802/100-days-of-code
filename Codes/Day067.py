import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "dhoni" or person.lower().strip() == "thala":
    canvas.itemconfig(container, image=dhoni)
  elif person.lower().strip() == "srk":
    canvas.itemconfig(container, image=srk)
  elif person.lower().strip() == "dhruv":
    canvas.itemconfig(container, image=dhruv)
  elif person.lower().strip() == "kohli":
    canvas.itemconfig(container, image=kohli)
  else:
    hello["text"] = "Unable to find this user"

hello = tk.Label(text=label)
hello.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
srk = ImageTk.PhotoImage(Image.open("guessWho/srk.jpg"))
dhruv = ImageTk.PhotoImage(Image.open("guessWho/dhruv.jpg"))
kohli = ImageTk.PhotoImage(Image.open("guessWho/kohli.jpg"))
dhoni = ImageTk.PhotoImage(Image.open("guessWho/dhoni.jpg"))
container = canvas.create_image(180,120,image=dhoni)

tk.mainloop()
