from tkinter import *
import random

def click():
    num = random.randint(1,20)
    answer["text"] = num

window = Tk()
window.title("Roll a dice")
window.geometry("200x200")

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)

answer = Message(text = "")
answer.place(x = 40, y = 100, width = 30, height = 25)

window.mainloop()
