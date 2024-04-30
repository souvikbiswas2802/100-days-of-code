import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("400x200") 

answer = 0

def typeanswer(value):
  global answer
  if answer == 0:
    answer = f"{value}"
  else:
    answer = f"{answer}{value}"
  calc["text"] = answer

def calculate():
  global answer
  answer = eval(answer)
  calc["text"] = answer

def reset():
  global answer
  answer = 0
  calc["text"] = answer


calc = tk.Label(text = answer)
calc.grid(row=0, column=1)

one = tk.Button(text = "1", command = lambda: typeanswer(1))
one.grid(row=1, column=0)
two = tk.Button(text = "2", command = lambda: typeanswer(2))
two.grid(row=1, column=1)
three = tk.Button(text = "3", command = lambda: typeanswer(3))
three.grid(row=1, column=2)
four = tk.Button(text = "4", command = lambda: typeanswer(4))
four.grid(row=2, column=0)
five = tk.Button(text = "5", command = lambda: typeanswer(5))
five.grid(row=2, column=1)
six = tk.Button(text = "6", command = lambda: typeanswer(6))
six.grid(row=2, column=2)
seven = tk.Button(text = "7", command = lambda: typeanswer(7))
seven.grid(row=3, column=0)
eight = tk.Button(text = "8", command = lambda: typeanswer(8))
eight.grid(row=3, column=1)
nine = tk.Button(text = "9", command = lambda: typeanswer(9))
nine.grid(row=3, column=2)
zero = tk.Button(text = "0", command = lambda: typeanswer(0))
zero.grid(row=4, column=1)
add = tk.Button(text = "+", command = lambda: typeanswer("+"))
add.grid(row=1, column=3)
minus = tk.Button(text = "-", command = lambda: typeanswer("-"))
minus.grid(row=1, column=4)
multiply = tk.Button(text = "*", command = lambda: typeanswer("*"))
multiply.grid(row=2, column=3)
divide = tk.Button(text = "/", command = lambda: typeanswer("/"))
divide.grid(row=2, column=4)
equals = tk.Button(text = "=", command = calculate)
equals.grid(row=3, column=3)
clear = tk.Button(text="C", command=reset)
clear.grid(row=3, column=4)


tk.mainloop()
