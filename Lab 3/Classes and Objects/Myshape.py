class MyShape:
    def __init__(self, color="purple", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape - Color: {self.color}, Is Filled: {self.is_filled}"

    def getArea(self):
        return 0
    
'''
shape = MyShape()
print(shape)
print("Area:", shape.getArea())
'''