import tkinter as tk 


window = tk.Tk()

text_var = tk.StringVar()

entry = tk.Entry(master=window, textvariable=text_var)
label = tk.Label(master=window, textvariable=text_var)

lb = tk.Label(master=window, text='hi')
lbl = tk.Label(master=window, text='kha')

entry.pack(side=tk.BOTTOM)
label.pack(side=tk.TOP)
lb.pack(side=tk.RIGHT)
lbl.pack(side=tk.LEFT)

window.mainloop()
