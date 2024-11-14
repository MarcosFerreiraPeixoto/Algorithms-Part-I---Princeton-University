class ArrayImplementationStack():
    def __init__(self):
        self.s = []
        self.n = 0
    
    def push(self, str):
        self.s.append(str)
        self.n += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError("The list is empty!")
    
        self.n -= 1
        return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0
    
    def __iter__(self):
        self._iter_index = self.n
        return self

    def __next__(self):
        if self._iter_index >= 0:
            item = self.s[self._iter_index]
            self._iter_index -= 1
            return item
        else:
            raise StopIteration