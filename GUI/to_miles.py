from tkinter import *


window = Tk()
window.title("To Miles")
window.geometry("300x250")

enter_lbl = Label(text = "Enter km: ")
enter_lbl.place(x = 30, y = 20)


enter_txt = Entry(text = 0)
enter_txt.place(x = 30, y = 50, width = 200, height = 25)
enter_txt["justify"] = "center"
enter_txt.focus()


output_txt = Entry(text = 0)
output_txt.place(x = 30, y = 100, width = 100, height= 35)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"
enter_txt["justify"] = "center"
def convert():
    km = enter_txt.get()
    km = int(km)
    result = km * 0.6214
    output_txt.delete(0, END)
    output_txt.insert(END, result)
    output_txt.insert(END, " miles")


convert_btn = Button(text = "convert", command = convert)
convert_btn.place(x = 200, y = 20, width = 75, height= 25)



window.mainloop()
