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
        print("The area is")
        return self.length * self.width
    
    def perimeter(self):
        print("The perimeter is")
        return 2*self.length + 2*self.width

class Diamond(Shapes):
    def __init__(self, length, altitude):
        self.length = length
        self.altitude = altitude
        
    def area(self):
        print("The area is")
        return self.length * self.altitude
    
    def perimeter(self):
        print("The perimeter is")
        return 4*self.length

class Triangle(Shapes):
    def __init__(self, height, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
#         where side_b is the base
        self.side_c = side_c
        self.height = height
        
    def area(self):
        print("The area is")
        return (self.side_b*self.height)/2
    
    def perimeter(self):
        print("The perimeter is")
        return self.side_a + self.side_b + self.side_c

import math
class Circle(Shapes):
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
        
    def area(self):
        print("The area is")
        return self.pi*(math.pow(self.r, 2))
    
    def perimeter(self):
        print("The circumference using pi = 3.14159 is")
        return 2*self.pi*self.r

def choose_shape(id):

    if id == 1:
        print("Enter sides")
        sides = int(input())
        # if sides
        #     print("Numbers only")
        x = Square(sides)
        print(x.perimeter())
        print(x.area())
        print("Continue? Y/N")
        answer = input()
        if answer == "Y":
            print("*************")
            return shape_menu()
        elif answer == "N":
            print("Ok Bye!")
            return quit()
    elif id == 2:
        print("Enter a length")
        length = int(input())
        print("Enter a width")
        width = int(input())
        x = Rectangle(length, width)
        print(x.perimeter())
        print(x.area())
        print("Continue? Y/N")
        answer = input()
        if answer == "Y":
            print("*************")
            return shape_menu()
        elif answer == "N":
            print("Ok Bye!")
            return quit()
    elif id == 3:
        print("Enter length")
        length = int(input())
        print("Enter altitude")
        altitude = int(input())
        x = Diamond(length, altitude)
        print(x.perimeter())
        print(x.area())
        print("Continue? Y/N")
        answer = input()
        if answer == "Y":
            print("*************")
            return shape_menu()
        elif answer == "N":
            print("Ok Bye!")
            return quit()
    elif id == 4:
        print("Enter height")
        height = int(input())
        print("I need 3 sides. Enter the base first")
        side_b = int(input())
        print("Now enter the other side")
        side_a = int(input())
        print("Finally enter the last side")
        side_c = int(input())
        x = Triangle(height, side_a, side_b, side_c)
        print(x.perimeter())
        print(x.area())
        print("Continue? Y/N")
        answer = input()
        if answer == "Y":
            print("*************")
            return shape_menu()
        elif answer == "N":
            print("Ok Bye!")
            return quit()
    elif id == 5:
        print("Enter a radius")
        r = int(input())
        pi = 3.14159
        x = Circle(pi, r)
        print(x.perimeter())
        print(x.area())
        print("Continue? Y/N")
        answer = input()
        if answer == "Y":
            print("*************")
            return shape_menu()
        elif answer == "N":
            print("Ok Bye!")
            return quit()
    else:
        print("Please choose a valid number")
        print("*************")
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

greeting = "Welcome to Shapes - Area and Perimeter Calculator"
print(greeting)
print(shape_menu())
text = input()