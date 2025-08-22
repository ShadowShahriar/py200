from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


rect = Rectangle(4, 5)
print(f"{rect.area() = }")
