import tkinter as tk

window = tk.Tk()

# width x height
window.geometry("444x224")
window.minsize(200,100) # min 
window.maxsize(500,300) # max

heading1 = tk.Label(text="Heading")
heading1.pack()

window.mainloop()