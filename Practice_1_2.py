# Practice two >>> Draw a triangle
a = float(input("Enter the first side of the triangle =  "))
b = float(input("Insert the second side of the triangle = "))
c = float(input("Enter the third side of the triangle = "))

if ((a + b) > c) & ((a + c) > b) & ((b + c) > a):
    print("** A triangle can be drawn **")
else:
    print("** You can not draw a triangle **")
