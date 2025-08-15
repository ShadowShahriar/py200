import math

PI = math.pi

print(f"{10 + 3 = }")
print(f"{10 - 3 = }")
print(f"{10 * 3 = }")
print(f"{10 / 3 = }")
print(f"{10 // 3 = }")
print(f"{10 % 3 = }")
print(f"{10 ** 3 = }")

print("")
print(round(2.77))
print(abs(-4.5))

print("")
print(math.ceil(2.2))
print(math.floor(2.2))
print(math.factorial(4))


# convert degrees to radians
def rads(d: float) -> float:
    return d * (PI / 180)


print("")
print(math.sin(rads(45)))
print(math.cos(rads(180)))
