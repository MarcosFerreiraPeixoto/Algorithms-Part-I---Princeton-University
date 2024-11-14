class _Node():
    def __init__(self):
        self.item = None
        self.next: _Node = None

class LinkedStack():
    def __init__(self):
        self.first = None
        self.n = 0
    
    def push(self, string):
        old_first = self.first

        self.first = _Node()
        self.first.item = string
        self.first.next = old_first
        self.n += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("The list is empty!")
        
        item = self.first.item
        self.first = self.first.next
        self.n -= 1

        return item   

    def is_empty(self):
        return self.n == 0
        
    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.next