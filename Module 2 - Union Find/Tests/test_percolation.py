import unittest
import time
from Percolation import Percolation

class TestPercolation(unittest.TestCase):
    def test_initialization(self):
        perc = Percolation(5)
        self.assertEqual(perc.n, 5)
        self.assertFalse(perc.percolates())
        self.assertEqual(perc.number_of_open_sites(), 0)

        with self.assertRaises(ValueError):
            Percolation(0)

    def test_open_site(self):
        perc = Percolation(5)
        self.assertFalse(perc.is_open(1, 1))  
        
        perc.open(1, 1)
        self.assertTrue(perc.is_open(1, 1))   
        
        perc.open(1, 1)  
        self.assertEqual(perc.number_of_open_sites(), 1)  

    def test_is_full(self):
        perc = Percolation(5)
        perc.open(1, 1)  
        self.assertTrue(perc.is_full(1, 1))  

        perc.open(2, 1)
        self.assertTrue(perc.is_full(2, 1))  

        perc.open(3, 1)
        self.assertTrue(perc.is_full(3, 1))  

    def test_percolates(self):
        perc = Percolation(5)
        
        perc.open(1, 1)
        perc.open(2, 1)
        perc.open(3, 1)
        perc.open(4, 1)
        perc.open(5, 1)
        
        self.assertTrue(perc.percolates())  

    def test_percolates_2(self):
        n = 8
        perc = Percolation(n)

        open_sites = [
            (1, 3), (1, 4), (1, 5), 
            (2, 1), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 1), (3, 2), (3, 3), (3, 6), (3, 7),
            (4, 3), (4, 4), (4, 6), (4, 7), (4, 8),
            (5, 2), (5, 3), (5, 4), (5, 6), (5, 7),
            (6, 2), (6, 7), (6, 8),
            (7, 1), (7, 3), (7, 5), (7, 6), (7, 7), (7, 8),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)
        ]

        for row, col in open_sites:
            perc.open(row, col)
        
        self.assertTrue(perc.percolates())

    def test_no_percolation(self):
        perc = Percolation(5)
        perc.open(1, 1)
        perc.open(2, 1)
        perc.open(3, 1)
        perc.open(4, 1)
        
        self.assertFalse(perc.percolates())  
    
    def test_no_percolation_2(self):
        n = 8
        perc = Percolation(n)

        open_sites = [
            (1, 3), (1, 4), (1, 6), 
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 1), (3, 2), (3, 5), (3, 6),
            (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 1), (5, 7), (5, 8),
            (6, 2), (6, 4), (6, 5), (6, 6),
            (7, 2), (7, 3), (7, 5), (7, 6), (7, 8),
            (8, 1), (8, 3), (8, 7)
        ]
        
        for row, col in open_sites:
            perc.open(row, col)
        
        self.assertFalse(perc.percolates())

    
    def test_diagonal_no_percolation(self):
        perc = Percolation(5)
        
        perc.open(1, 1)
        perc.open(2, 2)
        perc.open(3, 3)
        perc.open(4, 4)
        perc.open(5, 5)
        
        self.assertFalse(perc.percolates())  

    def test_number_of_open_sites(self):
        perc = Percolation(5)
        perc.open(1, 1)
        perc.open(2, 2)
        perc.open(3, 3)
        
        self.assertEqual(perc.number_of_open_sites(), 3)
        
        perc.open(2, 2)  
        self.assertEqual(perc.number_of_open_sites(), 3)  

    def test_invalid_indices(self):
        perc = Percolation(5)
        
        with self.assertRaises(ValueError):
            perc.open(0, 1)
        
        with self.assertRaises(ValueError):
            perc.is_open(6, 1)
        
        with self.assertRaises(ValueError):
            perc.is_full(1, 6)

    def test_edge_connections(self):
        perc = Percolation(3)
        perc.open(1, 1)  
        perc.open(1, 2)  
        self.assertTrue(perc.is_full(1, 2))  

        perc.open(2, 2)  
        self.assertTrue(perc.is_full(2, 2))  

    def test_top_bottom_virtual_sites(self):
        perc = Percolation(2)
        
        perc.open(1, 1)
        perc.open(2, 1)
        
        self.assertTrue(perc.percolates())


class TestPercolationPerformance(unittest.TestCase):
    def test_constructor_performance(self):
        n = 1000  # Large grid size to test performance
        start_time = time.time()
        
        # Creating an n x n grid
        perc = Percolation(n)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # The constructor should be fast even for large n.
        # We are using a conservative threshold, assuming n^2 time complexity.
        self.assertTrue(elapsed_time < 1, f"Constructor took too long: {elapsed_time} seconds")

    def test_instance_methods_performance(self):
        n = 1000
        perc = Percolation(n)

        # Test open() performance with a random site
        start_time = time.time()
        perc.open(1, 1)
        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 0.001, f"open() took too long: {elapsed_time} seconds")

        # Test is_open() performance
        start_time = time.time()
        is_open = perc.is_open(1, 1)
        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 0.001, f"is_open() took too long: {elapsed_time} seconds")

        # Test is_full() performance
        start_time = time.time()
        is_full = perc.is_full(1, 1)
        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 0.001, f"is_full() took too long: {elapsed_time} seconds")

        # Test percolates() performance
        start_time = time.time()
        does_percolate = perc.percolates()
        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 0.001, f"percolates() took too long: {elapsed_time} seconds")

if __name__ == "__main__":
    unittest.main()
