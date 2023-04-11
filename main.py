from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import datetime
import pymysql
import tkinter as tk
from tkinter import messagebox
from connect import host, user, password, db_name

connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

def zapolnenie():
        window2 = Tk()
        window2.title("Форма заполнения")
        window2.geometry('300x200+700+300')
        window2.resizable(False, False)
        window2.configure(background='#BF7F30')
        txt_1 = Entry(window2, width=20, bg='#BF9930')
        txt_1.grid(row=5, column=2)
        now = datetime.datetime.now()
        k = (now.strftime("%Y-%m-%d %H:%M"))
        with connection.cursor() as cursor:
            prof = f"SELECT "
            cursor.execute(prof)
            profs = cursor.fetchall()
            for i in profs:
                doljnosti = [i['id_dolj']]

        combobox = ttk.Combobox(values=doljnosti)
        combobox.place()
        txt_3 = Entry(window2, width=20, bg='#BF9930')
        txt_3.grid(row=8, column=2)
        txt_5 = Entry(window2, width=20, bg='#BF9930')
        txt_5.grid(row=9, column=2)
        txt_6 = Entry(window2, width=20, bg='#BF9930')
        txt_6.grid(row=10, column=2)
        lbl_one1 = Label(window2, text='ФИО',bg='#BF7F30').grid(row=5, column=1)
        lbl_one2 = Label(window2, text='Должность',bg='#BF7F30').grid(row=7, column=1)
        lbl_one3 = Label(window2, text='Актуальность',bg='#BF7F30').grid(row=8, column=1)
        lbl_one4 = Label(window2, text='Профессия',bg='#BF7F30').grid(row=9, column=1)
        lbl_one4 = Label(window2, text='Образование',bg='#BF7F30').grid(row=10, column=1)
        lbl_one5 = Label(window2, text='Уровень владения ПК', bg='#BF7F30').grid(row=10, column=1)


        def zapolnenie2():
            with connection.cursor() as cursor:
                fior = txt_1.get()
                loginr = txt_2.get()
                passwordr = txt_3.get()
                numberphoner = txt_4.get()
                emailr = txt_5.get()
                passportr = txt_6.get()

                if fior == '' or loginr == '' or passwordr == '' or numberphoner == '' or emailr == '' or passportr == '':
                    msg = "Поля не заполнены"
                    mb.showerror("Ошибка", msg)
                else:
                    sqll = f"SELECT * FROM `users`"
                    cursor.execute(sqll)
                    ress = cursor.fetchall()
                    for i in ress:
                        loginsr = i['login']
                        print(loginsr)
                        if loginsr == loginr:
                            msg = "Данный логин уже существует!"
                            mb.showerror("Ошибка", msg)
                    if len(password) < 8:
                        msg = "Невозможный пароль!"
                        mb.showerror("Ошибка", msg)
                    if len(password) >= 8:
                            vak = f"INSERT INTO `users` (FIO,login,password,email,phone,passport) VALUES ('{fior}','{loginr}','{passwordr}','{numberphoner}','{emailr}','{passportr}')"
                            cursor.execute(vak)
                            connection.commit()
                            msg = "Вакансия отправлена!"

                            mb.showinfo("Информация", msg)
                            window2.destroy()


        btn_reg = Button(window2, text='Отправить', command=zapolnenie2,bg='#BF9930').grid(row=12, column=2)
        window2.mainloop()

root1 = Tk()
root1.title("Форма для вакансии")
root1.geometry('300x200+700+300')
root1.resizable(False, False)
root1.configure(background='#BF7F30')
# Лейблы
# lbl_one0 = Label(root1, text='Логин',bg='#BF7F30').grid(row=6, column=5)
# lbl_one1 = Label(root1, text='Пароль',bg='#BF7F30').grid(row=8, column=5)
# # Поля для ввода
# txt_one = Entry(root1, width=20, bg='#BF9930')
# txt_one.grid(row=7, column=5)
# txt_two = Entry(root1, width=20, bg='#BF9930')
# txt_two.grid(row=9, column=5)
# Поля для ввода
# Кнопки
btn_reg = Button(text='Заполнить заявку', command=zapolnenie, bg='#BF9930')
btn_reg.place(x=90, y=75)
# Кнопки
# таблица
root1.mainloop()