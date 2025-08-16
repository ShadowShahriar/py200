from tkinter import filedialog as fd

d: str = fd.askdirectory(
    title="Choose a directory", initialdir="C:/Windows/System32", mustexist=True
)

print(d)
