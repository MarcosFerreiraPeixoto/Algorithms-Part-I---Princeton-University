class FixedCapacityStack():
    def __init__(self, max_size: int):
        self.s = [None] * max_size 
        self.n = 0
    
    def push(self, string):
        if self.n >= len(self.s):
            raise ValueError("The Stack is full! Pop a value before pushing a new one.")
        
        self.s[self.n] = string
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("The list is empty!")
        
        self.n -= 1
        item = self.s[self.n]
        
        return item       

    def is_empty(self):
        return self.n == 0