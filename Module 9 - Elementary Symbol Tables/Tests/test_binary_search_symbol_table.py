import unittest
from BinarySearchSTSymbolTable import BinarySearchST  # Adjust the import to your file structure

class TestBinarySearchST(unittest.TestCase):

    def setUp(self):
        self.st = BinarySearchST()

    def test_empty_table(self):
        self.assertTrue(self.st.is_empty())
        self.assertEqual(self.st.size(), 0)
        self.assertEqual(self.st.keys(), [])

    def test_put_and_get(self):
        self.st.put("a", 1)
        self.assertFalse(self.st.is_empty())
        self.assertEqual(self.st.size(), 1)
        self.assertEqual(self.st.get("a"), 1)

        self.st.put("b", 2)
        self.assertEqual(self.st.size(), 2)
        self.assertEqual(self.st.get("b"), 2)

    def test_overwrite_value(self):
        self.st.put("a", 1)
        self.st.put("a", 10)
        self.assertEqual(self.st.size(), 1)
        self.assertEqual(self.st.get("a"), 10)

    def test_delete(self):
        self.st.put("a", 1)
        self.st.put("b", 2)
        self.st.put("c", 3)
        
        self.st.delete("b")
        self.assertEqual(self.st.size(), 2)
        self.assertNotIn("b", self.st.keys())
        self.assertRaises(KeyError, self.st.get, "b")

        # Ensure other keys are unaffected
        self.assertEqual(self.st.get("a"), 1)
        self.assertEqual(self.st.get("c"), 3)

    def test_contains(self):
        self.st.put("a", 1)
        self.assertTrue(self.st.contains("a"))
        self.assertFalse(self.st.contains("b"))

    def test_get_key_error(self):
        with self.assertRaises(KeyError):
            self.st.get("nonexistent")

    def test_delete_key_error(self):
        with self.assertRaises(KeyError):
            self.st.delete("nonexistent")

    def test_empty_after_delete(self):
        self.st.put("a", 1)
        self.st.delete("a")
        self.assertTrue(self.st.is_empty())

    def test_keys(self):
        self.st.put("a", 1)
        self.st.put("b", 2)
        self.st.put("c", 3)
        self.assertEqual(set(self.st.keys()), {"a", "b", "c"})

    def test_duplicate_keys(self):
        self.st.put("a", 1)
        self.st.put("a", 2)
        self.assertEqual(self.st.size(), 1)
        self.assertEqual(self.st.get("a"), 2)

    def test_mixed_operations(self):
        self.st.put("a", 1)
        self.st.put("b", 2)
        self.st.put("c", 3)
        self.st.delete("b")
        self.st.put("d", 4)
        self.st.put("a", 10)  # Update an existing key
        self.assertEqual(self.st.size(), 3)
        self.assertEqual(set(self.st.keys()), {"a", "c", "d"})
        self.assertEqual(self.st.get("a"), 10)
        self.assertEqual(self.st.get("c"), 3)
        self.assertEqual(self.st.get("d"), 4)

    def test_large_number_of_operations(self):
        for i in range(1000):
            self.st.put(f"key{i}", i)
        self.assertEqual(self.st.size(), 1000)

        # Test retrieval of a subset of keys
        for i in range(0, 1000, 100):
            self.assertEqual(self.st.get(f"key{i}"), i)

        # Test deletion of half the keys
        for i in range(0, 1000, 2):
            self.st.delete(f"key{i}")
        self.assertEqual(self.st.size(), 500)

        # Ensure remaining keys are correct
        for i in range(1, 1000, 2):
            self.assertEqual(self.st.get(f"key{i}"), i)

    def test_non_string_keys(self):
        self.st.put(1, "one")
        self.st.put(2.5, "two point five")
        self.assertEqual(self.st.get(1), "one")
        self.assertEqual(self.st.get(2.5), "two point five")
        self.assertTrue(self.st.contains(2.5))
        self.st.delete(1)
        self.assertFalse(self.st.contains(1))

    def test_edge_cases_with_empty_table(self):
        with self.assertRaises(KeyError):
            self.st.delete("nonexistent")

        self.assertFalse(self.st.contains("nonexistent"))
        self.assertEqual(self.st.keys(), [])

    def test_sorted_keys(self):
        self.st.put("d", 4)
        self.st.put("b", 2)
        self.st.put("a", 1)
        self.st.put("c", 3)

        # Verify keys are sorted
        self.assertEqual(self.st.keys(), ["a", "b", "c", "d"])

    def test_key_collision(self):
        self.st.put("a", 1)
        self.st.put("a", 2)
        self.st.put("a", 3)
        self.assertEqual(self.st.size(), 1)  # Only one key-value pair for "a"
        self.assertEqual(self.st.get("a"), 3)

    def test_stress_on_edge_conditions(self):
        # Insert and remove the same key repeatedly
        for _ in range(100):
            self.st.put("edge", "value")
            self.assertEqual(self.st.get("edge"), "value")
            self.st.delete("edge")
            self.assertFalse(self.st.contains("edge"))
            self.assertTrue(self.st.is_empty())

if __name__ == "__main__":
    unittest.main()
