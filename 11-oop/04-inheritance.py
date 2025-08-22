class Animal:
    def sound(self) -> str:
        return "(Inaudible)"


class Dog(Animal):
    def sound(self) -> str:
        return "Vau!"


anim = Animal()
print(f"{anim.sound() = }")

dawg = Dog()
print(f"{dawg.sound() = }")
