import math

area_circle = lambda r: math.pi * r ** 2

radius = float(input("Enter radius of the circle: "))

area = area_circle(radius)

print("Area of the circle:", area)