# Shape Area and Perimeter Classes - Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, 
# triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.

class Shapes:
    def __init__(self, length_of_sides):
        self.length_of_sides = length_of_sides
        
    def area(self):
        print("The area is")
        return self.length_of_sides * self.length_of_sides
    
    def perimeter(self):
        print("The perimeter is")
        return 4*self.length_of_sides
    
    # def num_of_sides(self):
    #     return 4

class Square(Shapes):
    pass

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*self.length + 2*self.width

class Diamond(Shapes):
    def __init__(self, length, altitude):
        self.length = length
        self.altitude = altitude
        
    def area(self):
        return self.length * self.altitude
    
    def perimeter(self):
        return 4*self.length

class Triangle(Shapes):
    def __init__(self, height, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
#         where side_b is the base
        self.side_c = side_c
        self.height = height
        
    def area(self):
        return (self.side_b*self.height)/2
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

import math
class Circle(Shapes):
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
        
    def area(self):
        return self.pi*(math.pow(self.r, 2))
    
    def perimeter(self):
        return 2*self.pi*self.r

def choose_shape(id):

    if id == 1:
        print("Enter sides")
        sides = int(input())
        x = Square(sides)
        print(x.perimeter())
        print(x.area())
    elif id == 2:
        print("Enter a length")
        length = int(input())
        print("Enter a width")
        width = int(input())
        x = Rectangle(length, width)
        print("Perimeter")
        print(x.perimeter())
        print("Area")
        print(x.area())
    elif id == 3:
        return Diamond()
    elif id == 4:
        return Triangle()
    elif id == 5:
        return Circle()
    else:
        print("Please choose a valid number")
        return shape_menu()

def shape_menu():
    print("Select A Shape")
    print("1) Square")
    print("2) Rectangle")
    print("3) Diamond")
    print("4) Triangle")
    print("5) Circle")

    id = int(input("Choose a shape by selecting the number "))
    return choose_shape(id)

print("Welcome to Shape Area and Perimeter")
print(shape_menu())
text = input()