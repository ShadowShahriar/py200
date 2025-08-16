import filedialpy

f = (
    filedialpy.openFiles(
        initial_dir="C:\\Windows\\System32",
        initial_file="hello.txt",
        title="Choose multiple files",
        filter=["*.txt *.json", "*.txt", "*.json"],
    )
    or []
)

print(f)
print(len(f))
