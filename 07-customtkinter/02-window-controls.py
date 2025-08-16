import customtkinter as ctk
import winhdef as wdef

title: str = "Custom Application"
background: str = "#090b10"

root = ctk.CTk()
root.title(title)
root.iconbitmap(wdef.__icon_path)
root.config(width=400, height=200, background=background)

root.minsize(width=200, height=200)
root.maxsize(width=550, height=550)
root.resizable(False, False)

wdef.center(root)
wdef.ontop(root)

root.mainloop()
