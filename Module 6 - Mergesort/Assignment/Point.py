from typing import Callable
import matplotlib.pyplot as plt

class Point():
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"
    
    @property
    def x(self):
       return self._x 
    
    @property
    def y(self):
       return self._y 
    
    def __eq__(self, other: 'Point'):
        if not isinstance(other, Point):
            return False
        
        return self.compare_to(other) == 0

    def draw(self):
        plt.plot(self.x, self.y, 'o')
        plt.text(self.x, self.y, f'  {self}', fontsize=9)

    def draw_to(self, that: 'Point'):
        plt.plot([self.x, that.x], [self.y, that.y], 'r-')

    def compare_to(self, that: 'Point') -> int:
        if self.y < that.y:
            return -1
        elif self.y > that.y:
            return 1
        elif self.x < that.x:
            return -1
        elif self.x > that.x:
            return 1
        else:
            return 0

    def slope_to(self, that: 'Point') -> float:
        if self.y == that.y and self.x == that.x:
            return float("-inf")
        elif self.y == that.y:
            return 0
        elif self.x == that.x:
            return float("inf")
        else:
            return (that.y - self.y) / (that.x - self.x)
    

    def slope_order(self) -> Callable[['Point', 'Point'], int]:
        class SlopeComparator():
            def __init__(self, base_point: 'Point'):
                self.base_point = base_point

            def __call__(self, p1: 'Point', p2: 'Point') -> int:
                slope_a = self.base_point.slope_to(p1)
                slope_b = self.base_point.slope_to(p2)
                
                if slope_a < slope_b:
                    return -1
                elif slope_a == slope_b:
                    return 0
                else:
                    return 1

        return SlopeComparator(self)