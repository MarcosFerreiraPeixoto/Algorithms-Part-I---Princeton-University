class _Node():
    def __init__(self):
        self.item: str = None
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
        if not self.is_empty():
            item = self.first.item
            self.first = self.first.next
            self.n -= 1

            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False
        
    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.value
            current = current.next