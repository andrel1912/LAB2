from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
# Använder Shape för position
        super().__init__(x, y)

# Kollar så att radien är positiv
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
# Omkrets
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self):
        return self.radius == 1 and self .x == 0 and self.y == 0
    
# utskrift/felsökning i terminalen
    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self):
        return f"Cirkel({self.x}, {self.y}), radie: {self.radius}"