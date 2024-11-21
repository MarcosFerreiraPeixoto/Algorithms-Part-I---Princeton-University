import unittest
from Assignment.Point import Point

class TestPoint(unittest.TestCase):

    def test_point_creation(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_slope_to(self):
        p1 = Point(1, 2)
        p2 = Point(3, 6)
        p3 = Point(1, 2)
        p4 = Point(3, 2)

        self.assertEqual(p1.slope_to(p2), 2.0)
        self.assertEqual(p1.slope_to(p3), float('-inf'))
        self.assertEqual(p1.slope_to(p4), 0.0)

        p5 = Point(1, 3)
        self.assertEqual(p1.slope_to(p5), float('inf'))

    def test_slope_order(self):
        p = Point(0, 0)
        points = [Point(1, 1), Point(2, 2), Point(3, 0)]
        slope_order = p.slope_order()
        
        sorted_points = sorted(points, key=lambda point: slope_order(p, point))
        expected_sorted = [Point(1, 1), Point(2, 2), Point(3, 0)]

        self.assertEqual(sorted_points, expected_sorted)

    def test_compare_to(self):
        p1 = Point(1, 2)
        p2 = Point(1, 3)
        p3 = Point(0, 2)
        p4 = Point(1, 2)

        self.assertEqual(p1.compare_to(p2), -1)
        self.assertEqual(p1.compare_to(p3), 1) 
        self.assertEqual(p1.compare_to(p4), 0) 

    def test_invalid_creation(self):
        with self.assertRaises(TypeError):
            Point("x", 2)
        
        with self.assertRaises(TypeError):
            Point(1, "y")

    def test_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(2, 1)
        
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

if __name__ == "__main__":
    unittest.main()
