import tkinter.messagebox as messagebox
import dbFan as db
from tkinter import *
from ui import *


def registr(login_entry, password_entry):
    global root
    global username
    username = login_entry.get()
    password = password_entry.get()
    if username and password:
        try:
            stored_password = db.check_password(username)
            if stored_password is not None:
                if password == stored_password:
                    messagebox.showinfo("Успех", "Вы вошли в свой аккаунт!")
                    app_run()
                else:
                    messagebox.showerror('Ошибка', 'Неверный пароль')
            else:
                if db.check_username(username):
                    messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует')
                else:
                    db.add_user(username, password)
                    messagebox.showinfo("Успех", "Регистрация прошла успешно!")
                    app_run()
        except Exception as e:
            messagebox.showerror('Ошибка', f'Ошибка регистрации{e}')
            print(e)
    else:
        messagebox.showwarning("Ошибка", "Заполните все поля!")

def app_run():
    global root
    for widget in root.winfo_children():
        widget.destroy()
    label_start()
    choice_sport()

def select_team(team_listbox):
    selected_team = team_listbox.curselection()
    if selected_team:
        team_name = team_listbox.get(selected_team)
        db.add_teams(username, team_name)
        messagebox.showinfo("Выбор команды", f"Вы выбрали команду: {team_name}")
        menu_run()
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, выберите команду!")

def menu_run():
    global root
    for widget in root.winfo_children():
            widget.destroy()
    root.option_add("*tearOff", FALSE)
    main_menu = Menu(root)
 
    file_menu = Menu(background='#2f2f2f', foreground= 'white', font= ('Arial', 10))
    file_menu.add_command(label="Профиль")
    file_menu.add_command(label="Команды")
    file_menu.add_separator()
    file_menu.add_command(label="Выйти")
    
    main_menu.add_cascade(label="Мой аккаунт", menu=file_menu)
    main_menu.add_cascade(label="Новости")
    main_menu.add_cascade(label="Турниры")
    
    root.config(menu=main_menu)