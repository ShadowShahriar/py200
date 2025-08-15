people: list[str] = ["Tushan", "Kaniz", "Shahriar", "Dolon", "Amrin"]
long_names: list[str] = [p for p in people if len(p) > 7]
print(f"Long names: {long_names}")
