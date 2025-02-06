import tkinter as tk 


window = tk.Tk()

text1 = tk.Label(master=window, text='hello world')
text2 = tk.Label(master=window, text='bye world')

text1.pack()
text2.pack()

window.mainloop()
