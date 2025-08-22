from random import randint


def roll_dice():
    print("🎲 Dice Roller")
    while 1:
        try:
            dice = int(input("How many dice do you wanna roll? (1-6): "))
            if dice < 1 or dice > 6:
                print("⛔ Choose between 1 to 6")
                continue
            results = [randint(1, 6) for _ in range(dice)]
            print(f"You rolled: {results}")

        except ValueError:
            print("⛔ Not a valid number")

        print("")
        again = input("Roll again? (y/n): ").lower()
        if again != "y":
            print("Aight, bye!")
            break


roll_dice()
