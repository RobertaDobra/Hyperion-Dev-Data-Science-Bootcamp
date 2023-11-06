x=float(input("Enter length of side1 of a triangle "))
y=float(input("Enter length of side2 of a triangle "))
z=float(input("Enter length of side3 of a triangle "))
s=(x+y+z)/2
area=(s*(s-x)*(s-y)*(s-z))**0.5
print(area)