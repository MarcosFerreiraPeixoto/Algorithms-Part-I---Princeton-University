import unittest
from HSort import HSort

class TestHSort(unittest.TestCase):

    def test_h_1(self):
        hsort = HSort(h=1)
        data = [5, 3, 8, 4, 2]
        hsort.sort(data)
        self.assertEqual(data, [2, 3, 4, 5, 8])

    def test_h_2(self):
        hsort = HSort(h=2)
        data = [9, 8, 3, 7, 2, 6, 1, 5]
        hsort.sort(data)
        self.assertEqual(data, [1, 5, 2, 6, 3, 7, 9, 8])

    def test_empty_list(self):
        hsort = HSort(h=1)
        data = []
        hsort.sort(data)
        self.assertEqual(data, [])

    def test_single_element(self):
        hsort = HSort(h=1)
        data = [42]
        hsort.sort(data)
        self.assertEqual(data, [42])

    def test_already_sorted(self):
        hsort = HSort(h=3)
        data = [1, 2, 3, 4, 5]
        hsort.sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        hsort = HSort(h=2)
        data = [5, 4, 3, 2, 1]
        hsort.sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        hsort = HSort(h=2)
        data = [4, 5, 4, 2, 3, 2]
        hsort.sort(data)
        self.assertEqual(data, [3, 2, 4, 2, 4, 5])

    def test_negative_numbers(self):
        hsort = HSort(h=2)
        data = [-1, -3, 2, 1, 0]
        hsort.sort(data)
        self.assertEqual(data, [-1, -3, 0, 1, 2])

if __name__ == "__main__":
    unittest.main()
