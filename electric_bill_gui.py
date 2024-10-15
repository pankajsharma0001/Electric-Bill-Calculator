import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Electricity Bill Calculator')
window.geometry('300x200+600+100')  # Increased size
window.configure(bg="#E8F0F2")  # Lighter background color for a fresh look
window.resizable(False, False)

# Ampere selection
ampere_label = tk.Label(window, text='Select Ampere:', font=("Arial", 12, "bold"), bg='#E8F0F2', fg='#333333')
ampere_label.place(x=20, y=20)

ampere_value = [5, 15, 30, 60]
option1 = tk.StringVar()

ampere_list = ttk.Combobox(window, values=ampere_value, width=5, textvariable=option1, state="readonly", font=("Arial", 10))
ampere_list.place(x=150, y=22)
ampere_list.current(0)

# Unit entry
unit_label = tk.Label(window, text='Enter Unit:', font=("Arial", 12, "bold"), bg='#E8F0F2', fg='#333333')
unit_label.place(x=20, y=65)

unit_entry = tk.Entry(window, width=10, font=("Arial", 10))
unit_entry.place(x=150, y=68)

# Bill label
bill_label = tk.Label(window, text='Total Bill:', font=("Arial", 12, "bold"), bg='#E8F0F2', fg='#333333')
bill_label.place(x=20, y=110)

bill_amount = tk.Label(window, text='0.00', font=("Arial", 12), bg='#E8F0F2', fg='#d9534f')
bill_amount.place(x=150, y=110)

# Calculate bill based on ampere selection
def ampere_5(unit):
    if unit <= 20:
        bill = 30
    elif unit <= 30:
        bill = 110 + (unit-20) * 6.5
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
        bill = 155 + (unit-20) * 6.5
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
        bill = 200 + (unit-20) * 6.5
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

# Function to calculate bill based on ampere and unit input
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
    bill_amount.config(text=f'{bill:.2f}')

# Convert button
button = tk.Button(window, text="Calculate", font=("Arial", 10, "bold"), background="#28A745", 
                   activebackground="#218838", foreground="#ffffff", command=get_bill, relief="raised", bd=4)
button.place(x=100, y=150)

# Bind the Enter key to trigger the get_bill function
window.bind('<Return>', lambda event: get_bill())

window.mainloop()
