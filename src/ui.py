from tkinter import *
from tkinter import ttk, messagebox
from functions import registr, menu_run, select_team

root = Tk()

def label_start():
    label = ttk.Label(root, text='Fan news', font=('Arial', 35), background='#2f2f2f', foreground='white')
    under_label_text = ttk.Label(root, text='Добро пожаловать! Придумайте логин и пароль или введите уже существующий',
         font=('Arial', 13), background='#2f2f2f', foreground='white')
    
    label.pack(expand=True)
    label.place(x=300, y=50)

    under_label_text.pack(expand=True)
    under_label_text.place(x=120, y=140)

def button_click():
    button = Button(root, text="Log in", command=lambda: registr(login_entry, password_entry))
    button.pack()
    button.place(x=360, y=350)

def enty_log():
    global login_entry, password_entry

    label_login = ttk.Label(root, text='Логин', font=('Arial', 12), background="#2f2f2f", foreground='white')
    label_login.place(x=240, y=230)

    label_password = ttk.Label(root, text='Пароль', font=('Arial', 12), background="#2f2f2f", foreground='white')
    label_password.place(x=210, y=280)

    login_entry = ttk.Entry(root, width=20, font=('Arial', 15))
    login_entry.pack()
    login_entry.place(x=300, y=230)

    password_entry = ttk.Entry(root, width=20, font=('Arial', 15), show='*')
    password_entry.pack()
    password_entry.place(x=300, y=280)

def choice_sport():
    global leagues, selected_ligs

    button_choice = ttk.Button(root, text= 'Выбрать', command= choice_button)
    button_choice.place(x= 320, y= 360)
    
    button_skip = ttk.Button(root, text= 'Пропустить', command= menu_run)
    button_skip.place(x= 410, y= 360)

    leagues = {
        'АПЛ': ["Арсенал", "Челси", "Ливерпуль", "Манчестер Сити", "Манчестер Юнайтед"],
        'Ла лига': ["Барселона", "Реал Мадрид", "Атлетико Мадрид", "Севилья"],
        'Бундеслига': ["Бавария", "Боруссия Дортмунд", "Байер Леверкузен", "РБ Лейпциг"]}
    selected_ligs = StringVar()

    style = ttk.Style()
    style.configure('TRadiobutton', font=('Arial', 15), background='#2f2f2f', foreground= 'white')

    header = ttk.Label(root, text="Выберите любимую лигу", font=('Arial', 18), background='#2f2f2f', foreground='white')
    header.place(x=10, y=115)

    y_pos = 160
    for league in leagues:
        lig_btn = ttk.Radiobutton(root, text=league, variable=selected_ligs, value=league)
        lig_btn.place(x=10, y=y_pos)
        y_pos += 30

def choice_button():
    team_frame = ttk.Frame()
    team_frame.pack()

    league = selected_ligs.get()

    for widget in team_frame.winfo_children():
        widget.destroy()

    team_label = ttk.Label(root, team_frame, text="Команды {}".format(league))
    team_label.pack()

    team_listbox = Listbox(root, team_frame, font= ('Arial', 12),
     background= "#2f2f2f", foreground= 'white', width= 30)

    team_listbox.place(x = 350, y = 130)
    team_listbox.pack()

    for team in leagues[league]:
        team_listbox.insert(END, team)

    close_button = ttk.Button(root, team_frame, text="Закрыть", command=team_frame.destroy)
    close_button.pack(side=LEFT, padx=(5, 10), pady=10)

    select_button = ttk.Button(root, team_frame, text="Выбрать", command=lambda: select_team(team_listbox))
    select_button.pack(side=LEFT, padx=(5, 10), pady=10)

def main():
    root.geometry('800x500')
    root.title('Fan News')
    root.attributes("-alpha", 0.90)
    root.configure(bg="#2f2f2f")
    
    label_start()
    button_click()
    enty_log()
    root.mainloop()

if __name__ == "__main__":
    main()