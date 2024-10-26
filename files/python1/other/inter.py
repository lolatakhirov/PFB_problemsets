#!/Users/pfb2024/mamba/envs/projects/bin/python3
import ttkbootstrap as ttkb
import tkinter as tk
from PIL import Image, ImageTk

parent = tk.Tk()
parent.title("Image in Tkinter")
image = Image.open("0537dce4-11e0-4f4a-ac90-b6091888af10.jpeg")
image = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image = image)


overlay_frame = tk.Frame(parent, bg='gray93', bd=0)
overlay_frame.place(relx=0.5, rely=0.2, anchor='center')

entry = tk.Entry(overlay_frame)
button = tk.Button(overlay_frame, text = "Click me to begin!")
label = tk.Label(overlay_frame, text = "Welcome! You are on the right path to finding your bestie! ")
label2 = tk.Label(overlay_frame, text = "Please enter your name in the box")
label.pack()
label2.pack()
entry.pack()
button.pack()
image_label.pack()
parent.mainloop()
