def upper_everything(items: list[str]) -> list[str]:
    return [item.upper() for item in items]


people: list[str] = ["Tushan", "Kaniz", "Shahriar", "Dolon", "Amrin"]
loud_list: list[str] = upper_everything(people)
print(f"Long names: {loud_list}")
