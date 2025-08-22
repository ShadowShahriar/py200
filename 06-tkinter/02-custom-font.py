import tkinter as tk
from tkextrafont import Font

import os.path as path
import sys

script_path = path.abspath(__file__)
script_dir = path.dirname(script_path)
font_path = path.join(script_dir, "assets", "font.ttf")

window = tk.Tk()
font = Font(file=font_path, size=24, family="Action Jackson")

label = tk.Label(window, text="Custom Font Example", font=font)
label.pack()

window.mainloop()
