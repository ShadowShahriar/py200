class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)

result = p1 + p2
print(result.x, result.y)

result = p1 - p2
print(result.x, result.y)

result = p1 * p2
print(result.x, result.y)

result = p1 / p2
print(result.x, result.y)
