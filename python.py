import tkinter as tk 


window = tk.Tk()

def print_something():
    print('something')


btn = tk.Button(master=window, text='click me !', command=print_something)

btn.pack()

window.mainloop()
