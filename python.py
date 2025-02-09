import tkinter as tk 
from tkinter import W, E, N, S


window = tk.Tk()

fah_lbl = tk.Label(master=window, text='fahrenheit')
cel_lbl = tk.Label(master=window, text='celsius')
result_lbl = tk.Label(master=window, text='Result will be displayed here')

fah_ent = tk.Entry(master=window)

calc_btn = tk.Button(master=window, text='calc')

fah_lbl.grid(row=0, column=0)
cel_lbl.grid(row=1, column=0)
result_lbl.grid(row=1, column=1)

fah_ent.grid(row=0, column=1)

calc_btn.grid(row=0, column=2)


window.mainloop()

