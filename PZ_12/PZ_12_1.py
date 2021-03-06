# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x720")
label1 = Label(text = 'Форма заявки на работу в зоопарке', font = 'Arial 20')
label2 = Label(text = 'Пожалуйста, заполните форму. Обязательные поля отмечены', font = 'Arial 10')
label3 = Label(text = '*', fg = 'red', font = 'Arial 12')
label1.place(x = 20, y = 20)
label2.place(x = 20, y = 55)
label3.place(x = 397, y = 55)
label4 = Label(text = 'Контактная информация', font = 'Arial 12')
label4.place(x = 40, y = 90)
label5 = Label(text = 'Имя', font = 'Arial 11')
label6 = Label(text = '*', fg = 'red', font = 'Arial 12')
entry1 = Entry(width = 40)
label5.place(x = 40, y = 125)
label6.place(x = 75, y = 125)
entry1.place(x = 155, y = 125)
label7 = Label(text = 'Телефон', font = 'Arial 11')
entry2 = Entry(width = 40)
label7.place(x = 40, y = 160)
entry2.place(x = 155, y = 160)
label8 = Label(text = 'Email', font = 'Arial 11')
label9 = Label(text = '*', fg = 'red', font = 'Arial 12')
entry3 = Entry(width = 40)
label8.place(x = 40, y = 195)
label9.place(x = 83, y = 195)
entry3.place(x = 155, y = 195)
label10 = Label(text = 'Персональная информация', font = 'Arial 12')
label10.place(x = 40, y = 250)
label11 = Label(text = 'Возраст', font = 'Arial 11')
label12 = Label(text = '*', fg = 'red', font = 'Arial 12')
entry4 = Entry(width = 40)
label11.place(x = 40, y = 285)
label12.place(x = 103, y = 285)
entry4.place(x = 155, y = 285)
label12 = Label(text = 'Пол', font = 'Arial 11')
combobox1 = ttk.Combobox(values = ['Женщина', 'Мужчина'], state = 'readonly', width = 37)
label12.place(x = 40, y = 320)
combobox1.place(x = 155, y = 320)
label13 = Label(text = 'Перечислите', font = 'Arial 11')
label14 = Label(text = 'личные', font = 'Arial 11')
label15 = Label(text = 'качества', font = 'Arial 11')
label13.place(x = 40, y = 355)
label14.place(x = 40, y = 377)
label15.place(x = 40, y = 399)
text1 = Text(width = 30, height = 6)
text1.place(x = 155, y = 358)
label16 = Label(text = 'Выберите ваших любимых животных', font = 'Arial 12')
label16.place(x = 40, y = 495)
checkbutton1 = Checkbutton(text = 'Зебра', font = 'Arial 11')
checkbutton2 = Checkbutton(text = 'Слон', font = 'Arial 11')
checkbutton3 = Checkbutton(text = 'Кошка', font = 'Arial 11')
checkbutton4 = Checkbutton(text = 'Антилопа', font = 'Arial 11')
checkbutton5 = Checkbutton(text = 'Анаконда', font = 'Arial 11')
checkbutton6 = Checkbutton(text = 'Голубь', font = 'Arial 11')
checkbutton7 = Checkbutton(text = 'Человек', font = 'Arial 11')
checkbutton8 = Checkbutton(text = 'Краб', font = 'Arial 11')
checkbutton1.place(x = 42, y = 525)
checkbutton2.place(x = 42, y = 555)
checkbutton3.place(x = 182, y = 525)
checkbutton4.place(x = 182, y = 555)
checkbutton5.place(x = 322, y = 525)
checkbutton6.place(x = 322, y = 555)
checkbutton7.place(x = 462, y = 525)
checkbutton8.place(x = 462, y = 555)
button1 = Button(text = 'Отправить информацию', font = 'Arial 11')
button1.place(x = 20, y = 620)
root.mainloop()

