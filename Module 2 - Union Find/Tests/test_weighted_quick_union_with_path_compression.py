import unittest
from WeightedQuickUnionWithPathCompressionUF import WeightedQuickUnionWithPathCompressionUF

class TestWeightedQuickUnionWithPathCompressionUF(unittest.TestCase):
    def setUp(self):
        self.wquwpc = WeightedQuickUnionWithPathCompressionUF(10)

    def test_union_operations(self):
        self.wquwpc.union(4,3)
        assert(self.wquwpc.id == [0, 1, 2, 4, 4, 5, 6, 7, 8, 9])

        self.wquwpc.union(3,8)
        assert(self.wquwpc.id == [0, 1, 2, 4, 4, 5, 6, 7, 4, 9])

        self.wquwpc.union(6,5)
        assert(self.wquwpc.id == [0, 1, 2, 4, 4, 6, 6, 7, 4, 9])

        self.wquwpc.union(9,4)
        assert(self.wquwpc.id == [0, 1, 2, 4, 4, 6, 6, 7, 4, 4])

        self.wquwpc.union(2,1)
        assert(self.wquwpc.id == [0, 2, 2, 4, 4, 6, 6, 7, 4, 4])

        assert(self.wquwpc.connected(8,9) == True)
        assert(self.wquwpc.connected(5,0) == False)

        self.wquwpc.union(5,0)
        assert(self.wquwpc.id == [6, 2, 2, 4, 4, 6, 6, 7, 4, 4])

        self.wquwpc.union(7,2)
        assert(self.wquwpc.id == [6, 2, 2, 4, 4, 6, 6, 2, 4, 4])

        self.wquwpc.union(6,1)
        assert(self.wquwpc.id == [6, 2, 6, 4, 4, 6, 6, 2, 4, 4])

        self.wquwpc.union(7,3)
        assert(self.wquwpc.id == [6, 2, 6, 4, 6, 6, 6, 6, 4, 4])

if __name__ == "__main__":
    unittest.main()
