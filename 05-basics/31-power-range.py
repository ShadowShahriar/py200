n = 5
m = True
for i in range(n):
    m = m ^ i & 1
print(m)
