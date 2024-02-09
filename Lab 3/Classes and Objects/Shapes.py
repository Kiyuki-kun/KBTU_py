from Myshape import MyShape
import math

class Rectangle(MyShape):
    def __init__(self, color="Red", is_filled=False, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return (f"Rectangle - Color: {self.color}, Is Filled: {self.is_filled}, "
                f"Top Left: ({self.x_top_left}, {self.y_top_left}), "
                f"Length: {self.length}, Width: {self.width}")
        
    def getPerim(self):
        return 2 * (self.length + self.width)

class Circle(MyShape):
    def __init__(self, color="Yellow", is_filled=False, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return (f"Circle - Color: {self.color}, Is Filled: {self.is_filled}, "
                f"Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}")

'''
rectangle = Rectangle(color="blue", length=5, width=3)
print(rectangle)
print("Area:", rectangle.getArea())
print("Perimeter:", rectangle.getPerim())
'''

'''
circle = Circle(color="red", radius=2)
print(circle)
print("Area:", circle.getArea())
'''