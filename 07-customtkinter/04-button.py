import customtkinter as ctk
import winhdef as wdef
from customtkinter import CTkButton as button

title: str = "Custom Application"

# === set the location of the custom theme file ===
ctk.set_default_color_theme(wdef.__theme_path)

# === set title bar color (light/dark/system) ===
ctk.set_appearance_mode("dark")

root = ctk.CTk()

# === set app title and icon ===
root.title(title)
root.iconbitmap(wdef.__icon_path)

# === set main window size and background color ===
root.config(width=400, height=200)

btn = button(
    master=root,
    text="Hello",
    width=170,
    height=36,
    command=lambda: print("Hello?"),
)

btn.place(relx=0.5, rely=0.5, anchor="center")

# === place the window to the center ===
wdef.center(root)

# === place the window always on top ===
wdef.ontop(root)

root.mainloop()
