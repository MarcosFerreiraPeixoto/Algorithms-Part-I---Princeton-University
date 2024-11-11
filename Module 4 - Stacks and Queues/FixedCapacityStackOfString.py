class FixedCapacityStackOfString():
    def __init__(self, max_size: int):
        self.s = [None] * max_size 
        self.n = 0
    
    def push(self, string):
        self.n += 1
        self.s[self.n] = string
    
    def pop(self):
        if not self.is_empty():
            item = self.s[self.n]
            self.n -= 1
            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False