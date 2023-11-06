shape=input("Input shape i.e square, rectangle, circle:")
import math
if shape=="square":
    length=float(input("Input length:"))
    area=length**2
if shape=="rectangle":
    length=float(input("Input length:"))
    width=float(input("Input width:"))
    area=length*width
if shape=="circle":
    radius=float(input("Input radius:"))
    area=math.pi*radius**2
print(area)