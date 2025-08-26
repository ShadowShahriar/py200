# =======================
# === Normal Function ===
# =======================
def add(x, y):
    return x + y


print(add(2, 3))

# =======================
# === Lambda Function ===
# =======================
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))

# =============================
# === Basic Lambda Function ===
# =============================
square = lambda x: x**2
print(square(4))

# ============================================
# === Lambda Function with Three Arguments ===
# ============================================
multiply = lambda x, y, z: x * y * z
print(multiply(3, 4, 5))

# ================================================
# === Normal Function within Built-in Function ===
# ================================================
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

pairs = [(1, 5), (2, 1), (3, 7), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
