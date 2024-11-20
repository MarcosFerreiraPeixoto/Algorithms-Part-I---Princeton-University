import unittest
from Assignment.Point import Point
from Assignment.LineSegment import LineSegment
from Assignment.FastCollinearPoints import FastCollinearPoints

class TestFastCollinearPoints(unittest.TestCase):

    def setUp(self):
        # Set up test cases and initialize FastCollinearPoints instance
        self.points_valid = [
            Point(0, 0),
            Point(1, 1),
            Point(2, 2),
            Point(3, 3),
            Point(4, 4),
        ]
        self.points_non_collinear = [
            Point(0, 0),
            Point(1, 2),
            Point(2, 3),
            Point(3, 1),
        ]
        self.points_with_duplicates = [
            Point(0, 0),
            Point(1, 1),
            Point(1, 1),  # Duplicate point
            Point(2, 2),
        ]
        self.points_empty = []
        self.points_single = [Point(0, 0)]

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            FastCollinearPoints(self.points_empty)

    def test_single_point(self):
        fast_collinear = FastCollinearPoints(self.points_single)
        self.assertEqual(fast_collinear.number_of_segments(), 0)
        self.assertEqual(fast_collinear.segments(), [])

    def test_all_collinear_points(self):
        fast_collinear = FastCollinearPoints(self.points_valid)
        self.assertEqual(fast_collinear.number_of_segments(), 1)
        # Expect a single line segment from the first to the last point
        self.assertEqual(len(fast_collinear.segments()), 1)

    def test_no_collinear_points(self):
        fast_collinear = FastCollinearPoints(self.points_non_collinear)
        self.assertEqual(fast_collinear.number_of_segments(), 0)
        self.assertEqual(fast_collinear.segments(), [])

    def test_some_collinear_points(self):
        points = [
            Point(0, 0),
            Point(1, 1),
            Point(2, 2),
            Point(3, 3),
            Point(4, 4),
            Point(0, 3),
            Point(1, 2),
        ]
        fast_collinear = FastCollinearPoints(points)
        self.assertEqual(fast_collinear.number_of_segments(), 1)
        self.assertEqual(len(fast_collinear.segments()), 1)

    def test_duplicate_points(self):
        with self.assertRaises(ValueError):
            FastCollinearPoints(self.points_with_duplicates)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            FastCollinearPoints(None)
        
        with self.assertRaises(TypeError):
            FastCollinearPoints([None, Point(1, 2), Point(3, 4)])

    def test_large_input(self):
        # Add a larger test with many points
        points = [Point(i, i) for i in range(100)]  # All points are collinear
        fast_collinear = FastCollinearPoints(points)
        self.assertEqual(fast_collinear.number_of_segments(), 1)
        self.assertEqual(len(fast_collinear.segments()), 1)

if __name__ == "__main__":
    unittest.main()
