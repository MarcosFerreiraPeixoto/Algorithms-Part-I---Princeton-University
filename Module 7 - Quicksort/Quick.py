from random import randrange

class Quick():
    def __init__(self, comparator=None):
        self.comparator = comparator

    def sort(self, l, lo=None, hi=None):
        if len(l) <= 1:
            return l
        elif lo is None and hi is None:
            self._shuffle(l)
            lo = 0
            hi = len(l) - 1
        elif lo >= hi:
            return

        j = self._partition(l, lo, hi)

        self.sort(l, lo, j - 1)
        self.sort(l, j + 1, hi)

    def select(self, l, nth, lo=None, hi=None):
        if len(l) < nth:
            raise ValueError(f"The iterable has less than {nth} elements!")
        elif nth <= 0:
            raise ValueError(f"The selection index should be an integer greater than zero.")
        elif len(l) == 1:
            return l[0]
        elif lo is None and hi is None:
            self._shuffle(l)
            lo = 0
            hi = len(l) - 1
        elif lo == hi:
            return l[lo]

        j = self._partition(l, lo, hi)
        
        if (j + 1) < nth:
            return self.select(l, nth, j + 1, hi)
        elif (j + 1) > nth:
            return self.select(l, nth, lo, j - 1)
        else:
            return l[j]

    def _shuffle(self, l):
        for i in range(len(l)):
            random_index = randrange(0, i + 1)

            self._exch(l, i, random_index)

    def _partition(self, l, lo, hi):
        i = lo + 1
        j = hi

        while True:
            while self._less(l[i], l[lo]):
                if i >= j:
                    break
                i += 1
            while self._less(l[lo], l[j]):
                if j < i:
                    break
                j -= 1

            if j <= i:
                break

            self._exch(l, i, j)
        
        self._exch(l, lo, j)

        return j

    def is_sorted(self, l):
        for i in range(1, len(l)):
            
            if self._less(l[i], l[i-1]):
                return False
        
        return True
    
    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) <= 0
        return a <= b