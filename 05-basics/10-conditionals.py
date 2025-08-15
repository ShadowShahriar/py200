temp: int = 35

if temp > 30:
    print("Too hot")
    print("Drink water")
else:
    print("Cold")

print("")

age: int = 21
message: str = ""

if age >= 30:
    message = "Old"
elif age >= 18:
    message = "Adult"
else:
    message = "Toddler"
print(message)

responsibility: str = "Responsible" if age >= 18 else "Freebird"
print(responsibility)

print("")

high_income = True
good_credit = True
student = False

if (high_income and good_credit) and not student:
    print("No probation needed")

if high_income and good_credit:
    print("Promotion confirmed")
elif high_income or good_credit:
    print("Can be promoted")
else:
    print("Might get fired")

print("")

if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")
