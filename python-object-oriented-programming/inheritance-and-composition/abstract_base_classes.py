# abstract base class
from abc import ABC, abstractmethod
import math

class GraphicsShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicsShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return math.pi * self.radius * self.radius

class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side * self.side

# cannot instantiate an abstract class
# shape = GraphicsShape()
# circle and square should implement calcArea abstract class
circle = Circle(10)
print(f"circle's area={circle.calcArea()}")
square = Square(10)
print(f"square's area={square.calcArea()}")