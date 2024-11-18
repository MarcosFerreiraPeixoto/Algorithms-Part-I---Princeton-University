class ShellSort():
    def sort(self, l):
        h = 1
        while h < len(l)/3:
            h = 3 * h + 1
        
        while h >= 1:
            for i in range(h, len(l)):
                for j in range(i, h - 1, -h):
                    if self._less(l[j], l[j- h]):
                        self._exch(l, j, j - h)
                    else:
                        break
            
            h = (h - 1)//3
    
    def _less(self, a, b):
        return a < b

    def _exch(self, l, i, j):
        l[i], l[j] = l[j], l[i]