from tkinter import filedialog as fd

filetypes = (
    ("Text Documents", "*.txt"),
    ("JSON and Text Files", "*.txt *.json"),
    ("All Files", "*.*"),
)

filenames = (
    fd.askopenfilenames(
        title="Choose multiple files",
        initialdir="C:/Windows/System32",
        filetypes=filetypes,
    )
    or ()
)

print(filenames)
print(len(filenames))
