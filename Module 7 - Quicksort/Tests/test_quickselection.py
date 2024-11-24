import unittest
from Quick import Quick

class TestQuick(unittest.TestCase):

    def setUp(self):
        self.selector = Quick()

    def test_empty_list(self):
        l = []
        with self.assertRaises(ValueError):
            self.selector.select(l, 1)

    def test_single_element(self):
        l = [42]
        self.assertEqual(self.selector.select(l, 1), 42)

    def test_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(self.selector.select(l, 3), 3)

    def test_reverse_sorted_list(self):
        l = [5, 4, 3, 2, 1]
        self.assertEqual(self.selector.select(l, 2), 2)

    def test_unsorted_list(self):
        l = [3, 1, 4, 1, 5, 9]
        self.assertEqual(self.selector.select(l, 4), 4)

    def test_duplicates(self):
        l = [2, 3, 2, 1, 3]
        self.assertEqual(self.selector.select(l, 3), 2)

    def test_negative_numbers(self):
        l = [0, -1, -3, 2, 1]
        self.assertEqual(self.selector.select(l, 5), 2)

    def test_large_numbers(self):
        l = [10**5, 10**3, 10**4]
        self.assertEqual(self.selector.select(l, 2), 10**4)

    def test_out_of_bounds(self):
        l = [1, 2, 3]
        with self.assertRaises(ValueError):
            self.selector.select(l, 0)  # nth = 0 is invalid
        with self.assertRaises(ValueError):
            self.selector.select(l, 4)  # nth > len(l) is invalid

    def test_multiple_same_nth(self):
        l = [5, 5, 5, 5]
        self.assertEqual(self.selector.select(l, 2), 5)

if __name__ == "__main__":
    unittest.main()
