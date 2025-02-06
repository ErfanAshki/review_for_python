import tkinter as tk 


window = tk.Tk()

first_name_lbl = tk.Label(master=window, text='first_name : ')
last_name_lbl = tk.Label(master=window, text='last_name : ')

first_name_ent = tk.Entry(master=window)
last_name_ent = tk.Entry(master=window)

first_name_lbl.grid(row=0, column=0)
first_name_ent.grid(row=0, column=1)
last_name_lbl.grid(row=1, column=0)
last_name_ent.grid(row=1, column=1)

window.mainloop()
