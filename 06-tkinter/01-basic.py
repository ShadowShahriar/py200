import tkinter as tk
import os.path as path
import sys

script_path = path.abspath(__file__)
script_dir = path.dirname(script_path)
icon_path = path.join(script_dir, "favicon.ico")

print(script_dir)
print(sys.path[0])


def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")


root = tk.Tk()
root.title("Basic Application")
root.iconbitmap(icon_path)
root.config(width=400, height=200, background="#090b10")

root.lift()
root.attributes("-topmost", True)

center_window(root)

root.mainloop()
