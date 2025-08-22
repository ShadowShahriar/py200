class Bird:
    def fly(self) -> None:
        print("Birds can fly")


class Penguin(Bird):
    def fly(self) -> None:
        print("Penguins cannot fly")


bird = Bird()
bird.fly()

penguin = Penguin()
penguin.fly()
