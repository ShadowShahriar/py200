d = {"a": 1}
k = d.keys()
print(list(k))

d["b"] = 2
d["a"] = 0
print(list(k))
