class HSort():
    def __init__(self, h, comparator=None):
        self.h = h
        self.comparator = comparator

    def sort(self, l):
        for i in range(self.h, len(l)):
            for j in range(i, self.h - 1, -self.h):
                if self._less(l[j], l[j- self.h]):
                    self._exch(l, j, j - self.h)
                else:
                    break

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) < 0
        return a < b

    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]