class Percolation:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("Grid size must be greater than 0.")
        
        self.n = n
        self.virtual_top = 0
        self.virtual_bottom = n**2 + 1
        self.open_site_counter = 0

        self.id = []
        self.size = []
        self.site_open = []

        for i in range(0, n**2+2):
            self.id.append(i)
            self.size.append(1)
            self.site_open.append(False)

    def _get_site_index(self, row: int, col: int) -> int:
        if (1 <= row <= self.n) and (1 <= col <= self.n):
            return ((row - 1) * self.n) + col
        else:
            raise ValueError("The input site does not exist!")

    def _find(self, i: int) -> int:
        val = i

        while val != self.id[val]:
            self.id[val] = self.id[self.id[val]]
            val = self.id[val]

        return val

    def _connected(self, p: int, q: int) -> bool:
        return self._find(p) == self._find(q)

    def _union(self, p: int, q: int):
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return
        
        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

    def is_open(self, row: int, col: int) -> bool:
        return self.site_open[self._get_site_index(row, col)]

    def open(self, row: int, col: int):
        if not self.is_open(row, col):
            n = self._get_site_index(row, col)
            self.open_site_counter += 1

            self.site_open[n] = True

            # Connecting with open neighbors
            neighbors = [
                (row, col - 1), # left neighbor 
                (row, col + 1), # right neighbor 
                (row - 1, col), # top neighbor 
                (row + 1, col)  # bottom neighbor 
            ]

            for n_row, n_col in neighbors:
                if (1 <= n_row <= self.n) and (1 <= n_col <= self.n) and self.is_open(n_row, n_col):
                    self._union(n, self._get_site_index(n_row, n_col))
            
            # Connection with virtual end and start
            if row == 1:
                self._union(n, self.virtual_top)
            if row == self.n:
                self._union(n, self.virtual_bottom)

    def is_full(self, row: int, col: int) -> bool:
        return self._connected(self.virtual_top, self._get_site_index(row, col))

    def number_of_open_sites(self) -> int:
        return self.open_site_counter

    def percolates(self) -> bool:
        return self._connected(self.virtual_top, self.virtual_bottom)
