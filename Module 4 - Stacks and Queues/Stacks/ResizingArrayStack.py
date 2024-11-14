class ResizingArrayStack():
    def __init__(self):
        self.s = [None]
        self.n = 0
    
    def resize(self, capacity: int):
        new_s = [None] * capacity

        for i in range(self.n):
            new_s[i] = self.s[i]
        
        self.s = new_s

    def push(self, string: str):
        if self.n == len(self.s):
            self.resize(2*(len(self.s)))

        self.s[self.n] = string
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("The list is empty!")
        
        self.n -= 1
        item = self.s[self.n]
        self.s[self.n] = None
        

        if self.n > 0 and self.n == len(self.s)//4:
            self.resize(len(self.s)//2)

        return item

    def is_empty(self):
        return self.n == 0
    
    def __iter__(self):
        self._iter_index = self.n
        return self

    def __next__(self):
        if self._iter_index >= 0:
            item = self.s[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopIteration