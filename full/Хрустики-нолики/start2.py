import random
from tkinter import *  # підключаємо модуль tkinter
from tkinter import messagebox  # діалогові вікна

player1 = []
player2 = []

win_chrest = 0
win_zeros = 0
draw = 0

game_steps = 0

active_pl = 1

window = Tk()  # створення вікна

window.title("Хрестики-нулики")  # заголовок
window.geometry("470x600")
window.resizable(False, False)


def iswinner():
    global win_chrest
    global win_zeros
    global draw

    global player1
    global player2

    winner = 0

    if (1 in player1) and (2 in player1) and (3 in player1):
        winner = 1
    elif (1 in player2) and (2 in player2) and (3 in player2):
        winner = 2

    elif (4 in player1) and (5 in player1) and (6 in player1):
        winner = 1
    elif (4 in player2) and (5 in player2) and (6 in player2):
        winner = 2

    elif (7 in player1) and (8 in player1) and (9 in player1):
        winner = 1
    elif (7 in player2) and (8 in player2) and (9 in player2):
        winner = 2

    elif (1 in player1) and (5 in player1) and (9 in player1):
        winner = 1
    elif (1 in player2) and (5 in player2) and (9 in player2):
        winner = 2

    elif (3 in player1) and (5 in player1) and (7 in player1):
        winner = 1
    elif (3 in player2) and (5 in player2) and (7 in player2):
        winner = 2

    elif (1 in player1) and (4 in player1) and (7 in player1):
        winner = 1
    elif (1 in player2) and (4 in player2) and (7 in player2):
        winner = 2

    elif (2 in player1) and (5 in player1) and (8 in player1):
        winner = 1
    elif (2 in player2) and (5 in player2) and (8 in player2):
        winner = 2

    elif (3 in player1) and (6 in player1) and (9 in player1):
        winner = 1
    elif (3 in player2) and (6 in player2) and (9 in player2):
        winner = 2

    if winner == 1:
        win_chrest += 1
        clear_()
        update_scoreboard()
    elif winner == 2:
        win_zeros += 1
        clear_()
        update_scoreboard()
    elif winner == 0 and game_steps == 9:
        draw += 1
        clear_()
        update_scoreboard()


def update_scoreboard():
    label1.config(text=f'Виграв нулик: {win_zeros}')
    label2.config(text=f'Виграв хрестик: {win_chrest}')
    label3.config(text=f'Нічия: {draw}')


def buttonClick(id):
    global player1
    global player2
    global game_steps
    global active_pl

    game_steps += 1
    if active_pl == 1:
        player1.append(id)
        active_pl = 2

        if id == 1:
            button1.config(text='X', state=DISABLED)
        elif id == 2:
            button2.config(text='X', state=DISABLED)
        elif id == 3:
            button3.config(text='X', state=DISABLED)
        elif id == 4:
            button4.config(text='X', state=DISABLED)
        elif id == 5:
            button5.config(text='X', state=DISABLED)
        elif id == 6:
            button6.config(text='X', state=DISABLED)
        elif id == 7:
            button7.config(text='X', state=DISABLED)
        elif id == 8:
            button8.config(text='X', state=DISABLED)
        elif id == 9:
            button9.config(text='X', state=DISABLED)

    elif active_pl == 2:
        player2.append(id)
        active_pl = 1

        if id == 1:
            button1.config(text='O', state=DISABLED)
        elif id == 2:
            button2.config(text='O', state=DISABLED)
        elif id == 3:
            button3.config(text='O', state=DISABLED)
        elif id == 4:
            button4.config(text='O', state=DISABLED)
        elif id == 5:
            button5.config(text='O', state=DISABLED)
        elif id == 6:
            button6.config(text='O', state=DISABLED)
        elif id == 7:
            button7.config(text='O', state=DISABLED)
        elif id == 8:
            button8.config(text='O', state=DISABLED)
        elif id == 9:
            button9.config(text='O', state=DISABLED)

    iswinner()


button1 = Button(window, text='__')  # кнопка
button1.grid(row=0, column=0, ipadx=40, ipady=40, sticky="snew")
button1.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(1))

button2 = Button(window, text='__')  # кнопка
button2.grid(row=0, column=1, ipadx=40, ipady=40, sticky="snew")
button2.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(2))

button3 = Button(window, text='__')  # кнопка
button3.grid(row=0, column=2, ipadx=40, ipady=40, sticky="snew")
button3.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(3))

button4 = Button(window, text='__')  # кнопка
button4.grid(row=1, column=0, ipadx=40, ipady=40, sticky="snew")
button4.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(4))

button5 = Button(window, text='__')  # кнопка
button5.grid(row=1, column=1, ipadx=40, ipady=40, sticky="snew")
button5.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(5))

button6 = Button(window, text='__')  # кнопка
button6.grid(row=1, column=2, ipadx=40, ipady=40, sticky="snew")
button6.config(bg='#e3e3e3', fg='#4286969697f5', font=('Arial', 30, "bold"), command=lambda: buttonClick(6))

button7 = Button(window, text='__')  # кнопка
button7.grid(row=2, column=0, ipadx=40, ipady=40, sticky="snew")
button7.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(7))

button8 = Button(window, text='__')  # кнопка
button8.grid(row=2, column=1, ipadx=40, ipady=40, sticky="snew")
button8.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(8))

button9 = Button(window, text='__')  # кнопка
button9.grid(row=2, column=2, ipadx=40, ipady=40, sticky="snew")
button9.config(bg='#e3e3e3', fg='#696969', font=('Arial', 30, "bold"), command=lambda: buttonClick(9))

label1 = Label(window)
label1.config(text=f'Виграв нулик: {win_zeros}', bg='#ffffff', fg='#000000', font='Arial, 15')
label1.grid()

label2 = Label(window)
label2.config(text=f'Виграв хрестик: {win_chrest}', bg='#ffffff', fg='#000000', font='Arial, 15')
label2.grid()

label3 = Label(window)
label3.config(text=f'Нічия: {draw}', bg='#ffffff', fg='#000000', font='Arial, 15')
label3.grid()


def clear_():
    global player1
    global player2
    global game_steps
    global active_pl

    player1 = []
    player2 = []
    game_steps = 0
    active_pl = 1

    button1.config(text='__', state=NORMAL)
    button2.config(text='__', state=NORMAL)
    button3.config(text='__', state=NORMAL)
    button4.config(text='__', state=NORMAL)
    button5.config(text='__', state=NORMAL)
    button6.config(text='__', state=NORMAL)
    button7.config(text='__', state=NORMAL)
    button8.config(text='__', state=NORMAL)
    button9.config(text='__', state=NORMAL)


window.mainloop()  # зациклення затримки вікна