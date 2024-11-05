import unittest
from PercolationStats import PercolationStats  # Ensure PercolationStats is in the same directory or path

class TestPercolationStats(unittest.TestCase):

    def setUp(self):
        # Set parameters for tests
        self.grid_size = 200
        self.trials = 100
        self.perc_stats = PercolationStats(self.grid_size, self.trials)

    def test_mean(self):
        # Check if mean is within reasonable bounds
        mean = self.perc_stats.mean()
        self.assertGreaterEqual(mean, 0.57, "Mean percolation threshold should be >= 0.57")
        self.assertLessEqual(mean, 0.63, "Mean percolation threshold should be <= 0.63")

    def test_stddev(self):
        # Check if standard deviation is within reasonable bounds
        stddev = self.perc_stats.stddev()
        self.assertGreaterEqual(stddev, 0, "Standard deviation should be >= 0")
        self.assertLessEqual(stddev, 0.1, "Standard deviation should be <= 0.1")

    def test_confidence_interval(self):
        # Calculate confidence interval bounds
        conf_lo = self.perc_stats.confidence_lo()
        conf_hi = self.perc_stats.confidence_hi()
        
        # Check if confidence interval is within reasonable bounds
        self.assertGreaterEqual(conf_lo, 0.56, "Confidence lower bound should be >= 0.56")
        self.assertLessEqual(conf_hi, 0.64, "Confidence upper bound should be <= 0.64")
        self.assertLessEqual(conf_lo, conf_hi, "Confidence lower bound should be <= upper bound")

    def test_invalid_parameters(self):
        # Test constructor raises ValueError on invalid parameters
        with self.assertRaises(ValueError):
            PercolationStats(0, 10)
        with self.assertRaises(ValueError):
            PercolationStats(10, 0)
        with self.assertRaises(ValueError):
            PercolationStats(-1, 10)
        with self.assertRaises(ValueError):
            PercolationStats(10, -1)

# Run the tests
if __name__ == "__main__":
    unittest.main()
