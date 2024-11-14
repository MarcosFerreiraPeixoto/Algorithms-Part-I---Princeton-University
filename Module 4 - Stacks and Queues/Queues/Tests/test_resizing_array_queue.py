import unittest
from Queues.ResizingArrayQueue import ResizingArrayQueue

class TestResizingArrayQueue(unittest.TestCase):

    def setUp(self):
        self.queue = ResizingArrayQueue()

    def test_enqueue_dequeue(self):
        self.queue.enqueue("to")
        self.queue.enqueue("be")
        self.queue.enqueue("or")
        self.queue.enqueue("not")
        self.queue.enqueue("to")
        
        self.assertEqual(self.queue.dequeue(), "to")
        self.assertEqual(self.queue.dequeue(), "be")
        self.assertEqual(self.queue.dequeue(), "or")
        self.assertEqual(self.queue.dequeue(), "not")
        
        self.queue.enqueue("be")
        self.assertEqual(self.queue.dequeue(), "to")
        self.assertEqual(self.queue.dequeue(), "be")
        
        self.assertTrue(self.queue.is_empty())
        
        self.queue.enqueue("is")
        self.assertEqual(self.queue.dequeue(), "is")
        self.assertTrue(self.queue.is_empty())

        
    def test_enqueue_dequeue_order(self):
        elements = ["one", "two", "three", "four", "five"]
        for element in elements:
            self.queue.enqueue(element)
        for element in elements:
            self.assertEqual(self.queue.dequeue(), element)
        self.assertTrue(self.queue.is_empty())

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue("test")
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_underflow(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


if __name__ == "__main__":
    unittest.main()