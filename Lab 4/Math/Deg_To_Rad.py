import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

degrees = float(input("Enter the degree value: "))

radians = degrees_to_radians(degrees)

print(f"{degrees} degrees = {radians} radians.")
