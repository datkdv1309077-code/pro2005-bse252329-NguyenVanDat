class Product:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải lớn hơn 0")

    def __str__(self):
        return f"Price của product là: {self._price}"

p = Product(100)

print(p)

p.set_price(200)

print(p)