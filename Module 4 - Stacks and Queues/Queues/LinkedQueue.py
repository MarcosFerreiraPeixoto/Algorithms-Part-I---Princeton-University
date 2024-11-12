class _Node():
    def __init__(self):
        self.item: str = None
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
        if not self.is_empty():
            item = self.first.item
            self.first = self.first.next
            self.n -= 1

            return item
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if self.n == 0 else False