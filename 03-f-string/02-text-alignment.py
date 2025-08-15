text: str = "Header"
fill: str = "-"
spaces: int = 40

print(f"|{text:<{spaces}}|")  # align text to the left (add spaces to the right)
print(f"|{text:^{spaces}}|")  # align text to the center (add spaces in both directions)
print(f"|{text:>{spaces}}|")  # align text to the right (add spaces to the left)

print("")

print(f"|{text:{fill}<{spaces}}|")
print(f"|{text:{fill}^{spaces}}|")
print(f"|{text:{fill}>{spaces}}|")
