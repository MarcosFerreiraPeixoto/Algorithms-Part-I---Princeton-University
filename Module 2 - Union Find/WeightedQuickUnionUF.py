class WeightedQuickUnionUF():
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Number of elements must be non-negative")
        
        self.id = []
        self.size = []
        self.count = 0

        for i in range(0, n):
            self.id.append(i)
            self.size.append(1)
    
    def count(self):
        return self.count

    def validate(self, p: int):
        n = len(self.id)
        if p < 0 or p >= n:
            raise ValueError(f"index {p} is not between 0 and {n - 1}")

    def find(self, p: int):
        self.validate(p)
        val = p

        while val != self.id[val]:
            val = self.id[val]

        return val

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        self.count -= 1