import customtkinter as ctk
import winhdef as wdef

title: str = "Custom Application"
background: str = "#f0f0f0"

# === set title bar color (light/dark/system) ===
ctk.set_appearance_mode("light")

root = ctk.CTk(fg_color=background)

# === set app title and icon ===
root.title(title)
root.iconbitmap(wdef.__icon_path)

# === set main window size and background color ===
root.config(width=400, height=200, background=background)

# === make the window semi-transparent when not in focus ===
wdef.shy(root)

# === place the window to the center ===
wdef.center(root)

# === place the window always on top ===
wdef.ontop(root)

root.mainloop()
