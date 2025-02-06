import tkinter as tk 


window = tk.Tk()

text_var = tk.StringVar()

entry = tk.Entry(master=window, textvariable=text_var)
label = tk.Label(master=window, textvariable=text_var)

entry.pack()
label.pack()

window.mainloop()
