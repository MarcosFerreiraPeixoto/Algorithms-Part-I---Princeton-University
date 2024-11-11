class _Node():
    def __init__(self):
        self.item: str = None
        self.next: _Node = None

class LinkedStacksOfString():
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
        if not self.is_empty():
            item = self.first.item
            self.first = self.first.next
            self.n -= 1

            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False