from math import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2


circle = Circle(5)
print(f"{circle.area() = :.2f} square units")
