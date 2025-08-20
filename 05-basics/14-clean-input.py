def ask_dolon():
    print("Dolon, ajke ki class hobe? :3")


def ask_tushan():
    print("Bro, ajke class ache?")


match input("Kare ask korba? "):
    case "Dolon":
        ask_dolon()
    case "Tushan":
        ask_tushan()
    case _:
        print("Class hok ba na hok, ami varsity jaitesi")
