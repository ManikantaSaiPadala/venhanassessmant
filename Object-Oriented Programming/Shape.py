class Shape:
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, rad: float):
        self.rad = rad

    def area(self) -> float:
        return 3.14 * self.rad ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.rad

class Rectangle(Shape):
    def __init__(self, len: float, wid: float):
        self.len = len
        self.wid = wid

    def area(self) -> float:
        return self.len * self.wid

    def perimeter(self) -> float:
        return 2 * (self.len + self.wid)

cir = Circle(5)
rect = Rectangle(5, 9)
print(f"Area of Circle : {cir.area()}")
print(f"Perimeter of Circle : {cir.perimeter()}")
print(f"Area of Rectangle : {rect.area()}")
print(f"Perimeter of Rectangle : {rect.perimeter()}")