count: int = 1024
rating: float = 4.95
active: bool = True
course: str = "Software Development Project"
people: list[str] = ["Tushan", "Kaniz", "Shahriar", "Dolon", "Amrin"]
cgpa: list[float] = [4.00, 3.98, 3.55, 3.9, 3.9]
json: dict[str, str] = {"name": "Shahriar", "role": "Artist"}

print(count)
print(type(count))

print("")
print(rating)
print(type(rating))

print("")
print(active)
print(type(active))

print("")
print(course)
print(type(course))

print("")
print(people)
print(type(people))

print("")
print(cgpa)
print(type(cgpa))

print("")
print(json)
print(type(json))
