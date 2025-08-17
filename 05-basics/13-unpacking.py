# =======================
# === basic unpacking ===
# =======================
a, b, c = [1, 2, 3]
print(f"{a = }, {b = }, {c = }")

# =======================
# === ignoring values ===
# =======================
a, _, c = [6, 7, 8]
print(f"{a = }, {c = }")

# ==========================
# === extended unpacking ===
# ==========================
a, b, *c = [1, 2, 3, 4, 5]
print(f"{a = }, {b = }, {c = }")

a, *b, c = [1, 2, 3, 4, 5]
print(f"{a = }, {b = }, {c = }\n")

# ===================================
# === unpacking nested structures ===
# ===================================
data = ("Shahriar", (21, "Stoopid"))
name, (age, profession) = data
print(f"{name = }")
print(f"{age = }")
print(f"{profession = }\n")

# ==========================================
# === unpacking lists and combining them ===
# ==========================================
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(f"{list3 = }")

# ==========================================
# === unpacking dicts and combining them ===
# ==========================================
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print(f"{dict3 = }\n")

# ======================================
# === swap variables using unpacking ===
# ======================================
k = 932
s = 503
print(f"Before: {k = }, {s = }")
k, s = s, k
print(f"After : {k = }, {s = }")


# ====================================
# === unpacking function arguments ===
# ====================================
def print_names(*names):
    for name in names:
        print(name)


print_names("Shahriar", "Tushan", "Kaniz", "Dolon", "Amrin")
