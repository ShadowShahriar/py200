from hdef import path, __script_dir as __dir
import tkinter as tk
import pygame

root = tk.Tk()
root.title("SFX Example")
root.geometry("300x100+50+50")

pygame.mixer.init()

sfx_click = pygame.mixer.Sound(path.join(__dir, "assets", "click.ogg"))
sfx_click.set_volume(0.4)

btn = tk.Button(
    root,
    text="Click Me!",
    command=lambda: sfx_click.play(),
    font=("Arial", 16),
)
btn.pack(pady=20, padx=20)
root.mainloop()
