import datetime
import tkinter as tk
from tkinter import *

import pymysql

from connect import host, user, password, db_name

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)


def zapolnenie():
    global result
    result = []

    window2 = Tk()
    window2.title("Форма заполнения")
    window2.geometry('300x200+700+300')
    window2.resizable(False, False)
    window2.configure(background='#BF7F30')

    txt_1 = Entry(window2, width=20, bg='#BF9930')
    txt_1.grid(row=5, column=2)

    varibale1 = tk.StringVar()
    varibale1.set("Выберите должность")

    def get_doljnost():
        with connection.cursor() as cursor:
            sql = f"SELECT id_dolj, name_dolj FROM doljnost"
            cursor.execute(sql)
            res = cursor.fetchall()
            arg = {}
            for i in res:
                arg[i["name_dolj"]] = [i["id_dolj"]]
            return arg

    arg1 = get_doljnost()
    val = []
    for i in arg1:
        val.append(i)

    def add_doljnost(var):
        result.append(varibale1.get())
        print(result)

    combobox1 = tk.OptionMenu(window2, varibale1, *val, command=add_doljnost)
    combobox1.grid(row=7, column=2)

    txt_3 = Entry(window2, width=20, bg='#BF9930')
    txt_3.grid(row=8, column=2)

    varibale2 = tk.StringVar()
    varibale2.set("Выберите профессию")

    def get_profession():
        with connection.cursor() as cursor:
            sql = f"SELECT id_profs, name_profs FROM profesion"
            cursor.execute(sql)
            res = cursor.fetchall()
            arg = {}
            for i in res:
                arg[i["name_profs"]] = [i["id_profs"]]
            return arg

    arg2 = get_profession()
    val = []
    for i in arg2:
        val.append(i)

    def add_profession(var):
        result.append(varibale2.get())
        print(result)

    combobox2 = tk.OptionMenu(window2, varibale2, *val, command=add_profession)
    combobox2.grid(row=9, column=2)

    varibale3 = tk.StringVar()
    varibale3.set("Выберите образование")

    def get_obrazovanie():
        with connection.cursor() as cursor:
            sql = f"SELECT id_obraz, name_obraz FROM obrazovanie"
            cursor.execute(sql)
            res = cursor.fetchall()
            arg = {}
            for i in res:
                arg[i["name_obraz"]] = [i["id_obraz"]]
            return arg

    arg3 = get_obrazovanie()
    val = []
    for i in arg3:
        val.append(i)

    def add_obrazovanie(var):
        result.append(varibale3.get())
        print(result)

    combobox3 = tk.OptionMenu(window2, varibale3, *val, command=add_obrazovanie)
    combobox3.grid(row=10, column=2)

    varibale4 = tk.StringVar()
    varibale4.set("Уровень владения ПК")

    def get_levc():
        with connection.cursor() as cursor:
            sql = f"SELECT id_levc, name_levc FROM level_vlad_comp"
            cursor.execute(sql)
            res = cursor.fetchall()
            arg = {}
            for i in res:
                arg[i["name_levc"]] = [i["id_levc"]]
            return arg

    arg4 = get_levc()
    val = []
    for i in arg4:
        val.append(i)

    def add_levc(var):
        result.append(varibale4.get())
        print(result)

    combobox3 = tk.OptionMenu(window2, varibale4, *val, command=add_levc)
    combobox3.grid(row=11, column=2)

    lbl_one1 = Label(window2, text='ФИО', bg='#BF7F30').grid(row=5, column=1)
    lbl_one2 = Label(window2, text='Должность', bg='#BF7F30').grid(row=7, column=1)
    lbl_one3 = Label(window2, text='Актуальность', bg='#BF7F30').grid(row=8, column=1)
    lbl_one4 = Label(window2, text='Профессия', bg='#BF7F30').grid(row=9, column=1)
    lbl_one4 = Label(window2, text='Образование', bg='#BF7F30').grid(row=10, column=1)
    lbl_one5 = Label(window2, text='Уровень владения ПК', bg='#BF7F30').grid(row=11, column=1)

    # not work
    def get_vakansia(result):
        with connection.cursor() as cursor:
            fiov = txt_1.get()
            actual = txt_3.get()
            res = result
            now = datetime.datetime.now()
            k = (now.strftime("%Y-%m-%d"))
            sql = f"INSERT INTO vakansia (data_opubl, kod_dolj, actual, kod_profs, kod_obraz, kod_levc, FIO) " \
                  f"VALUES('{k}', '{arg1[res[0]]}', '{actual}', '{arg2[res[1]]}', '{arg3[res[2]]}', '{arg4[res[3]]}', '{fiov}')"
            print(sql)
            cursor.execute(sql)

    btn_reg = Button(window2, text='Отправить', command=lambda: get_vakansia(result), bg='#BF9930').grid(row=12,
                                                                                                         column=2)
    window2.mainloop()


root1 = Tk()
root1.title("Форма для вакансии")
root1.geometry('300x200+700+300')
root1.resizable(False, False)
root1.configure(background='#BF7F30')
btn_reg = Button(text='Заполнить заявку', command=zapolnenie, bg='#BF9930')
btn_reg.place(x=90, y=75)
root1.mainloop()
