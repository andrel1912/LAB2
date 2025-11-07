class Shape:
    """klass för geometriska former x och y"""


    def __init__(self, x=0, y=0):
        """sätter igång formen med pos x och y"""
        self.x = x
        self.y = y
    

    def area(self):
        """Returnerar arean"""
        pass


    def perimeter(self):
        """Returnerar omkretsen"""
        pass
    
    def move(self, dx, dy):
        """dx flyttar formen horisontellt, dy vertikalt"""
        self.x += dx
        self.y += dy


        """Gör jämförelsemetoder baserade på area"""

    def __eq__(self, other):
        return self.area == other.area
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area