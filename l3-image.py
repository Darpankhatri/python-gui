import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
photo = tk.PhotoImage(file="img1.png")

img_label = tk.Label(image=photo)
img_label.pack()

# for other formate image
image = Image.open("img.jpeg")
photo1 = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo1)
img_label.pack()

window.mainloop()