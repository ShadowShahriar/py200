from tkinter import filedialog as fd

filetypes = (
    ("Text Documents", "*.txt"),
    ("JSON and Text Files", "*.txt *.json"),
    ("All Files", "*.*"),
)

d: str = (
    fd.asksaveasfilename(
        title="Save file as...",
        initialdir="C:/",
        confirmoverwrite=True,
        initialfile="shayan",
        filetypes=filetypes,
    )
    or "None"
)

print(d)
