class ResizingArrayStackOfString():
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
        if not self.is_empty():
            self.n -= 1
            item = self.s[self.n]
            self.s[self.n] = None
            

            if self.n > 0 and self.n == len(self.s)//4:
                self.resize(len(self.s)//2)

            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False