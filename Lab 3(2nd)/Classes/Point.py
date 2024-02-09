import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

'''
point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()  => (3, 4)
point2.show()  => (6, 8)

distance = point1.dist(point2)
print("Distance between the points:", distance)  => 5.0

point1.move(1, 2)
point1.show()  => (1, 2)
'''