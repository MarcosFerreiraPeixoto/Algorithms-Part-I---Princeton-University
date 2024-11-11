class ArrayImplementationStacksOfStrings():
    def __init__(self):
        self.stack = []
        self.stack_size = 0
    
    def push(self, str):
        self.stack.append(str)
        self.stack_size += 1
    
    def pop(self):
        if not self.is_empty():
            self.stack_size -= 1
            return self.stack.pop()
        else:
            raise ValueError("The list is empty!")

    def is_empty(self):
        return True if len(self.stack) == 0 else False