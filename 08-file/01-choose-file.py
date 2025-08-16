import filedialpy

f = filedialpy.openFile(
    initial_dir="C:\\Windows\\System32",
    initial_file="hello.txt",
    title="Choose a file",
    filter=["*.txt *.json", "*.txt", "*.json"],
)

print(f or "None")
