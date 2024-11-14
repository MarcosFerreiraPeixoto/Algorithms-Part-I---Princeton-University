from random import randrange, shuffle

class _Node():
    def __init__(self):
        self.item = None
        self.next: _Node = None

class RandomizedQueue():
    def __init__(self):
        self.first = None
        self.n = 0

    def is_empty(self):
        return self.n == 0
    
    def size(self):
        return self.n

    def enqueue(self, string):
        old_first = self.first

        self.first = _Node()
        self.first.item = string
        self.first.next = old_first
        self.n += 1
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("The list is empty!")

        n = randrange(0, self.n)
        
        if n == 0:
            item = self.first.item
            self.first = self.first.next
        else:
            node = self.first
            previous = None
            for _ in range(n):
                previous = node
                node = node.next
            
            item = node.item
            previous.next = node.next
        
        self.n -= 1
        return item

    def sample(self):
        n = randrange(0, self.n)
        node = self.first

        for _ in range(n):
            node = node.next
        
        item = node.item

        return item
        
    def __iter__(self):
        return self.RandomizedQueueIterator(self)

    class RandomizedQueueIterator:
        def __init__(self, randomized_queue):
            self.items = []
            current = randomized_queue.first
            
            while current != None:
                self.items.append(current.item)
                current = current.next
            
            shuffle(self.items)
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.items):
                item = self.items[self.index]
                self.index += 1
                return item
            else:
                raise StopIteration()