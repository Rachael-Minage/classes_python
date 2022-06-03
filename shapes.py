# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

class Circle:
    def __init__(self,radius) :
        self.radius = radius

    def area(self):
        a = 3.142*self.radius*self.radius
        return a
    def circumference(self):
        c = 2*3.142*self.radius
        return c



# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,side_a):
       self.side_a = side_a

    def area_of_square(self):
        return self.side_a**2
    def perimeter_of_square(self):
        return self.side_a*4


# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,w,l):
        self.w = w
        self.l = l
    def area_of_rectangle(self):
        return self.w*self.l
    def perimeter_of_rectangle(self):
        return 2*(self.w+self.l)

# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,radius):
        self.radius= radius
    def surface_area(self):
        return 4*3.142*self.radius**2
    def volume(self):
        return 4/3*(3.142*self.radius**3)




