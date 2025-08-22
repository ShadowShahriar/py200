class Car:
    def __init__(self, model, color) -> None:
        self.model: str = model
        self.color: str = color

    def display(self) -> None:
        print(f"Model: {self.model}, Color: {self.color}")


car1 = Car("Toyota", "Red")
car1.display()

car2 = Car("Volkswagen", "Black")
car2.display()
