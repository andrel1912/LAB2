from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        """Kollar cirkeln. Visar ValueError om radien inte är positiv"""
        super().__init__(x, y)
        if radius <= 0:
            raise ValueError("Radien måste vara positiv")
        self.radius = radius

    @property
    def area(self):
        """Returnerar cirkelns area"""
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self):
        """Returnerar cirkelns omkrets"""
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self):
        """Skickar true om cirkeln är en enhetscirkel"""
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self):
        return f"Cirkel({self.x}, {self.y}), radie: {self.radius}"