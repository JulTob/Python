from tkinter import *
import random

window = Tk()
window.title("20 D&D")
window.geometry("100x120")


answer = Message(text = "")
answer.place(x = 30, y = 40, width = 50, height = 27)
def click():
    num = random.randint(1,20)
    answer["text"] = num


button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 10, width = 50, height = 25)


window.mainloop()
