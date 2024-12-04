class MinPQ():
    def __init__(self, comparator=None) -> None:
        self.comparator = comparator
        self.s = [None]
        self.n = 0

    def insert(self, v):
        self.s.append(v)
        self.n += 1

        self._swim(self.n)
    
    def del_min(self):
        if self.is_empty():
            raise ValueError("The queue is empty!")

        self._exch(self.s, 1, self.n)
        min = self.s.pop()
        self.n -= 1
        self._sink()

        return min

    def min(self):
        if self.is_empty():
            raise ValueError("The queue is empty!")
        return self.s[1]

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def _swim(self, index):
        while index > 1:
            parent = index//2
            
            if self._less(self.s[parent], self.s[index]):
                self._exch(self.s, index, parent)

                index = parent
            else:
                break
    
    def _sink(self):
        index = 1
        child = index * 2

        while child <= self.n:
            if child + 1 <= self.n and self._less(self.s[child], self.s[child + 1]):
                child += 1
            
            if self._less(self.s[index], self.s[child]):
                self._exch(self.s, index, child)
                index = child
                child = index * 2
            else:
                break
                
    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) > 0
        return a > b