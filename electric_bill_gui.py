import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Electricity bill calculator')
window.geometry('200x150+600+100')
window.configure(bg="#F5F5F5")
window.resizable(False, False)

ampere_label = tk.Label(window, text='Select the Ampere:', font=("arial", 12), bg='#F5F5F5', fg='#333333')
ampere_label.place(x=5, y=5)

ampere_value = [5, 15, 30, 60]
option1 = tk.StringVar()

ampere_list = ttk.Combobox(window, values=ampere_value, width=5, textvariable=option1, state = "readonly")
ampere_list.place(x=145, y=5)
ampere_list.current(0)

unit_label = tk.Label(window, text='Enter the unit:', font=("arial", 12), bg='#F5F5F5', fg='#333333')
unit_label.place(x=5, y=50)

unit_entry = tk.Entry(window, width=8)
unit_entry.place(x=105, y=54)

bill_label = tk.Label(window, text='Bill:', font=("arial", 12), bg='#F5F5F5', fg='#333333')
bill_label.place(x=5, y=90)

bill_amount = tk.Label(window, bg='#F5F5F5', fg='#333333')
bill_amount.place(x=60, y=90)

x = 0 

def ampere_5(unit):
    if unit <= 20:
        bill = 30
    elif unit <= 30:
        bill = 110+ (unit-20) * 6.5
    elif unit <= 50:
        bill = 175 + (unit-30) * 8
    elif unit <= 100:
        bill = 360 + (unit-50) * 9.5
    elif unit <= 250:
        bill = 860 + (unit-100) * 9.5
    else:
        bill = 2335 + (unit-250) * 11
    return bill

def ampere_15(unit):
    if unit <= 20:
        bill = 50 + unit * 4
    elif unit <= 30:
        bill = 155+ (unit-20) * 6.5
    elif unit <= 50:
        bill = 220 + (unit-30) * 8
    elif unit <= 100:
        bill = 405 + (unit-50) * 9.5
    elif unit <= 250:
        bill = 905 + (unit-100) * 9.5
    else:
        bill = 2380 + (unit-250) * 11
    return bill

def ampere_30(unit):
    if unit <= 20:
        bill = 75 + unit * 5
    elif unit <= 30:
        bill = 200+ (unit-20) * 6.5
    elif unit <= 50:
        bill = 265 + (unit-30) * 8
    elif unit <= 100:
        bill = 450 + (unit-50) * 9.5
    elif unit <= 250:
        bill = 950 + (unit-100) * 9.5
    else:
        bill = 2425 + (unit-250) * 11
    return bill

def ampere_60(unit):
    if unit <= 20:
        bill = 125 + unit * 6
    elif unit <= 30:
        bill = 245 + (unit-20) * 6.5
    elif unit <= 50:
        bill = 310 + (unit-30) * 8
    elif unit <= 100:
        bill = 495 + (unit-50) * 9.5
    elif unit <= 250:
        bill = 1020 + (unit-100) * 9.5
    else:
        bill = 2495 + (unit-250) * 11
    return bill

def get_bill():
    ampere = int(ampere_list.get())
    unit = int(unit_entry.get())
    if ampere == 5:
        bill = ampere_5(unit)
    elif ampere == 15:
        bill = ampere_15(unit)
    elif ampere == 30:
        bill = ampere_30(unit)
    elif ampere == 60:
        bill = ampere_60(unit)
    else:
        bill = 0
    bill_amount.config(text=bill)

button = tk.Button(window, text="Convert", background="#18b8f2", activebackground="#FEDCBA", command=get_bill, relief="raised", bd=4)
button.place(x=70, y=110)

window.mainloop()
