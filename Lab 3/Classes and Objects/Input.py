from Shapes import Rectangle

color = input("Enter color for Rectangle: ")
is_filled = input("Is Rectangle filled? (True/False): ").lower() == 'true'
x_top_left = float(input("Enter X coordinate of top-left corner: "))
y_top_left = float(input("Enter Y coordinate of top-left corner: "))
length = float(input("Enter length of the Rectangle: "))
width = float(input("Enter width of the Rectangle: "))

rectangle = Rectangle(color=color, is_filled=is_filled, x_top_left=x_top_left, y_top_left=y_top_left, length=length, width=width)

print(rectangle)
print("Area:", rectangle.getArea())
