class SequentialST():
    def __init__(self):
        self.key_list = []
        self.value_list = []

    def put(self, key, value):
        for i in range(len(self.key_list)):
            if self.key_list[i] == key:
                self.value_list[i] = value
                return

        self.key_list.append(key)
        self.value_list.append(value)
    
    def get(self, key):
        for i in range(len(self.key_list)):
            if self.key_list[i] == key:
                return self.value_list[i]
        
        raise KeyError(key)

    def delete(self, key):
        for i in range(len(self.key_list)):
            if self.key_list[i] == key:
                self.key_list[i], self.key_list[-1] = self.key_list[-1], self.key_list[i]
                self.value_list[i], self.value_list[-1] = self.value_list[-1], self.value_list[i]

                self.key_list.pop()
                self.value_list.pop()
                return

        raise KeyError(key)

    def contains(self, key):
        for i in range(len(self.key_list)):
            if self.key_list[i] == key:
                return True
        
        return False

    def is_empty(self):
        return len(self.key_list) == 0

    def size(self):
        return len(self.key_list)

    def keys(self):
        return self.key_list