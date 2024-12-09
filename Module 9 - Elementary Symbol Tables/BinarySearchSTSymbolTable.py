class BinarySearchST:
    def __init__(self):
        self.key_list = []
        self.value_list = []

    def _rank(self, key, lo=None, hi=None):
        if lo is None or hi is None:
            lo, hi = 0, len(self.key_list) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.key_list[mid]:
                hi = mid - 1
            elif key > self.key_list[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def put(self, key, value):
        rank_value = self._rank(key)

        if rank_value < len(self.key_list) and self.key_list[rank_value] == key:
            self.value_list[rank_value] = value
        else:
            self.key_list.insert(rank_value, key)
            self.value_list.insert(rank_value, value)

    def get(self, key):
        if self.is_empty():
            raise KeyError(f"Key {key} not found.")
        
        rank_value = self._rank(key)
        if rank_value < len(self.key_list) and self.key_list[rank_value] == key:
            return self.value_list[rank_value]
        
        raise KeyError(f"Key {key} not found.")

    def delete(self, key):
        if self.is_empty():
            raise KeyError(f"Key {key} not found.")
        
        rank_value = self._rank(key)
        if rank_value < len(self.key_list) and self.key_list[rank_value] == key:
            del self.key_list[rank_value]
            del self.value_list[rank_value]
        else:
            raise KeyError(f"Key {key} not found.")

    def contains(self, key):
        if self.is_empty():
            return False
        
        rank_value = self._rank(key)
        return rank_value < len(self.key_list) and self.key_list[rank_value] == key

    def is_empty(self):
        return len(self.key_list) == 0

    def size(self):
        return len(self.key_list)

    def keys(self):
        return self.key_list
