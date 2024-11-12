class FixedCapacityStack():
    def __init__(self, max_size: int):
        self.s = [None] * max_size 
        self.n = 0
    
    def push(self, string):
        if self.n < len(self.s):
            self.s[self.n] = string
            self.n += 1
        else:
            raise ValueError("The Stack is full! Pop a value before pushing a new one.")
    
    def pop(self):
        if not self.is_empty():
            self.n -= 1
            item = self.s[self.n]
            
            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False