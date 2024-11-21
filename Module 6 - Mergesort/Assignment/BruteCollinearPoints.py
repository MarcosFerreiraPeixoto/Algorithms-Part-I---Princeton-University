from Assignment.Point import Point
from Assignment.LineSegment import LineSegment
from typing import List


class BruteCollinearPoints():
    def __init__(self, points: List[Point]):
        if points is None:
            raise ValueError("The input can't be None!")
        
        if len(points) == 0:
            raise ValueError("Input is empty!")

        for point in points:
            if not isinstance(point, Point):
                raise TypeError(f"Invalid item: {point}! It must be an instance of Point!")

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i].compare_to(points[j]) == 0:
                    raise ValueError("Duplicate points detected in the input!")

        self._segments = []

        self.find_segments(points)
    
    def get_segment_extremity_points(self, points: List[Point]) -> List[Point]:       
        min_point = points[0]
        max_point = points[0]
        
        for i in range(1, len(points)):
            if min_point.compare_to(points[i]) == 1:
                min_point = points[i]
            
            if max_point.compare_to(points[i]) == -1:
                max_point = points[i]

        return min_point, max_point

    def find_segments(self, points: List[Point]):
        if len(points) < 4:
            return

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    for l in range(k + 1, len(points)):
                        slope_i_j = points[i].slope_to(points[j])
                        slope_j_k = points[j].slope_to(points[k])
                        slope_k_l = points[k].slope_to(points[l])

                        if slope_i_j == slope_j_k == slope_k_l:
                            p1, p2 = self.get_segment_extremity_points([points[i], points[j], points[k], points[l]])
                            self._segments.append(LineSegment(p1, p2))

    def number_of_segments(self) -> int:
        return len(self._segments)

    def segments(self) -> List[LineSegment]:
        return self._segments