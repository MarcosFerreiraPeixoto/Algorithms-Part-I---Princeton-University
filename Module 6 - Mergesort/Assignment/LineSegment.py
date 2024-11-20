from Assignment.Point import Point

class LineSegment():
    def __init__(self, p1: Point, p2: Point):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError("Both p1 and p2 must be instances of Point.")
    
        if p1.compare_to(p2) == 0:
            raise ValueError(f"both arguments to LineSegment constructor are the same point: {p1}")
        
        self._p1 = p1
        self._p2 = p2

    def __eq__(self, other):
        if not isinstance(other, LineSegment):
            return False

        return (self._p1, self._p2) == (other.p1, other.p2) or (self._p2, self._p1) == (other.p1, other.p2)
    def __str__(self):
        return f"[{self._p1}, {self._p2}]"
    
    @property
    def p1(self):
       return self._p1 
    
    @property
    def p2(self):
       return self._p2 
    
    def draw(self):
        self._p1.draw_to(self.p2)