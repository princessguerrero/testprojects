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