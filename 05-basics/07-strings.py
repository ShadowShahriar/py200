course: str = "software development project"
message: str = """
15 Aug 2025

Dear friend,
It's been a while... Wanna hang out and grab pizza sometime?

Yours,
"""

first: str = "Shayan"
last: str = "Shahriar"
full: str = f"{first} {last}"

print(course.upper())
print(course.lower())
print(course.title())
print(course.title().swapcase())

print(f'{course.find("dev") = }')
print(f'{course.index("dev") = }')
print(f'{course.replace("dev", "ved") = }')
print(f'{"dev" in course = }')
print(f'{"meme" not in course = }')
print(f"{len(course) = }")

print(f"{course[0] = }")
print(f"{course[-1] = }")
print(f"{course[0:4] = }")
print(f"{course[:4] = }")
print(f"{course[4:] = }")
print(f"{course[:] = }")

print("")
print(message.strip())
print(full)
print("*" * 10)
