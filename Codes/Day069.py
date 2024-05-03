import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")
story = "You meet Dhoni on the way from a Cricket Tournament."

def greet():
  global story
  canvas.itemconfig(container, image=greets)
  story = "He asked you to play a little game of cricket with him."
  storyLabel["text"] = story
  button1.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def criticize():
  global story
  canvas.itemconfig(container, image=criticizes)
  story = "You criticize him and he gets angry and leaves the place. \nYou lose."
  storyLabel["text"] = story
  button1.pack_forget()
  button2.pack_forget()
  restartButton.pack()

def playNow():
  global story
  canvas.itemconfig(container, image=now)
  story = "You Both played for about 2 hours and you both got tired. \nYou both left the place."
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def playLater():
  global story
  canvas.itemconfig(container, image=raining)
  story = "You told him you are busy today and \nwill play with him next sunday. \nBut it is raining so heavy."
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  button5.pack()
  button6.pack()

def go():
  global story
  canvas.itemconfig(container, image=now)
  story = "You decided to go inspite of heavy raining,\n you were amazed when you saw that Dhoni was waiting for you,\n you both played cricket together. \nHe won the match and you both went home."
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()

def dont():
  global story
  canvas.itemconfig(container, image=sad)
  story = "You didn't go to play. You made Dhoni Sad. You Loose."
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()

def restart():
  global story
  canvas.itemconfig(container, image=start)
  story = "You meet Dhoni on the way from a Cricket Tournament."
  storyLabel["text"] = story
  restartButton.pack_forget()
  button1.pack()
  button2.pack()

start_img = Image.open("p1.png")
greets_img = Image.open("p3.jpg")
criticizes_img = Image.open("p2.jpg")
now_img = Image.open("p4.jpg")
raining_img = Image.open("p5.jpg")
sad_img = Image.open("p6.jpg")

start = ImageTk.PhotoImage(start_img)
greets = ImageTk.PhotoImage(greets_img)
criticizes = ImageTk.PhotoImage(criticizes_img)
now = ImageTk.PhotoImage(now_img)
raining = ImageTk.PhotoImage(raining_img)
sad = ImageTk.PhotoImage(sad_img)

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()
container = canvas.create_image(150,150, image=start)
storyLabel = tk.Label(text=story)
storyLabel.pack()
button1 = tk.Button(text="Greet Him and tell how exceptional player he is.", command=greet)
button1.pack()
button2 = tk.Button(text="Criticize Him!", command=criticize)
button2.pack()
button3 = tk.Button(text="Play right Now.", command=playNow)
button4 = tk.Button(text="Play next sunday.", command=playLater)
button5 = tk.Button(text="Go to Play.", command=go)
button6 = tk.Button(text="Don't Go.", command=dont)
restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()
