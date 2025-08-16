from tkinter.colorchooser import askcolor

colors = askcolor(title="Color Picker", initialcolor="blue")
print(colors[1])
