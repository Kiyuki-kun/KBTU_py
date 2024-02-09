from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
'''
rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area()) => 24 
'''