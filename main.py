from tkinter import *
from tkinter import messagebox
from morze import *

window = Tk()
window.title("Азбука Морзе")
window.geometry('600x250')


def clicked():
    content = txt.get()
    result = Russian_to_Morse(content)
    lbl_res.configure(text=f"Результат {result}")

lbl = Label(window, text="Введите текст")
lbl.grid(column=0, row=0)
txt = Entry(window, width=50)
txt.grid(column=1, row=0)
btn = Button(window, text="Конвертировать", command=clicked)
btn.grid(column=2, row=0)
lbl_res = Label(window, text="Результат:", font=("Arial Bold", 14))
lbl_res.grid(column=0, row=1, columnspan=2)

















window.mainloop()
