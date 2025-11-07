class Shape:
# class för formerna
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def area(self):
        pass

    def perimeter(self):
        pass
    
# Flyttar formen
    def move(self , dx, dy):
        self.x += dx
        self.y += dy

# Jämförelser baserat på arean 
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __le__(self, other):
        return self.area() <= other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()