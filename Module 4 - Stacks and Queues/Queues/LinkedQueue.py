class _Node():
    def __init__(self):
        self.item = None
        self.next: _Node = None

class LinkedQueue():
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0
    
    def enqueue(self, string):
        old_last = self.last

        self.last = _Node()
        self.last.item = string
        self.last.next = None
        
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

        self.n += 1
    
    def dequeue(self):
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