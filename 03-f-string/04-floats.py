n: float = 1234.56789

# print the actual floating point number
print(n)

# print only two floating decimals
print(round(n, 2))

# print only two floating decimals (with f-string)
print(f"{n:.2f}")

# print the floating point number rounded to the closest integer
print(f"{n:.0f}")

# print only two floating decimals in combination with the thousand separator
print(f"{n:,.3f}")
