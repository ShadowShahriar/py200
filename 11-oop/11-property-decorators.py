class Product:
    def __init__(self, price) -> None:
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if val > 0:
            self._price = val
        else:
            print("Invalid price")


product = Product(100)
product.price = 200
print(product.price)
