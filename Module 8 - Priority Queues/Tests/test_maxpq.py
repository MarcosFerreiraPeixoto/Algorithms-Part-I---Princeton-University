import unittest
from MaxPQ import MaxPQ  # Replace 'your_module' with the actual module name.

class TestMaxPQ(unittest.TestCase):

    def setUp(self):
        self.pq = MaxPQ()

    def test_empty_queue(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(self.pq.size(), 0)
        with self.assertRaises(ValueError):
            self.pq.max()
        with self.assertRaises(ValueError):
            self.pq.del_max()

    def test_insert_and_max(self):
        self.pq.insert(5)
        self.assertEqual(self.pq.max(), 5)
        self.assertEqual(self.pq.size(), 1)
        self.assertFalse(self.pq.is_empty())

    def test_insert_and_del_max(self):
        self.pq.insert(10)
        self.assertEqual(self.pq.del_max(), 10)
        self.assertTrue(self.pq.is_empty())

    def test_ordering(self):
        for val in [3, 1, 4, 1, 5, 9]:
            self.pq.insert(val)
        
        self.assertEqual(self.pq.del_max(), 9)
        self.assertEqual(self.pq.del_max(), 5)
        self.assertEqual(self.pq.del_max(), 4)
        self.assertEqual(self.pq.del_max(), 3)
        self.assertEqual(self.pq.del_max(), 1)
        self.assertEqual(self.pq.del_max(), 1)
        self.assertTrue(self.pq.is_empty())

    def test_with_duplicates(self):
        self.pq.insert(4)
        self.pq.insert(4)
        self.assertEqual(self.pq.del_max(), 4)
        self.assertEqual(self.pq.del_max(), 4)
        self.assertTrue(self.pq.is_empty())

    def test_negative_numbers(self):
        for val in [0, -1, -3, 2, 1]:
            self.pq.insert(val)
        
        self.assertEqual(self.pq.del_max(), 2)
        self.assertEqual(self.pq.del_max(), 1)
        self.assertEqual(self.pq.del_max(), 0)
        self.assertEqual(self.pq.del_max(), -1)
        self.assertEqual(self.pq.del_max(), -3)
    
    def test_large_numbers(self):
        self.pq.insert(10**10)
        self.pq.insert(10**5)
        self.pq.insert(10**8)

        self.assertEqual(self.pq.del_max(), 10**10)
        self.assertEqual(self.pq.del_max(), 10**8)
        self.assertEqual(self.pq.del_max(), 10**5)

    def test_custom_comparator(self):
        pq = MaxPQ(comparator=lambda x, y: y - x)
        pq.insert(5)
        pq.insert(10)
        pq.insert(1)

        self.assertEqual(pq.del_max(), 1)  # Min priority with custom comparator
        self.assertEqual(pq.del_max(), 5)
        self.assertEqual(pq.del_max(), 10)
