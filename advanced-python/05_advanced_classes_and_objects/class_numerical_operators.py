class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    # +=
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
point1 = Point(1,2)
point2 = Point(2,3)

print (point1 + point2)
print (point1 - point2)
print (point1 * point2)
point1 += point2
print (point1)
