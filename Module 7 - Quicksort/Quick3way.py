from random import randrange

class Quick3way():
    def __init__(self, comparator=None):
        self.comparator = comparator

    def sort(self, l, lo=None, hi=None):
        if len(l) <= 1:
            return
        elif lo is None and hi is None:
            self._shuffle(l)
            lo = 0
            hi = len(l) - 1
        elif lo >= hi:
            return

        lt, gt = self._partition(l, lo, hi)

        self.sort(l, lo, lt - 1)
        self.sort(l, gt + 1, hi)


    def _shuffle(self, l):
        for i in range(len(l)):
            random_index = randrange(0, i + 1)

            self._exch(l, i, random_index)

    def _partition(self, l, lo, hi):
        i = lo + 1
        lt = lo
        gt = hi

        while True:
            if self._less(l[i], l[lt]):
                self._exch(l, i, lt)

                i += 1
                lt += 1            
            elif self._less(l[lt], l[i]):
                self._exch(l, i, gt)

                gt -= 1
            else:
                i += 1

            if gt < i:
                break

        return lt, gt

    def is_sorted(self, l):
        for i in range(1, len(l)):
            
            if self._less(l[i], l[i-1]):
                return False
        
        return True
    
    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) < 0
        return a < b