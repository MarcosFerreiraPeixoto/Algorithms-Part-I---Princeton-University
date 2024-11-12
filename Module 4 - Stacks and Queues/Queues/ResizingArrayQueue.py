class ResizingArrayQueue():
    def __init__(self):
        self.s = [None]
        self.head = 0
        self.tail = 0
    
    def resize(self, capacity: int):
        new_s = [None] * capacity

        for i in range(self.tail - self.head):
            new_s[i] = self.s[self.head + i]
        
        self.s = new_s
        self.tail = self.tail - self.head
        self.head = 0

    def enqueue(self, string: str):
        if self.tail == len(self.s):
            self.resize(2 * len(self.s))

        self.s[self.tail] = string
        self.tail += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.s[self.head]
            self.s[self.head] = None
            self.head += 1
            
            if (self.tail - self.head) <= len(self.s) // 4 and len(self.s) > 1:
                self.resize(len(self.s) // 2)

            return item
        else:
            raise ValueError("The queue is empty!")

    def is_empty(self):
        return self.tail == self.head
    
    def __iter__(self):
        self._iter_index = self.head
        return self

    def __next__(self):
        if self._iter_index < self.tail:
            item = self.s[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopIteration