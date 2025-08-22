def even_or_odd():
    print("Even or Odd Checker")
    while 1:
        try:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print(f"✅ {num} is Even")
            else:
                print(f"✅ {num} is Odd")
        except ValueError:
            print("⛔ Not a valid number")
        print("")

        again = input("Check again? (y/n): ").lower()
        if again != "y":
            print("Aight, bye!")
            break


even_or_odd()
