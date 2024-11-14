class _Node():
    def __init__(self, value=None, next=None, previous=None):
        self.item = value
        self.next = next
        self.previous = previous

class Deque():
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0
    
    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def add_first(self, value):
        new_node = _Node(value, next=self.first, previous=None)

        if self.is_empty():
            self.last = new_node
        else:
            self.first.previous = new_node

        self.first = new_node
        self.n += 1

    def add_last(self, value):
        new_node = _Node(value, next=None, previous=self.last)

        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node

        self.last = new_node
        self.n += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError("The Deque is empty!")
        
        previous_first = self.first

        if self.n == 1:
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            self.first.previous = None

        self.n -= 1
        return previous_first.item

    def remove_last(self):
        if self.is_empty():
            raise IndexError("The Deque is empty!")
        
        previous_last = self.last
        
        if self.n == 1:
            self.last = None
            self.first = None
        else:
            self.last = self.last.previous
            self.last.next = None

        self.n -= 1
        return previous_last.item

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.next