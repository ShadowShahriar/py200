import customtkinter as ctk
from winhdef import path, __script_dir

root = ctk.CTk()
font = path.join(__script_dir, "assets", "font.ttf")
ctk.FontManager.load_font(font)

label = ctk.CTkLabel(root, text="Custom Font Example", font=("Action Jackson", 30))
label.grid(padx=70, pady=50)

root.mainloop()
