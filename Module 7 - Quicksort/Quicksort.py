class Quicksort():
    def sort(self, l, lo=None, hi=None):
        if lo is None and hi is None:
            lo = 0
            hi = len(l) -1 
        elif lo == hi:
            return

        value = l[lo]

        i = l[lo + 1]
        j = l[hi] 

        while j >= i:
            while l[i] <= value:
                i += 1

            while l[j] > value:
                j -= 1
            
            l[i], l[j] = l[j], l[i]

        l[0], l[j] = l[j], l[0]

        self.sort(l, lo, j)
        self.sort(l, i, hi)

    def is_sorted(self, l):
        for i in range(1, len(l)):
            
            if self._less(l[i], l[i-1]):
                return False
        
        return True
    
    def _less(self, a, b):
        return a < b