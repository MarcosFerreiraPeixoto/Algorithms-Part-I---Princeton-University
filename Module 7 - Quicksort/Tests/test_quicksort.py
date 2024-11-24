import unittest
from Quick import Quick

class TestQuick(unittest.TestCase):

    def setUp(self):
        self.sorter = Quick()

    def test_empty_list(self):
        l = []
        self.sorter.sort(l)
        self.assertEqual(l, [])

    def test_single_element(self):
        l = [42]
        self.sorter.sort(l)
        self.assertEqual(l, [42])

    def test_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        self.sorter.sort(l)
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        l = [5, 4, 3, 2, 1]
        self.sorter.sort(l)
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        l = [3, 1, 4, 1, 5, 9]
        self.sorter.sort(l)
        self.assertEqual(l, [1, 1, 3, 4, 5, 9])

    def test_duplicates(self):
        l = [2, 3, 2, 1, 3]
        self.sorter.sort(l)
        self.assertEqual(l, [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        l = [0, -1, -3, 2, 1]
        self.sorter.sort(l)
        self.assertEqual(l, [-3, -1, 0, 1, 2])

    def test_large_numbers(self):
        l = [10**5, 10**3, 10**4]
        self.sorter.sort(l)
        self.assertEqual(l, [10**3, 10**4, 10**5])

if __name__ == "__main__":
    unittest.main()
