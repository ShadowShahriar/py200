import customtkinter as ctk
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


root = ctk.CTk()
root.minsize(width=200, height=200)
root.maxsize(width=550, height=550)
root.title("Custom Application")
root.iconbitmap(icon_path)

root.config(width=400, height=200, background="#090b10")

root.lift()
root.attributes("-topmost", True)


def handle_focus_in(event):
    if event.widget == root:
        root.attributes("-alpha", 1)


def handle_focus_out(event):
    if event.widget == root:
        root.attributes("-alpha", 0.5)


root.bind("<FocusOut>", handle_focus_out)
root.bind("<FocusIn>", handle_focus_in)

center_window(root)

root.mainloop()
