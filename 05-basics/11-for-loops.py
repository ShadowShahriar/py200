# === iterating through a list (array) ===
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("")

# === iterating through a string ===
for char in "Python":
    print(char)

print("")

# === iterating from 0 to 4 ===
for i in range(5):
    print(i)

print("")

# === iterating through a specific range (start, end, step) ===
for i in range(2, 10, 2):  # iterates 2, 4, 6, 8
    print(i)

print("")

# === stop the iteration once a condition is satisfied ===
for i in range(10):
    if i == 5:
        break
    print(i)

print("")

# === skips the current iteration and proceeds to the next one ===
for i in range(5):
    if i == 2:
        continue
    print(i)

print("")

# === anotate if the loop was finished normally ===
for i in range(3):
    print(i)
else:
    print("Loop finished normally.")
