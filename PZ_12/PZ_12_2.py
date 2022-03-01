# -*- coding: utf-8 -*-
# Вариант 2
# Проверить истинность высказывания: «Число A является нечететным"
from tkinter import *
root = Tk()
root.title("Задание 2")
root.geometry("600x115")

lbll = Label(root, text="Проверить истинность высказывания: "
                        "Число A является нечетным")
lbll.place(x=0, y=0)

lbl2 = Label(root, text="Введите целое число")
lbll.place(x=20, y=40)

tx =Entry(root, width=10)
tx.place(x=330, y=20)

def clicked():
    a = tx.get()
    a = int(a)
    if a % 2 == 0:
        lbl4 = Label(root, text="Ложь", font=("Times New Roman", 11), fg='red')
        lbl4.place(x=310, y=90)
    else:
        lbl4 = Label(root, text="Истина", font=("Times New Roman", 11), fg='green')
        lbl4.place(x=310, y=90)

bt = Button(root, text='Проверить', command=clicked)
bt.place(x=300, y=60)
root.mainloop()


