class SelectionSort():
    def __init__(self, comparator=None):
        self.comparator = comparator

    def sort(self, l):
        for i in range(len(l)):
            min_index = i
            for j in range(i, len(l)):
                if self._less(l[j], l[min_index]):
                    min_index = j

            self._exch(l, i, min_index)

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) < 0
        return a < b

    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]