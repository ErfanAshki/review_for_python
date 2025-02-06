import tkinter as tk 


window = tk.Tk()

lbl = tk.Label(master=window, text='')
eny = tk.Entry(master=window)

def show_entry_in_label():
    lbl['text'] = eny.get()

btn = tk.Button(master=window, text='click me !', command=show_entry_in_label)

eny.pack()
btn.pack()
lbl.pack()

window.mainloop()
