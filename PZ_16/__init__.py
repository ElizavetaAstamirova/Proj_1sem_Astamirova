# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#1c2957', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD_16/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить', width=155, command=self.open_dialog, bg='#57A0D2', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD_16/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#57A0D2',
                                    bd=0, width=155, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD_16/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#57A0D2',
                                    bd=0, width=155, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD_16/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#57A0D2',
                               bd=0, width=155, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD_16/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#57A0D2',
                               bd=0, width=155, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('add_FIO', 'product', 'measurement', 'quantity', 'price', 'nagr', 'ad', 'spec'), height=15, show='headings')

        self.tree.column('add_FIO', width=153, anchor=tk.CENTER)
        self.tree.column('product', width=112, anchor=tk.CENTER)
        self.tree.column('measurement', width=113, anchor=tk.CENTER)
        self.tree.column('quantity', width=112, anchor=tk.CENTER)
        self.tree.column('price', width=113, anchor=tk.CENTER)
        self.tree.column('nagr', width=72, anchor=tk.CENTER)
        self.tree.column('ad', width=113, anchor=tk.CENTER)
        self.tree.column('spec', width=112, anchor=tk.CENTER)

        self.tree.heading('add_FIO', text='Регистрационный номер')
        self.tree.heading('product', text='Фамилия')
        self.tree.heading('measurement', text='Имя')
        self.tree.heading('quantity', text='Отчество')
        self.tree.heading('price', text='Дата рождения')
        self.tree.heading('nagr', text='Награды')
        self.tree.heading('ad', text='Адрес')
        self.tree.heading('spec', text='Специальность')

        self.tree.pack()

    def records(self, add_FIO, product, measurement, quantity, price, nagr, ad, spec):
        self.db.insert_data(add_FIO, product, measurement, quantity, price, nagr, ad, spec)
        self.view_records()

    def update_record(self, add_FIO, product, measurement, quantity, price, nagr, ad, spec):
        self.db.cur.execute("""UPDATE users SET add_FIO=?, product=?, measurement=?, quantity=?, price=?, nagr=?, ad=?, spec=? WHERE add_FIO=?""",
                            (add_FIO, product, measurement, quantity, price, nagr, ad, spec, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE add_FIO=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, product):
        product = ("%" + product + "%",)
        self.db.cur.execute("""SELECT * FROM users WHERE product LIKE ?""", product)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, score):
    #    score = (score,)
    #    self.db.cur.execute("""SELECT * FROM users WHERE score>?""", score)
    #    [self.tree.delete(i) for i in self.tree.get_children()]
    #    [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Анкета')
        self.geometry('600x350+400+300')
        self.resizable(False, False)

        label_add_FIO = tk.Label(self, text='Регистрационный номер')
        label_add_FIO.place(x=80, y=25)
        self.entry_add_FIO = ttk.Entry(self)
        self.entry_add_FIO.place(x=230, y=25)

        label_product = tk.Label(self, text='Фамилия')
        label_product.place(x=80, y=50)
        self.entry_product = ttk.Entry(self)
        self.entry_product.place(x=230, y=50)

        label_measurement = tk.Label(self, text='Имя')
        label_measurement.place(x=80, y=75)
        self.entry_measurement = ttk.Entry(self)
        self.entry_measurement.place(x=230, y=75)

        label_quantity = tk.Label(self, text='Отчество')
        label_quantity.place(x=80, y=100)
        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.place(x=230, y=100)

        label_price = tk.Label(self, text='Дата рождения')
        label_price.place(x=80, y=125)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=230, y=125)

        label_fatima = tk.Label(self, text='Награды')
        label_fatima.place(x=80, y=150)

        label_nagr = tk.Label(self, text='Кр. Диплом')
        label_nagr.place(x=80, y=175)
        self.combobox = ttk.Combobox(self, values=[u'Да', u'Нет'])
        self.combobox.current(0)
        self.combobox.place(x=230, y=175)

        label_nagr2 = tk.Label(self, text='Медали')
        label_nagr2.place(x=80, y=200)
        self.combobox = ttk.Combobox(self, values=[u'Да', u'Нет'])
        self.combobox.current(0)
        self.combobox.place(x=230, y=200)

        label_ad = tk.Label(self, text='Адрес')
        label_ad.place(x=80, y=225)
        self.entry_ad = ttk.Entry(self)
        self.entry_ad.place(x=230, y=225)

        label_spec = tk.Label(self, text='Специальность')
        label_spec.place(x=80, y=250)
        self.entry_spec = ttk.Entry(self)
        self.entry_spec.place(x=230, y=250)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=300)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=300)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_add_FIO.get(),
                                                                       self.entry_product.get(),
                                                                       self.entry_measurement.get(),
                                                                       self.entry_quantity.get(),
                                                                       self.entry_price.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_ad.get(),
                                                                       self.entry_spec.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_add_FIO.get(),
                                                                          self.entry_product.get(),
                                                                          self.entry_measurement.get(),
                                                                          self.entry_quantity.get(),
                                                                          self.entry_price.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_ad.get(),
                                                                          self.entry_spec.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск по фамилии")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD_16/shop.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                add_FIO INTEGER NOT NULL DEFAULT 1,
                product TEXT NOT NULL,
                measurement TEXT NOT NULL,
                quantity TEXT NOT NULL,
                price INTEGER,
                nagr INTEGER NOT NULL DEFAULT 1,
                ad TEXT,
                spec TEXT
                )""")

    def insert_data(self, add_FIO, product, maesurement, quantity, price, nagr, ad, spec):
        self.cur.execute("""INSERT INTO users(add_FIO, product, measurement, quantity, price, nagr, ad, spec) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (add_FIO, product, maesurement, quantity, price, nagr, ad, spec))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Абитуриент")
    root.geometry("900x450+300+200")
    root.resizable(False, False)
    root.mainloop()