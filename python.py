import tkinter as tk 
from tkinter import W, E, N, S


window = tk.Tk()

title = tk.Label(master=window, text='Enter your data')

first_name_lbl = tk.Label(master=window, text='first_name : ',width=15, height=2)
last_name_lbl = tk.Label(master=window, text='last_name : ',width=10, height=4)
age_lbl = tk.Label(master=window, text='age : ',width=10, height=6)

first_name_ent = tk.Entry(master=window, width=10)
last_name_ent = tk.Entry(master=window, width=20)
age_ent = tk.Entry(master=window, width=30)

btn = tk.Button(master=window, text='submit')

title.grid(row=0, column=0, columnspan=2, sticky='ew')

first_name_lbl.grid(row=1, column=0)
first_name_ent.grid(row=1, column=1, sticky=(N,S))
last_name_lbl.grid(row=2, column=0)
last_name_ent.grid(row=2, column=1)
age_lbl.grid(row=3, column=0, sticky=(W,))
age_ent.grid(row=3, column=1, sticky='ns')

btn.grid(row=4, column=0,columnspan=2, sticky=(W,E))

window.mainloop()

