import tkinter as tk 


window = tk.Tk()

title = tk.Label(master=window, text='Enter your data')

first_name_lbl = tk.Label(master=window, text='first_name : ')
last_name_lbl = tk.Label(master=window, text='last_name : ')

first_name_ent = tk.Entry(master=window)
last_name_ent = tk.Entry(master=window)

btn = tk.Button(master=window, text='submit')

title.grid(row=0, column=0, columnspan=2, sticky='ew')

first_name_lbl.grid(row=1, column=0)
first_name_ent.grid(row=1, column=1)
last_name_lbl.grid(row=2, column=0)
last_name_ent.grid(row=2, column=1)

btn.grid(row=3, column=1, sticky='we')

window.mainloop()

