import tkinter as tk 
from tkinter import W, E, N, S


window = tk.Tk()

fah_lbl = tk.Label(master=window, text='fahrenheit : ')
cel_lbl = tk.Label(master=window, text='celsius : ')
result_lbl = tk.Label(master=window, text='Result will be displayed here')

fah_ent = tk.Entry(master=window, width=30)

calc_btn = tk.Button(master=window, text='calc')

fah_lbl.grid(row=0, column=0, padx=10, pady=(10,20))
fah_ent.grid(row=0, column=1, pady=(10,20))
calc_btn.grid(row=0, column=2, padx=10, pady=(10,20))

cel_lbl.grid(row=1, column=0, padx=10, pady=(5,20))

result_lbl.grid(row=1, column=1, pady=(5,20))



window.mainloop()

