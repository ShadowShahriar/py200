class Calc:
    def __init__(self, val) -> None:
        self.value = val

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def from_str(cls, val_str):
        return cls(int(val_str))


calc = Calc.from_str("42")
print(f"{calc.add(10, 20) = }")
