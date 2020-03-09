from tkinter import *


window = Tk()
window.geometry("500x200")

textbox1 = Entry(text = "")
textbox1.place(x = 155, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

textbox2 = Message(text = "")
textbox2.place(x = 155, y = 50, width = 200, height = 50)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "grey"
    textbox2["fg"] = "blue"
    textbox2["text"] = message



labell = Label(text = "Enter your name: ")
labell.place(x = 30, y = 20)

button1 = Button(text = "Press", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)


window.mainloop()
