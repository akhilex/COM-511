import math

 

 
class Circle:
 
 
    def __init__(self, radius):
 5 
 
        self.radius = radius
 6 
 
 7 
 
    def area(self):
 8 
 
        return math.pi * self.radius ** 2
 9 
 
 10 
 
class Cylinder(Circle):
 11 
 
    def __init__(self, radius, height):
 12 
 
        super().__init__(radius)
 13 
 
        self.height = height
 14 
 
 15 
 
    def area(self):
 16 
 
    
 17 
 
        circle_area = super().area()
 18 
 
        lateral_area = 2 * math.pi * self.radius * self.height
 19 
 
        return 2 * circle_area + lateral_area
 20 
 
 21 
 
    def volume(self):
 22 
 
 23 
 
        return math.pi * self.radius ** 2 * self.height
 24 
 
 25 
 
radius_circle = 5
 26 
 
circle_instance = Circle(radius_circle)
 27 
 
print(f"Circle Area: {circle_instance.area()}")
 28 
 
 29 
 
radius_cylinder = 3
 30 
 
height_cylinder = 8
 31 
 
cylinder_instance = Cylinder(radius_cylinder, height_cylinder)
 32 
 
print(f"Cylinder Area: {cylinder_instance.area()}")
 33 
 
print(f"Cylinder Volume: {cylinder_instance.volume()}")
 34 
 
