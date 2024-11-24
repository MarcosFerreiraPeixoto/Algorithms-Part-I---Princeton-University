class Mergesort():
    def __init__(self, comparator=None):
        self.comparator = comparator

    def sort(self, l, lo=None, hi=None):
        if lo is None and hi is None:
            lo = 0
            hi = len(l) - 1
        
        if lo < hi:
            mid = (lo + hi) // 2 

            self.sort(l, lo, mid)
            self.sort(l, mid + 1, hi)
            
            self.merge(l, lo, mid, hi)

    def merge(self, l, lo, mid, hi):
        l_copy = [i for i in l]
        
        assert(self.is_sorted(l[lo:mid + 1]) == True)
        assert(self.is_sorted(l[mid+1:hi + 1]) == True)
        
        i = lo
        j = mid + 1

        for k in range(lo, hi + 1):
            if j > hi:
                l[k] = l_copy[i]
                i += 1
            elif i > mid:
                l[k] = l_copy[j]
                j += 1
            elif self._less(l_copy[i], l_copy[j]):
                l[k] = l_copy[i]
                i += 1
            else:
                l[k] = l_copy[j]
                j+= 1
    
    def is_sorted(self, l):
        for i in range(1, len(l)):
            
            if self._less(l[i], l[i-1]):
                return False
        
        return True

    def _less(self, a, b):
        if self.comparator:
            return self.comparator(a, b) < 0
        return a < b