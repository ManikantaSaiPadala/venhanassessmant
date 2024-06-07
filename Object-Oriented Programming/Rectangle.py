class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

length = float(input())
width = float(input())
rect = Rectangle(length, width)
print(rect.area())
print(rect.perimeter())