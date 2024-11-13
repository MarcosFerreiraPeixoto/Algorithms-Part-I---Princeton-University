import unittest
from Deque import Deque

class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()
    
    def test_empty_iteration(self):
        result = list(self.deque)
        self.assertEqual(result, [])

    def test_add_first_remove_first(self):
        self.deque.add_first("to")
        self.deque.add_first("be")
        self.deque.add_first("or")
        
        self.assertEqual(self.deque.remove_first(), "or")
        self.assertEqual(self.deque.remove_first(), "be")
        self.assertEqual(self.deque.remove_first(), "to")
        self.assertTrue(self.deque.is_empty())

    def test_add_last_remove_last(self):
        self.deque.add_last("to")
        self.deque.add_last("be")
        self.deque.add_last("or")
        
        self.assertEqual(self.deque.remove_last(), "or")
        self.assertEqual(self.deque.remove_last(), "be")
        self.assertEqual(self.deque.remove_last(), "to")
        self.assertTrue(self.deque.is_empty())

    def test_add_first_remove_last(self):
        self.deque.add_first("to")
        self.deque.add_first("be")
        self.deque.add_first("or")
        
        self.assertEqual(self.deque.remove_last(), "to")
        self.assertEqual(self.deque.remove_last(), "be")
        self.assertEqual(self.deque.remove_last(), "or")
        self.assertTrue(self.deque.is_empty())

    def test_add_last_remove_first(self):
        self.deque.add_last("to")
        self.deque.add_last("be")
        self.deque.add_last("or")
        
        self.assertEqual(self.deque.remove_first(), "to")
        self.assertEqual(self.deque.remove_first(), "be")
        self.assertEqual(self.deque.remove_first(), "or")
        self.assertTrue(self.deque.is_empty())

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.add_first("test")
        self.assertFalse(self.deque.is_empty())
        self.deque.remove_first()
        self.assertTrue(self.deque.is_empty())

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_first("one")
        self.deque.add_last("two")
        self.assertEqual(self.deque.size(), 2)
        self.deque.remove_first()
        self.assertEqual(self.deque.size(), 1)
        self.deque.remove_last()
        self.assertEqual(self.deque.size(), 0)

    def test_underflow_remove_first(self):
        with self.assertRaises(ValueError):
            self.deque.remove_first()

    def test_underflow_remove_last(self):
        with self.assertRaises(ValueError):
            self.deque.remove_last()
    
    def test_iteration(self):
        elements = ["first", "second", "third", "fourth"]
        for element in elements:
            self.deque.add_last(element)

        for i, value in enumerate(self.deque):
            self.assertEqual(value, elements[i])

        self.assertEqual(self.deque.size(), len(elements))

if __name__ == "__main__":
    unittest.main()
