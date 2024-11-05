import unittest
from WeightedQuickUnionUF import WeightedQuickUnionUF

class TestWeightedQuickUnionUF(unittest.TestCase):
    def setUp(self):
        self.wqu = WeightedQuickUnionUF(10)

    def test_union_operations(self):
        self.wqu.union(4,3)
        assert(self.wqu.id == [0, 1, 2, 4, 4, 5, 6, 7, 8, 9])

        self.wqu.union(3,8)
        assert(self.wqu.id == [0, 1, 2, 4, 4, 5, 6, 7, 4, 9])

        self.wqu.union(6,5)
        assert(self.wqu.id == [0, 1, 2, 4, 4, 6, 6, 7, 4, 9])

        self.wqu.union(9,4)
        assert(self.wqu.id == [0, 1, 2, 4, 4, 6, 6, 7, 4, 4])

        self.wqu.union(2,1)
        assert(self.wqu.id == [0, 2, 2, 4, 4, 6, 6, 7, 4, 4])

        assert(self.wqu.connected(8,9) == True)
        assert(self.wqu.connected(5,0) == False)

        self.wqu.union(5,0)
        assert(self.wqu.id == [6, 2, 2, 4, 4, 6, 6, 7, 4, 4])

        self.wqu.union(7,2)
        assert(self.wqu.id == [6, 2, 2, 4, 4, 6, 6, 2, 4, 4])

        self.wqu.union(6,1)
        assert(self.wqu.id == [6, 2, 6, 4, 4, 6, 6, 2, 4, 4])

        self.wqu.union(7,3)
        assert(self.wqu.id == [6, 2, 6, 4, 6, 6, 6, 2, 4, 4])

if __name__ == "__main__":
    unittest.main()
