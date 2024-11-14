import unittest
from Assignment.RandomizedQueue import RandomizedQueue

class TestRandomizedQueue(unittest.TestCase):

    def setUp(self):
        self.queue = RandomizedQueue()
    
    def test_empty_iteration(self):
        result = list(self.queue)
        self.assertEqual(result, [])

    def test_enqueue_dequeue(self):
        self.queue.enqueue("to")
        self.queue.enqueue("be")
        self.queue.enqueue("or")
        
        removed_items = {self.queue.dequeue(), self.queue.dequeue(), self.queue.dequeue()}
        self.assertEqual(removed_items, {"to", "be", "or"})
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_sample(self):
        elements = ["one", "two", "three", "four", "five"]
        for element in elements:
            self.queue.enqueue(element)
        
        sampled_items = {self.queue.sample() for _ in range(10)}
        self.assertTrue(sampled_items.issubset(set(elements)))
        self.assertEqual(self.queue.size(), len(elements))

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue("test")
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue("one")
        self.queue.enqueue("two")
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)

    def test_underflow_dequeue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_underflow_sample(self):
        with self.assertRaises(IndexError):
            self.queue.sample()
    
    def test_iteration(self):
        elements = ["first", "second", "third", "fourth"]
        for element in elements:
            self.queue.enqueue(element)

        iterated_elements = list(self.queue)
        self.assertEqual(set(iterated_elements), set(elements))
        self.assertEqual(self.queue.size(), len(elements))

if __name__ == "__main__":
    unittest.main()
