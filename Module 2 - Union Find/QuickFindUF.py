class QuickFindUF:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Number of elements must be non-negative")
        
        self.id = []
        self.counter = n

        for i in range(0, n):
            self.id.append(i)

    def count(self):
        return self.counter

    def validate(self, p: int):
        n = len(self.id)
        if p < 0 or p >= n:
            raise ValueError(f"index {p} is not between 0 and {n - 1}")

    def find(self, p: int):
        self.validate(p)
        return self.id[p]

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            return

        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
        self.counter -= 1

