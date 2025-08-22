a = (True, False) * 2
print(a)

b = sum(a) == len(a) / 2
print(b)

c = all(a) or any(a) and not b
print(c)
