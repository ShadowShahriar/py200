class Book:
    def __init__(self, pages) -> None:
        self.pages = pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages


book1 = Book(154)
book2 = Book(122)
print(f"{book1 >  book2 = }")
print(f"{book1 <  book2 = }")
print(f"{book1 >= book2 = }")
print(f"{book1 <= book2 = }")
print(f"{book1 == book2 = }")
