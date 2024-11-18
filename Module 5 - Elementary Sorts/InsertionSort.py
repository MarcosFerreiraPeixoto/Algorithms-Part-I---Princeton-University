class InsertionSort():
    def sort(self, l):
        for i in range(len(l)):
            for j in range(i, 0, -1):
                if self._less(l[j], l[j-1]):
                    self._exch(l, j, j-1)
                else:
                    break

    def _less(self, a, b):
        return a < b

    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]