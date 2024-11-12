class ArrayImplementationStack():
    def __init__(self):
        self.s = []
        self.n = 0
    
    def push(self, str):
        self.s.append(str)
        self.n += 1
    
    def pop(self):
        if not self.is_empty():
            self.n -= 1
            return self.s.pop()
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if len(self.s) == 0 else False
    
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