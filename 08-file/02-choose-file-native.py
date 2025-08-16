from tkinter import filedialog as fd

filetypes = (
    ("Text Documents", "*.txt"),
    ("JSON and Text Files", "*.txt *.json"),
    ("All Files", "*.*"),
)

filename = fd.askopenfilename(
    title="Choose a file", initialdir="C:/Windows/System32", filetypes=filetypes
)

print(filename or "None")
