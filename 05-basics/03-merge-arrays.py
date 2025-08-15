def merge_arrays(A, B) -> list:
    # merge two arrays A and B
    # remove any duplicates
    # sort the list in ascending order
    return sorted(set(A + B))


A = ["Tushan", "Kaniz"]
B = ["Shahriar", "Tushan"]
C = merge_arrays(A, B)
print(C)
