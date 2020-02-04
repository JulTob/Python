##  Python Test Script File
####  Run by writting test.py in the terminal from path
class Shape:
    def __init__(shape, Sides, Area):
        shape.Sides = Sides
        shape.Area= Area

class Square(Shape):
    def __init__(square, l):
        Shape.__init__(square, 4, l*l)

sq = Square(12)
print (sq.Sides)
print (sq.Area)
