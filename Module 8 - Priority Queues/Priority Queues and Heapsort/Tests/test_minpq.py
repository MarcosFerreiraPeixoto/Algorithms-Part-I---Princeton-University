import unittest
from MinPQ import MinPQ  # Replace 'MinPQ' with the actual module name if necessary.

class TestMinPQ(unittest.TestCase):

    def setUp(self):
        self.pq = MinPQ()

    def test_empty_queue(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(self.pq.size(), 0)
        with self.assertRaises(ValueError):
            self.pq.min()
        with self.assertRaises(ValueError):
            self.pq.del_min()

    def test_insert_and_min(self):
        self.pq.insert(5)
        self.assertEqual(self.pq.min(), 5)
        self.assertEqual(self.pq.size(), 1)
        self.assertFalse(self.pq.is_empty())

    def test_insert_and_del_min(self):
        self.pq.insert(10)
        self.assertEqual(self.pq.del_min(), 10)
        self.assertTrue(self.pq.is_empty())

    def test_ordering(self):
        for val in [3, 1, 4, 1, 5, 9]:
            self.pq.insert(val)
        
        self.assertEqual(self.pq.del_min(), 1)
        self.assertEqual(self.pq.del_min(), 1)
        self.assertEqual(self.pq.del_min(), 3)
        self.assertEqual(self.pq.del_min(), 4)
        self.assertEqual(self.pq.del_min(), 5)
        self.assertEqual(self.pq.del_min(), 9)
        self.assertTrue(self.pq.is_empty())

    def test_with_duplicates(self):
        self.pq.insert(4)
        self.pq.insert(4)
        self.assertEqual(self.pq.del_min(), 4)
        self.assertEqual(self.pq.del_min(), 4)
        self.assertTrue(self.pq.is_empty())

    def test_negative_numbers(self):
        for val in [0, -1, -3, 2, 1]:
            self.pq.insert(val)
        
        self.assertEqual(self.pq.del_min(), -3)
        self.assertEqual(self.pq.del_min(), -1)
        self.assertEqual(self.pq.del_min(), 0)
        self.assertEqual(self.pq.del_min(), 1)
        self.assertEqual(self.pq.del_min(), 2)
    
    def test_large_numbers(self):
        self.pq.insert(10**10)
        self.pq.insert(10**5)
        self.pq.insert(10**8)

        self.assertEqual(self.pq.del_min(), 10**5)
        self.assertEqual(self.pq.del_min(), 10**8)
        self.assertEqual(self.pq.del_min(), 10**10)

    def test_custom_comparator(self):
        pq = MinPQ(comparator=lambda x, y: y - x)  # Reverse for max priority
        pq.insert(5)
        pq.insert(10)
        pq.insert(1)

        self.assertEqual(pq.del_min(), 10)  # Max priority with custom comparator
        self.assertEqual(pq.del_min(), 5)
        self.assertEqual(pq.del_min(), 1)

if __name__ == "__main__":
    unittest.main()
