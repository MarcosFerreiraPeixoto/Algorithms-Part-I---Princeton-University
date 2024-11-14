from random import randrange, shuffle

class RandomizedQueue:
    def __init__(self):
        self.items = []
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def enqueue(self, item):
        if item is None:
            raise ValueError("Argument to enqueue() cannot be None")
        
        self.items.append(item)
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")

        n = randrange(self.n)
        
        item = self.items[n]
        self.items[n] = self.items[-1]
        self.items.pop()
        
        self.n -= 1
        return item

    def sample(self):
        if self.is_empty():
            raise IndexError("The queue is empty")

        n = randrange(self.n)
        return self.items[n]

    def __iter__(self):
        shuffled_items = self.items[:]
        shuffle(shuffled_items)
        self._iter_index = 0
        self._iter_items = shuffled_items
        return self

    def __next__(self):
        if self._iter_index < len(self._iter_items):
            item = self._iter_items[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopIteration()