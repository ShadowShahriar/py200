balance: float = 5.00
amount = 0
wrong = False

while 1:
    try:
        amount = float(input("Send money to bKash: "))
        break
    except ValueError:
        wrong = True
        print("Not a valid amount of money. Please try again\n")

balance += amount

if not wrong:
    print("")

print("Thank you! :3")
print(f"Current {balance = }")
