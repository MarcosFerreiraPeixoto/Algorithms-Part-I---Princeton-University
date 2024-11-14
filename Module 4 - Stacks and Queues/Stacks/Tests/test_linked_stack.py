import unittest
from Stacks.LinkedStack import LinkedStack

class TestLinkedStack(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()

    def test_push_pop(self):
        self.stack.push("to")
        self.stack.push("be")
        self.stack.push("or")
        self.stack.push("not")
        self.stack.push("to")
        self.assertEqual(self.stack.pop(), "to")
        self.stack.push("be")
        self.assertEqual(self.stack.pop(), "be")
        self.assertEqual(self.stack.pop(), "not")
        self.stack.push("that")
        self.assertEqual(self.stack.pop(), "that")
        self.assertEqual(self.stack.pop(), "or")
        self.assertEqual(self.stack.pop(), "be")
        self.stack.push("is")
        self.assertEqual(self.stack.pop(), "is")
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), "to")
        self.assertTrue(self.stack.is_empty())

    def test_push_pop2(self):
        elements = ["one", "two", "three", "four", "five"]
        for element in elements:
            self.stack.push(element)
        for element in reversed(elements):
            self.assertEqual(self.stack.pop(), element)
        self.assertTrue(self.stack.is_empty())

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("test")
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_underflow(self):
        with self.assertRaises(ValueError):
            self.stack.pop()


if __name__ == "__main__":
    unittest.main()