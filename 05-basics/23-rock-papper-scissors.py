from random import choice


def rock_paper_scissors():
    print("🎮 Rock-Paper-Scissors")
    choices = ["rock", "paper", "scissors"]

    while 1:
        user = input("Choose rock, paper, or scissors (type 'q' to quit):\n> ").lower()
        if user == "q":
            print("Aight, bye!")
            break
        if user not in choices:
            print("⛔ Invalid choice")
            print("")
            continue

        pc = choice(choices)
        print("")
        print(f"🤖 Computer chose: {pc}")

        if user == pc:
            print("😑 It's a tie")
        elif (
            (user == "rock" and pc == "scissors")
            or (user == "paper" and pc == "rock")
            or (user == "scissors" and pc == "paper")
        ):
            print("😀 You won!")
        else:
            print("💀 Huh, loser")
        print("")


rock_paper_scissors()
