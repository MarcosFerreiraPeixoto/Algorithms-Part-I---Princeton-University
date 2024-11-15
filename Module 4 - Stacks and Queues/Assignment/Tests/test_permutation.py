import unittest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
from Assignment.Permutation import Permutation
import os


class TestPermutation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_random(self, mock_stdout):
        sys.argv = ['Permutation.py', '3']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "distinct.txt")

        p = Permutation(3, file_path)
        p.enqueue_from_file()
        p.dequeue_and_print()

        output = mock_stdout.getvalue().splitlines()

        self.assertEqual(len(output), 3)
        for item in output:
            self.assertIn(item, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_zero(self, mock_stdout):
        sys.argv = ['Permutation.py', '0']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "distinct.txt")

        p = Permutation(0, file_path)
        p.enqueue_from_file()
        p.dequeue_and_print()

        output = mock_stdout.getvalue().splitlines()

        self.assertEqual(len(output), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_k_equals_n(self, mock_stdout):
        sys.argv = ['Permutation.py', '9']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "distinct.txt")

        p = Permutation(9, file_path)
        p.enqueue_from_file()
        p.dequeue_and_print()

        output = mock_stdout.getvalue().splitlines()

        self.assertEqual(len(output), 9)
        for item in output:
            self.assertIn(item, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_duplicate_items(self, mock_stdout):
        sys.argv = ['Permutation.py', '6']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "duplicates.txt")

        p = Permutation(6, file_path)
        p.enqueue_from_file()
        p.dequeue_and_print()

        output = mock_stdout.getvalue().splitlines()

        self.assertEqual(len(output), 6)
        for item in output:
            self.assertIn(item, ['AA', 'BB', 'CC'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_empty_file(self, mock_stdout):
        sys.argv = ['Permutation.py', '3']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "empty.txt")

        p = Permutation(3, file_path)
        p.enqueue_from_file()
        p.dequeue_and_print()

        output = mock_stdout.getvalue().splitlines()

        self.assertEqual(len(output), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_permutation_invalid_file(self, mock_stdout):
        sys.argv = ['Permutation.py', '3']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "test_assets", "nonexistent.txt")

        with self.assertRaises(SystemExit):
            p = Permutation(3, file_path)
            p.enqueue_from_file()
            p.dequeue_and_print()

if __name__ == '__main__':
    unittest.main()
