import math

def sphere_volume(r):
    volume = (4 / 3) * math.pi * (r ** 3)
    print(volume)
    
a = int(input("Enter radius: "))
sphere_volume(a)