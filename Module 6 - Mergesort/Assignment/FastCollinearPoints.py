from Assignment.Point import Point
from Assignment.LineSegment import LineSegment
from Mergesort.Mergesort import Mergesort
from typing import List
import matplotlib.pyplot as plt

class FastCollinearPoints():
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

    def find_colinear_points(self, p: Point, sorted_points: List[Point]):
        colinear_points: List[List[Point]] = []

        colinear_points_list_guess = [p, sorted_points[0]]
        current_slope_value = p.slope_to(sorted_points[0])
        
        for i in range(1 ,len(sorted_points)):
            new_slope_value = p.slope_to(sorted_points[i])
            
            if current_slope_value == new_slope_value:
                colinear_points_list_guess.append(sorted_points[i])
            else:
                if len(colinear_points_list_guess) >= 4:
                    colinear_points.append(colinear_points_list_guess)
                
                current_slope_value = new_slope_value
                colinear_points_list_guess = [p, sorted_points[i]]
        
        if len(colinear_points_list_guess) >= 4:
            colinear_points.append(colinear_points_list_guess)

        return colinear_points

    def find_segments(self, points: List[Point]):
        if len(points) < 4:
            return

        for i in range(len(points)):
            p1 = points[i]
            
            points_to_sort = [p for p in points if p1.compare_to(p) != 0]
            sorter = Mergesort(p1.slope_order())
            sorter.sort(points_to_sort)
            colinear_points_lists = self.find_colinear_points(p1, points_to_sort)

            if colinear_points_lists != []:
                for colinear_points_list in colinear_points_lists:
                    p1, p2 = self.get_segment_extremity_points(colinear_points_list)
                    new_segment = LineSegment(p1, p2)
                    
                    if new_segment not in self._segments:
                        self._segments.append(new_segment)

    def number_of_segments(self) -> int:
        return len(self._segments)

    def segments(self) -> List[LineSegment]:
        return self._segments


def main(filename):
    # Read the points from a file
    points = []
    with open(filename, 'r') as file:
        n = int(file.readline().strip())  # Read the number of points
        for _ in range(n):
            x, y = map(int, file.readline().strip().split())
            points.append(Point(x, y))
    
    # Draw the points
    plt.figure(figsize=(8, 8))
    plt.xlim(0, 32768)
    plt.ylim(0, 32768)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Point Drawing Example")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    for point in points:
        plt.plot(point.x, point.y, 'o', color='black')  # Draw each point
    
    # Process the points and find line segments
    collinear = FastCollinearPoints(points)

    for segment in collinear.segments():
        print(segment)  # Print the segment
        segment.draw()
    
    # Display the result
    plt.show()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
    else:
        main(sys.argv[1])