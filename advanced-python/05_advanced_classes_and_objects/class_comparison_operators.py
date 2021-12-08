class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __ge__(self, other):
        return self.x >= other.x or self.x == other.x and self.y >= other.y
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f'({self.x},{self.y})'
    
    
point1 = Point(1,2)
point2 = Point(1,2)
print(point1 == point2) # True

print(point1 < point2) # False
print(point1 >= point2) # True

point3 = Point(2,3)
arr = [point3, point1, point2]
# we implemented ge and lt
arr.sort()

for point in arr:
    print(point)
    
