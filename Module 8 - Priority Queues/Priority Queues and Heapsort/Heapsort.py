class Heapsort():
    def __init__(self, comparator=None) -> None:
        self.comparator = comparator

    def sort(self, l):
        i = (len(l) // 2) - 1

        while i >= 0:
            self._sink(l, i, len(l))
            i -= 1

        for j in range(len(l) - 1, -1 , -1):
            self._exch(l, 0, j)
            self._sink(l, 0, j)

    def _sink(self, l, index, n):
        child = 2 * index + 1

        while child < n:
            if child + 1 < n and self._less(l[child], l[child + 1]):
                child += 1
            
            if self._less(l[index], l[child]):
                self._exch(l, index, child)
                index = child
                child = 2 * index + 1
            else:
                break

    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) < 0
        return a < b