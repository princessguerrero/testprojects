# Shape Area and Perimeter Classes - Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, 
# triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.

class Shapes:
    def __init__(self, length_of_sides):
        self.length_of_sides = length_of_sides
        
    def area(self):
        return self.length_of_sides * self.length_of_sides
    
    def perimeter(self):
        return 4*self.length_of_sides
    
    def num_of_sides(self):
        return 4

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

