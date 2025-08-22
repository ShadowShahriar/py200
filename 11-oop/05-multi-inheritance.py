class Dad:
    def height(self):
        return "Short"


class Mom:
    def color(self):
        return "Fair"


class Child(Dad, Mom):
    pass


child = Child()
print(f"{child.height() = }")
print(f"{child.color()  = }")
