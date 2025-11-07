from shape import Shape

class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, height=1):
# Använder Shape för position
        super().__init__(x, y)

# kollar att bredden och höjden är positiva
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")        
        self.width = width
        self.height = height

#area
    @property
    def area(self):
        return self.width * self.height
    
# omkrets
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Kollar att rektangeln är en kvadrat
    def is_square(self):
        return self.width == self.height
    
# utskrift/felsökning i terminalen
    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __str__(self):
        return f"Rektangel med centrum ({self.x}, {self.y}), bredd: {self.width}, höjd: {self.height}"