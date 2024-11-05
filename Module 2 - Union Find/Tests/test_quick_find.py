import unittest
from QuickFindUF import QuickFindUF

class TestQuickFindUF(unittest.TestCase):
    def setUp(self):
        self.qf = QuickFindUF(10)

    def test_union_operations(self):
        self.qf.union(4, 3)
        self.assertEqual(self.qf.id, [0, 1, 2, 3, 3, 5, 6, 7, 8, 9])

        self.qf.union(3, 8)
        self.assertEqual(self.qf.id, [0, 1, 2, 8, 8, 5, 6, 7, 8, 9])

        self.qf.union(6, 5)
        self.assertEqual(self.qf.id, [0, 1, 2, 8, 8, 5, 5, 7, 8, 9])

        self.qf.union(9, 4)
        self.assertEqual(self.qf.id, [0, 1, 2, 8, 8, 5, 5, 7, 8, 8])

        self.qf.union(2, 1)
        self.assertEqual(self.qf.id, [0, 1, 1, 8, 8, 5, 5, 7, 8, 8])

        self.assertTrue(self.qf.connected(8, 9))

        self.assertFalse(self.qf.connected(5, 0))

        self.qf.union(5, 0)
        self.assertEqual(self.qf.id, [0, 1, 1, 8, 8, 0, 0, 7, 8, 8])

        self.qf.union(7, 2)
        self.assertEqual(self.qf.id, [0, 1, 1, 8, 8, 0, 0, 1, 8, 8])

        self.qf.union(6, 1)
        self.assertEqual(self.qf.id, [1, 1, 1, 8, 8, 1, 1, 1, 8, 8])

        self.qf.union(7, 3)
        self.assertEqual(self.qf.id, [8, 8, 8, 8, 8, 8, 8, 8, 8, 8])

if __name__ == "__main__":
    unittest.main()
